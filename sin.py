from requests import get
from re import findall
import os
import glob
from Arsein import Robot_Rubika
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from datetime import datetime
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image
from colorama import Fore

green = '\033[32m' 
red = '\033[31m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'

bot = Robot_Rubika(" ")
#چنلی که میخواهید اخرین پست را بگیرد و سین بزنع
channels = "c0BNYxF06118b97a3bf02bac3ae26b05"

channell_sin_tabl = ["c0HGkO0951a2f9159b86470742c0b5d0","c0Ee9X09008b057804dadf8f941e305a","c0Btyq095a83abe72ecf41080c6f1c35","c0Ee9X09008b057804dadf8f941e305a","c0Btyq095a83abe72ecf41080c6f1c35","c0MTeU0f77bd1c780b8b7509797bfd68","c0Ee8O06d4d835c994ab8a51ea0e4880"]
channells = choice(channell_sin_tabl)


answered, sleeped, retries,forward_Channell, answer,lock_fosh,st,list_gap,sttab2,st_tabl,deletergap = [] , False , {} , True , [] , False , False , [] , False , False , True
alerts, blacklist, stars, alert_stickers, alert_Gif, lock_GIF,lock_Sticker,star_sinza,sin_time,tab_time = [] , [] , [] , [] , [] , False , False , False , False , False


sum = 0
while True:
    try:
        last_chat1 = bot.getChannelInfo(channels)["data"]["chat"]["last_message_id"]
        bot.joinChannelAction(channels)
        bot.joinChannelAction("c0BE7MY0332a687bb964485f52201e3a")
        bot.joinChannelAction(channells)
        print(white+last_chat1)
        last_chat = bot.getChannelInfo(channells)["data"]["chat"]["last_message_id"]
        messages_channell = bot.getMessages(channells,last_chat)
        for chat in messages_channell:
            	        try:
            	            chat = chat['text']
            	            link_Group = findall(r"https://rubika.ir/joing/\w{32}", chat)
            	            for linkes in link_Group:
            	                list_gap.append(linkes)
            	                randomli = choice(list_gap)
            	                tabeligh = bot.joinGroup(randomli)
            	                tabrligh = tabeligh['data']['group']['group_guid']
            	                info = tabeligh['data']['group']['group_title']
            	                momber = tabeligh['data']['group']['count_members']
            	                sum += 1
            	                bot.forwardMessages(channels,[last_chat1],tabrligh)
            	                res1 = bot.getMessagesInfo(channels, [last_chat1])
            	                for n in res1:
            	                    sen = n['count_seen']
            	                    print(green+f" forward mag : <{randomli}> \n {blue}name gap : <{info}> \n {yellow}forward : <{sum}> \n {blue}member group : <{momber}> \n {red}seen <{sen}>")
            	                    bot.leaveGroup(tabrligh)
            	                    
            	        except:continue  
        
    except:pass