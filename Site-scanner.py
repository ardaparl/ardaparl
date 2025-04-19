import requests from bs4 import BeautifulSoup

Banner

print("="*50) print("     Gelişmiş Site Güvenlik Bilgi Aracı") print("="*50)

Kullanıcıdan URL al

url = input("Site adresini yaz (https:// ile): ")

1. Admin Panel Finder

admin_paths = ["/admin", "/admin/login", "/admin.php", "/adminpanel"] print("\n[+] Admin Panel Taraması Başladı...") for path in admin_paths: test_url = url + path try: response = requests.get(test_url) if response.status_code == 200: print(f"[+] Admin panel bulundu: {test_url}") except: pass

2. WAF Tespiti

waf_signatures = { "Cloudflare": "cloudflare", "Akamai": "akamai", "Sucuri": "sucuri" } print("\n[+] WAF Tespiti Yapılıyor...") try: headers = {"User-Agent": "A'*100"} response = requests.get(url, headers=headers) for waf, sig in waf_signatures.items(): if sig in response.headers.get("Server", "").lower(): print(f"[!] WAF tespit edildi: {waf}") except: pass

3. Directory Scanner

print("\n[+] Dizin Taraması Başladı...") dirs = ["backup", "config", "admin", "test", ".git"] for d in dirs: full_url = f"{url}/{d}" try: r = requests.get(full_url) if r.status_code == 200: print(f"[+] Dizin bulundu: {full_url}") except: pass

4. JSON ve JavaScript Endpoint Taraması

print("\n[+] JSON/JS Uç Nokta Taraması Başladı...") try: soup = BeautifulSoup(response.text, "html.parser") scripts = soup.find_all("script") for s in scripts: if s.get("src") and (".js" in s["src"] or ".json" in s["src"]): print(f"[JS/JSON] {s['src']}") except: pass

5. Basit SQL Injection Testi

print("\n[+] SQL Injection Testi Yapılıyor...") test_payload = "' OR '1'='1" test = f"{url}?id={test_payload}" try: r = requests.get(test) if "sql" in r.text.lower() or "syntax" in r.text.lower(): print("[!] Olası SQLi açığı bulundu!") else: print("[-] SQLi zayıflığı bulunamadı.") except: pass

print("\n[+] Tarama tamamlandı.")

