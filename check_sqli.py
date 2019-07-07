import requests
url_list = []
not_found_counter = 0
found_counter = 0

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {'User-Agent': user_agent}

def check_sqli(target_list):
    global not_found_counter
    global found_counter
    with open(target_list,"r") as urls:
        for url in urls:
            lines = urls.readlines()
            for line in lines:
                if '?' in line:
                    url_list.append(line.rstrip())
                else:
                    pass
    print("[+] Testing URL parameters on %d targets" % (len(list(set(url_list)))))   
    for url in list(set(url_list)):
        try:
            s = requests.get(url+"'",timeout=4,headers=headers)
            if 'SQL' in s.text or 'sql' in s.text or 'syntax' in s.text:
                print("[+] Possible vulnerability found on: \n %s" % url)
                found_counter += 1
            else:
                not_found_counter += 1
        except:
            pass
    print("[ - ] Checked %d urls" % (int(not_found_counter)+int(found_counter)))
        
