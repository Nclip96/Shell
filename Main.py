import time
from datetime import datetime

print("Welcome to CORE OS v1.4")
time.sleep(0.5)
print("Enter command. Use command help for commands list.")

while True:
    command = input(">")
    
    if command == "help":
        print("cat - reads out a file. example: cat example.txt")
        print("convert - checks if a file is encrypted and if so, decrypts it. example: convert example.txt")
        print("penetrate - breaks into servers by IP address. example: penetrate 123.456.7.8")
        print("list - lists files on operating system")
        print("execute - executes a .exe file of your choice. example: execute example.exe")
    
    if command == "list":
        print("LOCKED-1")
        print("LOCKED-2")
        print("LOG-1")
        print("LOCKED-3")
        print("LOCKED-4")
        print("LOCKED-5")
        print("LOCKED-6")
        print("LOCKED-7")
        print("LOCKED-8")
        print("LOCKED-9")
        print("LOCKED-10")
    
    if command == "cat LOG-1":
        print("36,32,60,76,45,99,80,48,83,32,32,62,41,17,80,48,39,72,54,36,35,123,60,61,83,32,36,58,41,14,53,55,55,45,33,77")
        print("FILE MAY BE ENCRYPTED. USE CONVERT COMMAND IF POSSIBLE")
        
    if command == "cat LOCKED-1":
        LOCKED1pass = input("ENTER KEY:")
        if LOCKED1pass == "46273":
            print("Well, you must have gotten my last message. this is LOG-2, I'm starting to forget the outside. I can't remember last time I saw someone... LOCKED-2 key is the data in hidden.txt. You won't see it, but its there.")
    
    if command == "cat LOCKED-2":
        LOCKED1pass = input("ENTER KEY:")
        if LOCKED1pass == "354768":
            print("FOR THE CODE FOR LOCKED-3, DIVIDE BY 2: 1127624") # code is 563812
 
    if command == "cat LOCKED-3":
        LOCKED1pass = input("ENTER KEY:")
        if LOCKED1pass == "563812":
            print("There is no more you could get on this server. Try getting onto the IP 410.904.9.5")
    
    if command == "cat LOCKED-4":
        print("LOCKED")
    
    if command == "cat LOCKED-5":
        print("LOCKED")
    
    if command == "cat LOCKED-6":
        print("LOCKED")
    
    if command == "cat LOCKED-7":
        print("LOCKED")
    
    if command == "cat LOCKED-8":
        print("LOCKED")
    
    if command == "cat LOCKED-9":
        print("LOCKED")
        
    if command == "cat LOCKED-10":
        print("LOCKED")

    if command == "convert LOG-1":
        print("Why am I here? It should have ended!")
        print("To anyone who finds this, to access LOCKED-1, enter the code 46273.")
    
    if command == "cat hidden.txt":
        print("Good, you found secret file-1. I need to hide these files like this so I THEY can't find them. If you made it this far, you certainly aren't one of them. the password for LOCKED-2 is 354768")

    if command == "penetrate 410.904.9.5":
        print("ACCESS GRANTED! To use commands on 410.904.9.5, use this command for more info about server commands: data.help.IP{410.904.9.5}")
    
    if command == "data.help.IP{410.904.9.5}":
        print("data.cat.IP{410.904.9.5} - reads out a file from a server. example: data.cat.IP{410.904.9.5} example.txt")
        print("data.list.IP{410.904.9.5} - lists files on server")
    
    if command == "data.list.IP{410.904.9.5}":
        print("info.txt")
        print("data.txt")
        print("CLASSIFIED.txt")
        print("server.jar")

    if command == "data.cat.IP{410.904.9.5} info.txt":
        print("WELCOME TO SERVER 410.904.9.5")
        print("MCP COMMANDS:")
        print("MCP.KILL()")
        print("MCP.WRITE('')")
        print("MCP.CONNECT('')")
        print("MCP.SELFDESTRUCT()")
        print("end of file.")

    if command == "data.cat.IP{410.904.9.5} data.txt":
        print("SYSTEM DATA:")
        print()
        print("A WHILE AGO - POSSIBLE BREACH")
        print('NOW - BREACH ERROR RESOLVED! DESCRIPTION: DETECTION SYSTEM FAILURE. PACKAGE DOWNLOADED FROM "BREACH" MCP.PATCH.572.exe. FILE STATUS: SAFE')
        time.sleep(1)
        print("NOW - INCOMING PACKAGE: message.txt. FILE STATUS: SAFE")
        print()
        print()
        print("end of file.")

    if command == "data.cat.IP{410.904.9.5} CLASSIFIED.txt":
        print("Nice try, human.")
        print()
        time.sleep(0.5)
        print("Server switched to defense mode. All computers connected will be tracked.")
        ServerSafe = 0
        print("Message.txt has been updated: Use the commmand data.escape.IP{410.904.9.5}!")

    if command == "data.cat.IP{410.904.9.5} server.jar":
        print("FILE CAN NOT BE VIEWED IN TEXT BASED TERMINAL")

    if command == "data.escape.IP{410.904.9.5}":
        print("Connection terminated. If you were being tracked, we do not recommend you reenter the server.")
        print("If they got your location, which is highly likely, change your servers location with the command execute exploit-42216.exe")
    
    if command == "execute exploit-42216.exe":
        print("SERVER IP CHANGED! 810.127.2.4 ---> 127.513.6.8")
        time.sleep(1)
        print("File downloaded. Name: message.txt. Access key: 416283.")
    
    if command == "cat message.txt":
        message1key = input("Acess Key:")
        if message1key == "416283":
            print("Hello again, user. I assume you got the message I sent, or you wouldn't be reading this. I must ask, did you run the exploit yet?")
            print("    If not, do it now. The command was execute exploit-42216.exe. Just take care of that so we don't get CyberBreached")
            print("Now, I would like to ask you your name. I never actually got that. So, User. What's your name, anyway?")
            name = input("My name is ")
            time.sleep(1)
            print(f"Huh. You seem like a {name}. Anyway, {name}, lets get to business. I created a file called MCP.zip. It will allow us to sneak any payload into any server.")
            print("The problem is, I cant send payloads. Thats where you come in. You need to load Trojan.exe onto MCP.zip. if you can do that, we should be able to target")
            print("a trojan attack onto any server, we will be attacking MCP.MAIN at the IP 426.219.7.9.")
            time.sleep(5)
            print("Launching trojan_setup.exe")
            trojan = input("enter trojan file name:")
            
            if not (trojan == "MCP.zip" or trojan == "mcp.zip"):
                print("INCORRECT FILE! YOU HAVE 1 TRY LEFT!")
            else:
                print("Accepted.")
                destination = input("enter trojan destination:")
                if not destination == "426.219.7.9":
                    print("INCORRECT DESTINATION!")
                else:
                    print("Accepted.")
                    print("LAUNCHING DESTRUCTION_VISUALIZER.exe")
                    time.sleep(3)
                    current_time = datetime.now()
                    print(f"{current_time} - trojan hits server.")
                    time.sleep(1)
                    current_time = datetime.now()
                    print(f"{current_time} - trojan has been noticed.")
                    time.sleep(1.5)
                    current_time = datetime.now()
                    print(f"{current_time} - AI agents have been deployed to inspect trojan.")
                    time.sleep(1)
                    current_time = datetime.now()
                    print(f"{current_time} - AI agents are currently inspecting.")
                    time.sleep(3)
                    current_time = datetime.now()
                    print(f"{current_time} - AI agents found no issues.")
                    time.sleep(1)
                    current_time = datetime.now()
                    print(f"{current_time} - trojan progressing deeper into server.")
                    time.sleep(1)
                    current_time = datetime.now()
                    print(f"{current_time} - trojan.untility.js has found password.txt. password.txt = 96035")
                    time.sleep(1)
                    current_time = datetime.now()
                    finalpassword = input(f"{current_time} - Gate requires password:")
                    
                    if finalpassword == "96035":
                        time.sleep(1)
                        current_time = datetime.now()
                        print(f"{current_time} - trojan has crossed the gate. payload deploying in 5 seconds.")
                        time.sleep(0.5)
                        print("5...")
                        time.sleep(1)
                        print("4...")
                        time.sleep(1)
                        print("3...")
                        time.sleep(1)
                        print("2...")
                        time.sleep(1)
                        print("1...")
                        time.sleep(1)
                        current_time = datetime.now()
                        print(f"{current_time} - SERVER OFFLINE. MISSION SUCCESSFUL!")
                    else:
                        print("INCORRECT! PAYLOAD DESTROYED. MISSION FAILURE!")
