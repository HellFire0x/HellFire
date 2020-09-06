import json
import urllib.request
from os import system

Version = '1.1'
Developer = 'HellFire'
Helper = 'Dean Richards'

from pip._vendor.distlib.compat import raw_input

system ( 'cls' )


def datas ( ) -> object :
    data = urllib.request.urlopen (
        "https://panel.9hits.com/api/profileGet?key=b235add0de15a138ed4b0f618b10370e" ).read ( )
    output = json.loads ( data )
    return print ( output [ 'status' ] )


def log ( logger ) -> object :
    return print ( "        [\033[92m-\033[0m] - " + logger )


def givespace ( ) -> object :
    """

    :rtype: object
    """
    return print ( "\n\n" )


def logo ( ) -> object :
    Name = (
        "\u001B[93m\n          ___ ___         .__  .__  ___________.__                \n         /   |   \\   ____ | "
        " | |  | \\_   _____/|__|______   ____  \n        /    ~    \\_/ __ \\|  | |  |  |    __)  |  \\_  __ \\_/ __ "
        "\\ \n        \\    Y    /\\  ___/|  |_|  |__|     \\   |  ||  | \\/\\  ___/ \n         \\___|_  /  \\___  "
        ">____/____/\\___  /   |__||__|    \\___  >\n               \\/       \\/               \\/                   "
        " \\/ \n \u001B[0m      \n                          9 H I T S   E X P L O I T\n        "
        "___________________________________________________________\n                                Version:\u001B["
        "92m {0} \u001B[0m".format (
            Version ))
    print ( f"\u001B[6m{Name}\u001B[0m" )
    print ( f"                              Made By:\u001B[91m {Developer}  \u001B[0m" )
    print ( f"                            Helper:\u001B[34m {Helper} \u001B[0m" )


def main ( ) :
    logo ( )
    for x in [
        "        1) 9Hits Data" ,
        "        2) API Finder" ,
        "        3) 9Hits Links\n" ] :
        print ( x )

    Cmd = raw_input ( "        [\033[92m+\033[0m]> " )
    if Cmd == "1" :
        datas ( )
    if Cmd == "2" :
        # Command 2
        print ( "" )
    if Cmd == "3" :
        givespace ( )
        log ( "https://ftp.9hits.com/" )
        log ( "https://f.9hits.com/" )
        log ( "https://forum.9hits.com/" )
        log ( "https://mail.9hits.com/" )
        log ( "https://www.9hits.com/" )


main ( )
