import requests
from telethon import TelegramClient, events, sync
import re,os
from time import sleep
o = ("v7_BBOT")
tokenbot = "/6337805691:AAHVUWGP5tZdj7ta_7lQgTRhGcHRB41M0og" #توكن البوت الي يوصلك عليه الصيد
dragon = "5405731745" #ايديك
app =  TelegramClient("SwapBot",api_id=15551290,api_hash="52541a59f55c6f54678a4ec33e708e0f")
app.start()
qq = 0
numche = 1
bio = "Swap bot" #نبذه البوت الي من ينصاد يخلي بيها اذا ماتعرف عوفها
namebot = "YaBh #1"
app.send_message("botfather",f'/newbot')
app.send_message("botfather",namebot)
def fucker(o):
    global qq
    if 7==7:
    	qq+=1
    	url = f"https://t.me/{o}"
    	req = requests.get(url)
    	if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
    		app.send_message("botfather",f'{o}')
    		app.send_message("botfather",f'/setabouttext')
    		app.send_message("botfather",f"@{o}")
    		app.send_message("botfather",f'{bio}')
    		y = requests.post(f"""https://api.telegram.org/bot{tele_bot}/sendmessage?chat_id={own_id}&text=« We are the strongest »
« UserName » : « @{o} »
« ClickS » : « {qq} »
« Save » : « bot »
« number » : « {numche} »
« ThE KiNg Me » : « @xx_YaBh »""")    		
while True:
	print("[ "+str(qq)+" ] : @"+o)
	fucker(o)
app.run() 
