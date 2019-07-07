#!/usr/bin/python3
# Feel free to leave any feedback on my github: github.com/ak-wa
# Tests for tor connection ability through localhost:9150 (Tor Socks5 Port)
# Troubleshooting:
# 1. Make sure to have tor service installed and running(On linux: apt-get install tor && tor | On windows, just start the tor browser)
# 2. On importerror try to install the modules manually
# 3. Make sure you are running Python 3.x / Tested on Python 3.7
try:
    import socket,socks
    from sys import stdout,exit
    from requests import get
    from os import system
except:
    import_in = input("[-] One or more modules are missing, should I try installing with pip? y/n: ")
    if import_in == 'y':
        system('pip install socket')
        system('pip install requests')
        system('pip install socks')
        import socket,socks
        from sys import stdout,exit
        from requests import get
        from os import system
    else:
        exit()
try:
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1', 9150)
    socket.socket = socks.socksocket
    tor_check = get("https://check.torproject.org/?lang=en").text
    if "Congratulations" in tor_check:
        stdout.write("[+] Routing through tor succeeded\n")
        ip_check = get("https://api.ipify.org/")
        stdout.write("[+] Remote IP: %s" % (ip_check.text))
    else:
        stdout.write("[!] Routing through Tor failed\n")
except:
    stdout.write("[!] Routing through Tor failed\n")
