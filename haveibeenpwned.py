import requests

def mail_check(mail):
    ans = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+str(mail)+"?includeUnverified=true").json()
    print("[+] Found %s Leaks"% len(ans))
    for leak in ans:
        print("[+] Leak name:", leak["Name"])
        print("    Information leaked:")
        for info in leak["DataClasses"]:
            print("     %s"%info)
        print("  => Breach Date", leak["BreachDate"])
        
mail_check("123@gmail.com")
