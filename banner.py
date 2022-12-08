from colored import attr, fg
from pystyle import Center, Colors, Colorate
#waena

#! Colored code
yellow = fg("yellow")
white = fg("white")
blue = fg(20)
blues = fg(27)
cyan = fg('cyan')
green = fg(46)
r124 = fg(124)
red = fg('red')
purple = fg("purple_1a")
grey = fg("grey_27")
org = fg('orange_red_1')
bold = attr("bold")
reset = attr("reset")

#choice
checkinput = f'Check your input!'
selectoption = f'{bold}Please select your option{reset}: '
empty = "Your Mailbox is empty!"
#banner
br = ("""

█▀▀ █▀▄▀█ ▄▀█ █ █░░
██▄ █░▀░█ █▀█ █ █▄▄

█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
by - Acbar _+
""")
bann = (Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(br), True))
logo = f'''
{bann}
'''
menu = ("""
[1]> Generator Email
[2]> Custume Email
[3]> Cek Inbox [Email]
[4]> Delete Email
[5]> Exit
""")
tae = (Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(menu), True))
hu = f'''
{tae}
'''

put2 = 'Your Username:'
tae2 = (Colorate.Diagonal(Colors.blue_to_red, Center.XCenter(put2), True))
kar = f'''
{tae2}
'''
put2 = 'Your Domain:'
tae3 = (Colorate.Diagonal(Colors.blue_to_red, (put2), True))
kar1 = f'''
{tae3}
'''