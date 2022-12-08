from Program import *
from banner import *
from os import remove
from re import findall
import os,sys
os.system("clear")

def main():
    print(hu)
    put = input('                   Choice: ')

    if put=="1":
       RandomEmail()
    elif put=="2":
       username, domain, email = custom(); print(f'Your Email: {username}@{email}'); open('AllEmail.txt', 'a').write(f'{email}\n')
    elif put=="3":
       CekEmail(input('Your Username: '),input('Yuor Domain: '))
    elif put=="4":
       manu = int(input(selectoption))
       while not manu in [1, 2]: print(checkinput); manu = int(input(selectoption))
       if manu == 1: delEmail(input('Your username: '), input('Your domain: '))
       else:
           for username, domain in findall(r'(\w+)@(\w+.*)', open('AllEmail.txt').read().strip()): delEmail(username, domain)
           remove('AllEmail.txt'); print(f'\n{remtxt}\n')
    elif put=="5":
       os.system("exit")
if __name__=="__main__":
    print(logo)
    main()