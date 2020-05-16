#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import telebot
from telebot import types
from bs4 import BeautifulSoup as bs
import requests 
import time


bot = telebot.TeleBot("TOKEN")

#global var
bot_id = '@coronavirus_stat_info_bot'
date = time.ctime()


url = 'https://www.worldometers.info/coronavirus/country/iran/'
r = requests.get(url)
soup = bs(r.content,'html.parser')
items = soup.find_all('div',attrs={'class':'maincounter-number'})

cases = items[0].text.strip()
death = items[1].text.strip()
recover = items[2].text.strip()
	


#text
text_messages = {
	'user_choice':[],
	'WELCOME':
	'Please choose language.\nلطفا زبان مورد نظر را انتخاب کنید.'.encode("utf-8"),

	'welcome_en':
	'This bot is created to provide statistics of COVID-19.\n'
	'By defaut, this bot will check https://www.worldometers.info every hour and remind you if any changes occur.',

	'welcome_fa':
	'سلام،\nاین ربات آخرین آمار مربوط به کووید ۱۹ را به محض تغییر برای شما ارسال میکند.\nاین آمار از منابع کاملا معتبر بین المللی به دست می آید.'.encode("utf-8"),
	'what_to_do':
	'What should I do?',

	'taha_info':
	'You can contact the programmer via this link:\n@tatiiiij',

	'msg_template':
	"""🗓 Last Update: {}\n\n🇮🇷IRAN\n\n🏥Confirmed Cases: {}\n💀Deaths: {}\n✅Recovered: {}\n\n🆔{}""".format(date,cases,death,recover,bot_id).encode("utf-8"),
}

#ReplyKeyboardMarkup
imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Keep me updated', 'Contact programmer')

@bot.message_handler(commands=['start'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "If you want to see the COVID-19 statistics:\n select 'Keep me updated'.\n\nTo contact the developer of this bot:\nselect 'Contact programmer'. \n\n🆔@coronavirus_stat_info_bot\n🆔 @tatiiiij", reply_markup=imageSelect)  # show the keyboard
    

@bot.message_handler(func=lambda message: message.chat.id)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text
    if text == "Keep me updated":
    	bot.send_message(m.chat.id, text_messages['msg_template'])
    elif text == "Contact programmer":
    	bot.send_message(m.chat.id, text_messages['taha_info'])


bot.polling()



