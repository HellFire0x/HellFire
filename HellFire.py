from os import system

system('cls')

def Logo():
    Name = """
          ___ ___         .__  .__  ___________.__                
         /   |   \   ____ |  | |  | \_   _____/|__|______   ____  
        /    ~    \_/ __ \|  | |  |  |    __)  |  \_  __ \_/ __ \ 
        \    Y    /\  ___/|  |_|  |__|     \   |  ||  | \/\  ___/ 
         \___|_  /  \___  >____/____/\___  /   |__||__|    \___  >
               \/       \/               \/                    \/ 
       
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

    Cmd = input("        [+]> ")
    if Cmd == "1":
        #Command 1
        print("")


main()