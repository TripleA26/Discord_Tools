from colorama import Fore, init
from pytube.cli import on_progress
from pytube import YouTube
import colorama
from discord_webhook import DiscordWebhook, DiscordEmbed
from dhooks import Webhook
from pynput.keyboard import Key,Controller
from random import randint
from requests import get, post
import time
import string
import random
import requests
init(convert=True)
keyboard = Controller()
text = """ _______ _____  _____ _____  _      ______          
|__   __|  __ \|_   _|  __ \| |    |  ____|   /\    
   | |  | |__) | | | | |__) | |    | |__     /  \   
   | |  |  _  /  | | |  ___/| |    |  __|   / /\ \  
   | |  | | \ \ _| |_| |    | |____| |____ / ____ \ 
   |_|  |_|  \_\_____|_|    |______|______/_/    \_\
   """
bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET', 'BLUE', 'GREEN', 'RED']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))
time.sleep(1)
print("\nTriple_A Discord Tools :)\n")
time.sleep(2)
def gen(x, y):
    print(Fore.LIGHTYELLOW_EX + "")
    num = int(input('\nInput How Many Codes to Generate: '))

    with open(x, "w", encoding='utf-8') as file:
        print(Fore.WHITE + "[" + Fore.YELLOW + "?" + Fore.WHITE + "] " + Fore.LIGHTBLUE_EX + "Your nitro codes are being generated, be patient if you entered the high number!\n")

        start = time.time()

        for i in range(num):
                    code = "".join(random.choices(
                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k = y
                    ))
                    print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "] " + Fore.LIGHTGREEN_EX + f"https://discord.gift/{code}\n")
                    file.write(f"https://discord.gift/{code}\n")
        print(f"Generated {num} codes | Time taken: {time.time() - start}\n")
        print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "] " + Fore.LIGHTBLUE_EX + f"All the codes has been saved in a txt with the name: {x}" + Fore.YELLOW)
def check(x):
    with open(x) as file:
                    for line in file.readlines():
                        nitro = line.strip("\n")

                        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                        r = requests.get(url)

                        if r.status_code == 200:
                            print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]"+ Fore.RED + f" Valid | {nitro}\n The Programm has stopped because it found a valid nitro, GG :D")
                            break
                        elif r.status_code == 429:
                            print(Fore.WHITE + "[" + Fore.LIGHTYELLOW_EX + "?" + Fore.WHITE + "]" + Fore.LIGHTYELLOW_EX + "Your being Rate limited!!")
                        else:
                            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + "-" + Fore.WHITE + "]"+ Fore.RED + f" Invalid | {nitro} ")
                            
                    print(Fore.WHITE + "\n[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.LIGHTMAGENTA_EX + "All The codes has been checked :)")

    
print(Fore.LIGHTRED_EX + "")

sk = int(input("""What do you want to do?
        1 = Send message to any webhook
        2 = Nitro
        3 = Token
        4 = Ping spam in a MD
        5 = Yt video downloader (Not Disc tool but funny :D)
What do u select?: """))


