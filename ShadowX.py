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
        elif choice == "0":
            print("Görüşürüz gardaş!")
            break
        else:
            print("Geçerli bir seçenek gir!")

        input("\nDevam etmek için Enter'a bas...")
