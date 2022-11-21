import telebot

API_TOKEN = 'API'
chat_id = 'CHAT_ID'
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

doc = open('app-debug.apk', 'rb')
bot.send_document(chat_id, doc)
bot.send_document(chat_id, "FILEID")
