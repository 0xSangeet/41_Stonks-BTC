import g4f
from scraper import scrape
import telebot
from termcolor import colored

token = '' # put your telegram bot token here
channel_username = '' #put your channel's username here starting with an @
bot = telebot.TeleBot(token)
chat = bot.get_chat(chat_id=channel_username)

print(colored('''

  ___   ___   ____        _     _____                   _                         
 |  _|_|_  | |  _ \      | |   |  __ \                 (_)                        
 | |_| |_| | | |_) | ___ | |_  | |__) |   _ _ __  _ __  _ _ __   __ _             
 | |_   _| | |  _ < / _ \| __| |  _  / | | | '_ \| '_ \| | '_ \ / _` |            
 | | |_| | | | |_) | (_) | |_  | | \ \ |_| | | | | | | | | | | | (_| |  _   _   _ 
 | |_   _| | |____/ \___/ \__| |_|  \_\__,_|_| |_|_| |_|_|_| |_|\__, | (_) (_) (_)
 |___| |___|                                                     __/ |            
                                                                |___/             

''', 'green'))

scrape()

def get_response():
    with open('prompts.txt', 'r') as f:
        prompts = f.readlines()
    print(colored("[+]Method triggered...", 'cyan'))
    for prompt in prompts:
        response = g4f.ChatCompletion.create(model=g4f.models.gpt_35_turbo_16k_0613, messages=[{"role": "user", "content": f'{prompt} . Respond strictly within 3000 characters!'}])
        bot.send_message(chat.id, response.replace('**', '').replace('####', ''))
        print(colored("[+]Successfully posted message!", 'yellow'))
        

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Bot running...")
    get_response()

bot.infinity_polling()