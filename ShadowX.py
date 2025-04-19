import os
import socket
import requests
import whois

def port_scanner():
    target = input("Hedef IP: ")
    print("Portlar taranıyor...\n")
    for port in range(1, 100):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Açık port: {port}")
            s.close()
        except:
            pass

def header_grabber():
    url = input("URL (https:// dahil): ")
    try:
        response = requests.get(url)
        print("\nHTTP Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except:
        print("Bağlantı hatası!")

def sqli_finder():
    url = input("Test edilecek URL (parametreli): ")
    payloads = ["'", "' OR '1'='1", '" OR "1"="1', "';--"]
    print("SQL Injection taraması başlıyor...\n")
    for payload in payloads:
        test_url = url + payload
        r = requests.get(test_url)
        if "error" in r.text.lower() or "sql" in r.text.lower():
            print(f"[!] Muhtemel SQLi zafiyeti: {test_url}")

def whois_lookup():
    domain = input("Alan adı (örnek: google.com): ")
    try:
        w = whois.whois(domain)
        print("\nWhois Bilgisi:")
        print(w)
    except:
        print("Whois bilgisi alınamadı!")

def main():
    while True:
        os.system("clear")
        print("""
███████╗██╗  ██╗ █████╗ ██████╗ ██████╗  █████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║    ██║
█████╗  ███████║███████║██║  ██║██████╔╝███████║██║ █╗ ██║
██╔══╝  ██╔══██║██╔══██║██║  ██║██╔═══╝ ██╔══██║██║███╗██║
███████╗██║  ██║██║  ██║██████╔╝██║     ██║  ██║╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ 
                SHADOWX by gardaşın
----------------------------------------------------------
[1] Port Scanner
[2] HTTP Header Grabber
[3] SQL Injection Finder
[4] Whois Lookup
[0] Çıkış
""")
        choice = input("Seçimini yap: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            header_grabber()
        elif choice == "3":
            sqli_finder()
        elif choice == "4":
            whois_lookup()
        elif choice == "0":
            print("Görüşürüz gardaş!")
            break
        else:
            print("Geçerli bir seçenek gir!")

        input("\nDevam etmek için Enter'a bas...")

if __name__ == "__main__":
    main()
