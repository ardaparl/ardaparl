import os
import sys

def install_ufonet():
    print("[*] UFONet kurulumu başlatılıyor...")

    # UFONet'i klonla
    os.system("git clone https://github.com/epsylon/ufonet.git")

    # UFONet dizinine gir
    os.chdir("ufonet")

    # Gereksinim dosyasını yükle
    os.system("pip install -r requirements.txt")

    print("[+] UFONet kurulumu tamamlandı.")

def ddos_attack():
    print("[!] UFONet DDoS Saldırısı başlatılıyor...")
    os.system("python3 /data/data/com.termux/files/home/ardaparl/ufonet/ufonet.py")

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
[5] DDoS (UFONet)
[6] UFONet Kurulumunu Yap
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
        elif choice == "5":
            ddos_attack()
        elif choice == "6":
            install_ufonet()
        elif choice == "0":
            print("Görüşürüz gardaş!")
            break
        else:
            print("Geçerli bir seçenek gir!")

        input("\nDevam etmek için Enter'a bas...")

# Ana fonksiyonu başlat
if __name__ == "__main__":
    main()
