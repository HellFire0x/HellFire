from os import system
import json, urllib.request

system('cls')

def datas():
    data = urllib.request.urlopen("https://panel.9hits.com/api/profileGet?key=b235add0de15a138ed4b0f618b10370e").read()
    output = json.loads(data)
    print(output["status"])

def log(logger):
    print("        [\033[92m-\033[0m] - " + logger)

def GiveSpace():
    print("\n\n")

def Logo():
    Name = """\033[93m
          ___ ___         .__  .__  ___________.__                
         /   |   \   ____ |  | |  | \_   _____/|__|______   ____  
        /    ~    \_/ __ \|  | |  |  |    __)  |  \_  __ \_/ __ \ 
        \    Y    /\  ___/|  |_|  |__|     \   |  ||  | \/\  ___/ 
         \___|_  /  \___  >____/____/\___  /   |__||__|    \___  >
               \/       \/               \/                    \/ 
 \033[0m      
                          9 H I T S   E X P L O I T
        ___________________________________________________________
                                Version:\033[92m 1.0 \033[0m"""
    print("\033[6m" + Name + "\033[0m")
    print("                              Made By:\033[91m HellFire \033[0m")
    print("                            Helper:\033[34m Dean Richards \033[0m")

def main():
    Logo()
    Command = [
    "        1) 9Hits Data",
    "        2) API Finder",
    "        3) 9Hits Links",
    ""]

    for x in Command:
        print(x)

    Cmd = raw_input("        [\033[92m+\033[0m]> ")
    if Cmd == "1":
        datas()
    if Cmd == "2":
        #Command 2
        print("")
    if Cmd == "3":
        GiveSpace()
        log("https://ftp.9hits.com/")
        log("https://f.9hits.com/")
        log("https://forum.9hits.com/")
        log("https://mail.9hits.com/")
        log("https://www.9hits.com/")


main()