if sk == 1:
    print(Fore.LIGHTYELLOW_EX + "")
    sk5 = input("Do u want to send a embed? y/n:  ")
    if sk5 == ("n"):
        sk6 = input("Do u want to spam that message? y/n: ")
        if sk6 == ("n"):
            hook = Webhook(input("Webhook_ulr:  "))
            cont = input("What do u want to send to that webhook?:  ")
            hook.send(cont)
            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.GREEN + f" Sended --> {cont}")
            input('Press Enter For Exit...')
        else:
            ñ = 1
            hook = Webhook(input("Webhook_ulr:  "))
            cont = input("What do u want to send to that webhook?:  ")
            while True:
                hook.send(cont)
                print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.GREEN + f" Sended --> {cont} | Message Nº{ñ}")
                ñ += 1
    if sk5 == ("y"):
        print(Fore.LIGHTYELLOW_EX + "")
        colors = [ "1ABC9C", 
                   "11806A", 
                   "2ECC71", 
                   "1F8B4C", 
                   "23272A", 
                   "FFFFFF", 
                   "ED4245", 
                   "FEE75C", 
                   "57F287", 
                   "23272A", 
                   "2C2F33", 
                   "99AAB5", 
                   "5865F2", 
                   "FFFF00", 
                   "2C3E50", 
                   "34495E", 
                   "BCC0C0",
                   "7F8C8D",
                   "979C9F",
                   "95A5A6",
                   "992D22",
                   "E74C3C",
                   "A84300",
                   "E67E22",
                   "11806A",
                   "2ECC71",
                   "1F8B4C",
                   "3498DB",
                   "206694",
                   "9B59B6",
                   "71368A",
                   "E91E63",
                   "AD1457",
                   "F1C40F",
                   "C27C0E",
                   "E67E22",
                   "A84300"]
        random_color = random.choice(colors)
        
        webhook = DiscordWebhook(url = input("Webhook_ulr:  "))
        tit = input("Whats the Title of that webhook?: ")
        dsc = input("Whats the message that u wanna send?: ")
        cl = int(input("Do u want a:\n1 = random color\n2 = specific color\nWhat do u select?:  "))
        if cl == 1:
            embed = DiscordEmbed(title=(tit), description=(dsc), color = random_color)
            img = input("Wanna set an image? y/n:  ")
            if img == ("y"):
                rl = input("Image url: ")
                embed.set_image(url = rl)
            webhook.add_embed(embed)
            response = webhook.execute()
            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.GREEN + "The embed has been sended")
            input('Press Enter For Exit...')
            
        if cl == 2:
            cll = input("What color do u want? example(3498DB9):  ")
            if colors.__contains__(cll):
                embed = DiscordEmbed(title=(tit), description=(dsc), color = cll)
                img = input("Wanna set an image? y/n:  ")
                if img == ("y"):
                    rl = input("Image url: ")
                    embed.set_image(url = rl)
                webhook.add_embed(embed)
                response = webhook.execute()
                print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.GREEN + "The embed has been sended")
                input('Press Enter For Exit...')
            else:
                print(Fore.WHITE + "["+ Fore.LIGHTRED_EX + "!" + Fore.WHITE + "]" + Fore.LIGHTRED_EX + "Wrong Color, Please input a correct color")
                input('Press Enter For Exit...')
if sk == 2:
        sk2 = int(input("""\nWhat type of nitro wanna select?:
        1 = Nitro Generator (No check, just gen)
        2 = Nitro Checker
        3 = Nitro Generator and Checker
        4 = Send Nitro codes uncheckeds to a webhook
        What do u select?:  """))
        if sk2 == 2:
            print(Fore. RED + "Remember that in the same folder where you put this you have to have the codes in a txt with the name:  Nitro_Codes.txt")
            check("Nitro_Codes.txt")
            print(Fore.LIGHTYELLOW_EX + "")
            input("Press Enter for exit...")
            exit()
        sk8 = input("The codes will be for nitro classic or nitro boost? c/b: ")
        if sk8 == ("c"):

            if sk2 == 1:
                gen("Nitro_Codes.txt", 24)
                print(Fore.LIGHTYELLOW_EX + "")
                input("Press Enter For exit...")
                            
                            
            if sk2 == 3:
                gen("Nitro_Codes.txt", 24)
                print(Fore.LIGHTCYAN_EX + "")
                input('Press Enter For start checking :D ')
                check("Nitro_Codes.txt")
                print(Fore.LIGHTYELLOW_EX + "")
                input("Press Enter For exit...")
                
            if sk2 == 4:
                hook = Webhook(input("Webhook_ulr:"))
                gen("Nitro_Codes(Webhook).txt", 24)

                with open("Nitro_Codes(Webhook).txt") as file:
                    start = time.time()
                    for line in file.readlines():
                        nitro = line.strip("\n")
                        hook.send(nitro)
                        print(Fore.LIGHTGREEN_EX + f"[SENDED]  {nitro}\n")
                        time.sleep(2)
                    input('Press Enter For Exit...')
        else:
            if sk2 == 1:
                gen("Nitro_Codes.txt", 24)
                print(Fore.LIGHTYELLOW_EX + "")
                input("Press Enter For Exit...")
                            
                            
            if sk2 == 3:
                gen("Nitro_Codes.txt", 24)
                print(Fore.LIGHTMAGENTA_EX + "")
                input('Press Enter For start checking :D ')
                check("Nitro_Codes.txt")
                print(Fore.LIGHTCYAN_EX + "")
                input("Press Enter For exit...")
                
            if sk2 == 4:
                hook = Webhook(input("Webhook_ulr:"))
                gen("Nitro_Codes(Webhook).txt", 24)

                with open("Nitro_Codes(Webhook).txt") as file:
                    start = time.time()
                    for line in file.readlines():
                        nitro = line.strip("\n")
                        hook.send(nitro)
                        print(Fore.LIGHTGREEN_EX + f"[SENDED]  {nitro}\n")
                        time.sleep(2)
                    input('Press Enter For Exit...')

    
