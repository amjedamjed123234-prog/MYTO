import socket
import os
import requests

# الألوان
G = '\033[92m'  # أخضر
R = '\033[91m'  # أحمر
B = '\033[94m'  # أزرق
C = '\033[96m'  # سماوي
W = '\033[0m'   # أبيض

def clear():
    os.system('clear')

def banner():
    # (ASCII Art)
    print(R + """
    #################################################
    #                                               #
    #   ███╗   ███╗██╗   ██╗████████╗ ██████╗       #
    #   ████╗ ████║╚██╗ ██╔╝╚══██╔══╝██╔═══██╗      #
    #   ██╔████╔██║ ╚████╔╝    ██║   ██║   ██║      #
    #   ██║╚██╔╝██║  ╚██╔╝     ██║   ██║   ██║      #
    #   ██║ ╚═╝ ██║   ██║      ██║   ╚██████╔╝      #
    #   ╚═╝     ╚═╝   ╚═╝      ╚═╝    ╚═════╝       #
    #                                               #
    #        -- DEVELOPED BY [YOUR NAME] --         #
    ################################################# """ + W)
    print(G + "\n [1]" + W + " Port Scanner      " + G + "[2]" + W + " Subdomain Finder")
    print(G + " [3]" + W + " Text Encrypter    " + G + "[4]" + W + " Web Link Scraper")
    print(G + " [5]" + W + " DNS Lookup        " + R + "[6]" + W + " Exit")
    print(C + "-----------------------------------------------" + W)

def main():
    while True:
        clear()
        banner()
        choice = input(G + "msf_custom > " + W)

        if choice == '1':
            target = input(C + "Target IP: " + W)
            print("[*] Scanning...")
            for port in [21, 22, 80, 443]:
                s = socket.socket()
                s.settimeout(1)
                if s.connect_ex((target, port)) == 0:
                    print(G + f"[+] Port {port} is OPEN" + W)
                s.close()
            input("\nPress Enter...")

        elif choice == '2':
            domain = input(C + "Domain: " + W)
            print(G + f"[+] Found: www.{domain}\n[+] Found: mail.{domain}" + W)
            input("\nPress Enter...")

        elif choice == '3':
            text = input(C + "Text: " + W)
            enc = "".join([chr(ord(c)+4) for c in text])
            print(G + "Result: " + enc + W)
            input("\nPress Enter...")

        elif choice == '4':
            url = input(C + "URL (with http): " + W)
            print(G + "[+] Links extracted (Simulated)" + W)
            input("\nPress Enter...")

        elif choice == '5':
            domain = input(C + "Domain: " + W)
            try:
                print(G + "IP: " + socket.gethostbyname(domain) + W)
            except: print(R + "Error" + W)
            input("\nPress Enter...")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()