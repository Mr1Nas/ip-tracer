import os 
import colorama
import requests 
import time
import rainbowtext
import platform
plat = platform.uname()
print(f"your system{plat}")
plat0 = platform.uname()[0]
if plat0 == 'Windows':
    os.system("py -m pip install requests")
    os.system("py -m pip install rainbowtext")
    for i in colorama.Fore.GREEN+"Installation completed successfully!":
        print(i,end='',flush=True)
        time.sleep(0.1)
    
else:
    os.system("pip install requests")
    os.system("pip install rainbowtext")
    for i in colorama.Fore.GREEN+"Installation completed successfully!":
        print(i,end='',flush=True)
        time.sleep(0.1)
os.system("cls")
    
while True:
    print(colorama.Fore.YELLOW+"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░   ░░░░░░░░░░░░░░░░           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒   ▒  ▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒  ▒    ▒▒▒▒   ▒▒▒▒▒▒▒▒    ▒▒▒▒   ▒▒▒▒▒  ▒    
    ▓   ▓  ▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓▓  ▓▓▓   ▓▓▓   ▓▓▓
    ▓   ▓  ▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓   ▓▓   ▓▓▓▓▓         ▓▓▓   ▓▓▓
    ▓   ▓   ▓   ▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓   ▓▓▓
    █   █   ████████████████   █████    ██████   █    ████    ███     ████    ███
    █████   █████████████████████████████████████████████████████████████████████
    """)
    print(f"SYSTEM:{plat0}")
    print(colorama.Fore.GREEN+"----------------------------------------------------------------------------------")
    
    for i in colorama.Fore.RED+"The Source created By Mr1Nas\n":
        print(i,end='',flush=True)
        time.sleep(0.1)
    for k in colorama.Fore.RED+"https://github.com/Mr1Nas/ip-tracer\n":
        print(k,end='',flush=True)
        time.sleep(0.01)
    print(colorama.Fore.GREEN+"1_lookup your ip\n")
    print(colorama.Fore.GREEN+"2_lookup other ip or hostname\n")
    type = input("ENTER->")
    type = int(type)
    if type == 1:
        lu = 'http://ip-api.com/#'
        te = requests.get(lu)
        print(te.text)
    else:
        iplc = input("Enter ip or for lookup->  ")
        url = 'http://ip-api.com/'
        ipcol = url + iplc
        col = requests.get(ipcol)
        print(col.text)
   
    print(colorama.Fore.GREEN+"1-Again\n")
    print(colorama.Fore.RED+"2-Exit\n")
    ali = input("->")
    ali = int(ali)
    if ali == 2:
        break
    else:
        os.system("cls")
        os.system("clear")
