import sys,requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {'User-Agent': user_agent}

def check_robots(target):
    sys.stdout.write("[+] Checking for a robots.txt\n")
    try:
        req = requests.get(target+"/robots.txt",headers=headers,timeout=4)
        html = req.text
        if req.status_code != 200:
            sys.stdout.write("[+] Robots.txt non-existent or forbidden")
        else:
            for line in html.split("\n"):
                if line.startswith("Disallow: "):
                    sys.stdout.write(line.split(":")[1]+"\n")
    except requests.exceptions.Timeout:
        print("[-] Timeout to %s/robots.txt" % target)
    except:
        print("[-] Could not receive %s/robots.txt" % target)