if sk == 3:
    sk3 = int(input("""What do u wan to do?:
    1 = Token Gen
    2 = Token Checker
    3 = Token Generator and Checker
    4 = Send unchecked tokens To a webhook
    What do u select?:  """))
    
    
    if sk3 == 1:
        print(Fore.LIGHTYELLOW_EX + "")
        num1 = int(input("How many tokens to gen?:  "))
        with open("tokens.txt", "w", encoding='utf-8') as file:
            print(Fore.WHITE + "[" + Fore.LIGHTYELLOW_EX + "?" + Fore.WHITE + "] " + Fore.LIGHTBLUE_EX + "Your discord tokens are being generated, be patient if you entered the high number!")
            start = time.time()
        
            for i in range(num1):
                fst = "".join(random.choice(string.ascii_letters + string.digits) for i in range(24))
                scn = "".join(random.choice(string.ascii_letters + string.digits) for i in range(6))
                trh = "".join(random.choice(string.ascii_letters + string.digits) for i in range(27))
                fth = fst + "." + scn + "." + trh
                print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "] " + Fore.LIGHTGREEN_EX + f"{fth}\n")
                file.write(f"{fth}\n")
            print(Fore.LIGHTGREEN_EX + f"Generated {num1} tokens | Time taken: {time.time() - start} and saved in a file with the name: tokens.txt\n")
            print(Fore.LIGHTYELLOW_EX + "")
            input("Pres Enter For Exit...")
            
    if sk3 == 2:
        print(Fore.LIGHTRED_EX + "REMEMBER TO HAVE A FILE WITH THE NAME: tokens.txt")
        time.sleep(2)
        def variant1(token):
            response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
            return True if response.status_code == 200 else False


        def variant2(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
                return False
            else:
                return True

        def variant2_Status(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
            if response.status_code == 401:
                return 'Invalid'
            elif "You need to verify your account in order to perform this action." in str(response.content):
                return 'Phone Lock'
            else:
                return 'Valid'

        if __name__ == "__main__":
            try:
                checked = []
                with open('tokens.txt', 'r') as tokens:
                    for token in tokens.read().split('\n'):
                        if len(token) > 15 and token not in checked and variant2(token) == True:
                            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f'Token: {token} is Valid')
                            checked.append(token)
                        else:
                            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + "-" + Fore.WHITE + "] " + Fore.LIGHTRED_EX + f'Token: {token} is Invalid')
                if len(checked) > 0:
                    save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
                    if save == 'y':
                        name = randint(100000000, 9999999999)
                        with open(f'{name}.txt', 'w') as saveFile:
                            saveFile.write('\n'.join(checked))
                        print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]  " f'Tokens Save To {name}.txt File!')
            except:
                print(Fore.RED + "")
                input('Can`t Open "tokens.txt" File!')
        print(Fore.LIGHTGREEN_EX + "\nAll the codes has been checked")
        print(Fore.LIGHTYELLOW_EX + "")
        input("Pres Enter For Exit...")
                
                
    if sk3 == 3:
        print(Fore.LIGHTYELLOW_EX + "")
        num1 = int(input("How many tokens to gen?:  "))
        with open("tokens.txt", "w", encoding='utf-8') as file:
            print(Fore.WHITE + "[" + Fore.YELLOW + "?" + Fore.WHITE + "] " + Fore.LIGHTBLUE_EX + "Your discord tokens are being generated, be patient if you entered the high number!")
            start = time.time()
        
            for i in range(num1):
                fst = "".join(random.choice(string.ascii_letters + string.digits) for i in range(24))
                scn = "".join(random.choice(string.ascii_letters + string.digits) for i in range(6))
                trh = "".join(random.choice(string.ascii_letters + string.digits) for i in range(27))
                fth = fst + "." + scn + "." + trh
                print(Fore.GREEN + f"{fth}\n")
                file.write(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "] " + Fore.LIGHTGREEN_EX + f"{fth}\n")
            print(Fore.LIGHTGREEN_EX + f"Generated {num1} tokens | Time taken: {time.time() - start}\n")
        def variant1(token):
            response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
            return True if response.status_code == 200 else False

        def variant2(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
                return False
            else:
                return True

        def variant2_Status(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
            if response.status_code == 401:
                return 'Invalid'
            elif "You need to verify your account in order to perform this action." in str(response.content):
                return 'Phone Lock'
            else:
                return 'Valid'

        if __name__ == "__main__":
            try:
                checked = []
                with open('tokens.txt', 'r') as tokens:
                    for token in tokens.read().split('\n'):
                        if len(token) > 15 and token not in checked and variant2(token) == True:
                            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "] " + Fore.LIGHTGREEN_EX + f'Token: {token} is Valid')
                            checked.append(token)
                        else:
                            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + "-" + Fore.WHITE + "] " + Fore.LIGHTRED_EX + f'Token: {token} is Invalid')
                if len(checked) > 0:
                    save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
                    if save == 'y':
                        name = randint(100000000, 9999999999)
                        with open(f'{name}.txt', 'w') as saveFile:
                            saveFile.write('\n'.join(checked))
                        print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]  " f'Tokens Save To {name}.txt File!')
            except:
                input('Can`t Open "tokens.txt" File!')
        print(Fore.LIGHTGREEN_EX + "\nAll the codes has been checked")
        print(Fore.LIGHTYELLOW_EX + "")
        input("Pres Enter For Exit...")
    
    if sk3 == 4:
        print(Fore.LIGHTYELLOW_EX + "")
        hook = Webhook(input("Webhook_ulr:"))
        print(Fore.LIGHTYELLOW_EX + "")
        num = int(input("How many codes to send to the webhook?: "))
        for i in range(num):
            fst = "".join(random.choice(string.ascii_letters + string.digits) for i in range(24))
            scn = "".join(random.choice(string.ascii_letters + string.digits) for i in range(6))
            trh = "".join(random.choice(string.ascii_letters + string.digits) for i in range(27))
            token = fst + "." + scn + "." + trh
            hook.send(f"`{token}`")
            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]  " + Fore.LIGHTGREEN_EX + f" Sended -> {token}")
            time.sleep(2)
            
        
                
if sk == 4:
        wth = int(input("Your are gonna spam something:\n1 = Spam something with slowmode (u can put the seconds)\n2 = Spam someone fast\nWhat do you select?: "))
        if wth == 1:
            print(Fore.LIGHTYELLOW_EX + "")
            mss = input("What u wanna send to that channel?")
            tm = int(input("how many seconds is the slowmode?(number of seconds):  "))
            while True:
                keyboard.type(mss)
                for i in range(2):
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                
                time.sleep(tm)
        
        if wth == 2:
            print(Fore.LIGHTYELLOW_EX + "")
            mss = input("What u wanna send to that channel?")
            while True:
                keyboard.type(mss)
                for i in range(2):
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                time.sleep(0.7)

if sk == 5:
    print(Fore.LIGHTYELLOW_EX + "")
    url = input("Input the youtube link: ")
    yt = YouTube(url, on_progress_callback=on_progress)

    gotb=yt.streams.filter(progressive=True,file_extension='mp4').first()


    print('Downloading...: %s' % gotb.default_filename)
    gotb.download()

    print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]  " "\nDownload Completed!!")
    print(Fore.LIGHTYELLOW_EX + "")
    input("Press Enter for exit...")