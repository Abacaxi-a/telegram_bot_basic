import telebot

token = '<telegram token>'

bot  = telebot.TeleBot(token)

def send_msg(chat,msg):
        bot.send_message(chat,msg)

send_msg()
