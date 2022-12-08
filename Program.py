from httpx import get, post
from randomuser import RandomUser
from banner import *
import json
from rich.console import Console
from rich.table import Table

def Domain():
    resp = get("https://www.1secmail.com/api/v1/?action=getDomainList").json()
    print(f"""
    [1]. {resp[0]}
    [2]. {resp[1]}
    [3]. {resp[2]}
    [4]. {resp[3]}
    [5]. {resp[4]}
    [6]. {resp[5]}
    [7]. {resp[6]}
    [8]. {resp[7]}
    """)
    choosedom = int(input(selectoption))
    while not choosedom in [1, 2, 3, 4, 5, 6, 7, 8]: print(checkinput); choosedom = int(input(selectoption))
    dom = resp[0] if choosedom == 1 else resp[1] if choosedom == 2 else resp[2] if choosedom == 3 else resp[3] if choosedom == 4 else resp[4] if choosedom == 5 else resp[5] if choosedom == 6 else resp[6] if choosedom == 7 else resp[7]; return dom

def delEmail(username, domain):
    payload = {'action': 'deleteMailbox', 'login': username, 'domain': domain}
    print(f'This {username}@{domain} has been deleted!')
    post('https://www.1secmail.com/mailbox', data=payload)

def RandomEmail():
    h = get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    up = h.json()
    data = up[0]
    print("{green}Email:{reset} %s" % data)
def custom():
    username = input('Enter your username: ')
    domain = Domain(); email = f'{username}@{domain}'
    return username, email, domain
def CekEmail(username, domain):
    resp = get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}').json()
    if len(resp) == 0:
        print(f'\n{empty}\n')
    else:
        for ID in [value for i in resp for key, value in i.items() if key=='id']:
            resp = get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={ID}').json()
            for key, value in resp.items():
                if key == 'from': sender = value
                elif key == 'subject': subject = value
                elif key == 'date': date = value
                elif key == 'textBody': content = value

            print(f'''
{blues}╔══════════════════════════════════════════════════════════════╗{reset}
{blues}|{reset}                       {yellow}☠ 📩 |ɪɴʙᴏx| ㋛{reset}                        {blues}|{reset}
{blues}╚══════════════════════════════════════════════════════════════╝{reset}
{green}_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳{reset}
----> 𝑵𝒆𝒘 𝑴𝒆𝒔𝒔𝒂𝒈𝒆
{cyan}➥{reset}{org}🅵🆁🅾🅼{reset}    : {bold}{sender}{reset}
{cyan}➥{reset}{org}🅸🅳{reset}      : {bold}{ID}{reset}
{cyan}➥{reset}{org}🆃🅾{reset}      : {bold}{username}@{domain}{reset}
{cyan}➥{reset}{org}🅳🅰🆃🅴{reset}    : {bold}{date}{reset}
{cyan}➥{reset}{org}🆂🆄🅱🅹🅴🅲🆃{reset} : {bold}{subject}{reset}
{cyan}➥{reset}{org}🅿🅴🆂🅰🅽{reset}   : {bold}{content.strip()}{reset}
{green}_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳_̳{reset}
''')