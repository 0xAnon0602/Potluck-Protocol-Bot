import telebot
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("TELEGRAM_API")
bot=telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["fang"])
def fang(message):
	bashCmd = ["python3","fang.py"]
	process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
	output, error = process.communicate()


	bot.send_message(message.chat.id,output,parse_mode="html",disable_web_page_preview=True)



bot.polling()
	
