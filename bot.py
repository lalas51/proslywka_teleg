import telebot;
bot = telebot.TeleBot('%1381323596:AAHvVjPBkfUcURunqak8YkBxtxSCJmvolnw%');
def get_text_messages(message):
@bot.message_handler(content_types=['text', 'document', 'audio'])
if message.text == "Zdarova":
    bot.send_message(message.from_user.id, "Zdarova, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши Zdarova Хряк")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю, воин. Напиши /help.")
	bot.polling(none_stop=True, interval=0)
