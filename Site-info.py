# site-info.py

import requests
from bs4 import BeautifulSoup

def banner():
    print("="*40)
    print("  Site Bilgisi Toplama Aracı")
    print("="*40)

def get_target():
    url = input("Site adresini yaz (https:// ile): ")
    return url

def site_info(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"\n[+] Başlık: {soup.title.string}")
        print(f"[+] Status Code: {response.status_code}")
    except Exception as e:
        print(f"[!] Hata: {e}")

banner()
url = get_target()
site_info(url)
