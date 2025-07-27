import os, requests, socket
from colorama import Fore, init
init()

def banner():
    os.system("clear")
    print(Fore.MAGENTA + """
______  ___ _____ ___________ 
|___  / / _ \_   _|___  /  _  \
   / / / /_\ \| |    / /| | | |
  / /  |  _  || |   / / | | | |
./ /___| | | || | ./ /__| |/ / 
\_____/\_| |_/\_/ \_____/___/
""" + Fore.CYAN + "     >> USE WISELY <<\n")

def menu():
    print(Fore.YELLOW + """
[1] Cek DNS
[2] Cek IP Public
[3] OSINT Nama (Google Dork)
[4] Cek Lokasi IP
[5] Subdomain Finder
[6] Cek Port Terbuka
[7] Traceroute
[8] Whois Domain
[9] Cari Username di Sosmed
[10] Reverse IP Lookup
[0] Exit
""")

def dns_lookup():
    domain = input("Masukkan domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)
    except:
        print("Gagal mendapatkan IP.")

def cek_ip_public():
    ip = requests.get("https://api.ipify.org").text
    print("IP Publik Anda:", ip)

def osint_nama():
    nama = input("Masukkan nama untuk OSINT: ")
    print("Cek di Google...")
    print(f"https://www.google.com/search?q={nama.replace(' ', '+')}")

def geoip():
    ip = input("Masukkan IP: ")
    r = requests.get(f"http://ip-api.com/json/{ip}").json()
    for k, v in r.items():
        print(f"{k}: {v}")

def subdomain():
    domain = input("Domain target: ")
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}").text
        print(r)
    except:
        print("Gagal mendapatkan subdomain.")

def port_scan():
    host = input("IP target: ")
    for port in [21, 22, 23, 80, 443, 8080]:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"Port {port} terbuka")
            s.close()
        except:
            pass

def traceroute():
    host = input("Masukkan host/domain: ")
    os.system(f"traceroute {host}")

def whois():
    domain = input("Masukkan domain: ")
    os.system(f"whois {domain}")

def username_checker():
    uname = input("Masukkan username: ")
    platforms = ['https://github.com/', 'https://twitter.com/', 'https://instagram.com/', 'https://tiktok.com/@']
    for p in platforms:
        url = p + uname
        r = requests.get(url)
        status = "✅ ADA" if r.status_code == 200 else "❌ TIDAK ADA"
        print(url, "-", status)

def reverse_ip():
    ip = input("Masukkan IP: ")
    r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}").text
    print(r)

def main():
    while True:
        banner()
        menu()
        choice = input("Pilih opsi > ")
        if choice == "1": dns_lookup()
        elif choice == "2": cek_ip_public()
        elif choice == "3": osint_nama()
        elif choice == "4": geoip()
        elif choice == "5": subdomain()
        elif choice == "6": port_scan()
        elif choice == "7": traceroute()
        elif choice == "8": whois()
        elif choice == "9": username_checker()
        elif choice == "10": reverse_ip()
        elif choice == "0":
            print("Keluar dari tools ZATZD...")
            break
        else:
            print("Pilihan tidak valid.")
        input(Fore.CYAN + "\nEnter untuk kembali ke menu...")

main()
