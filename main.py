import telebot

# تأكد أن هذا السطر لا يحتوي على أي مسافات زائدة
API_TOKEN = "8277065517:AAEpbvbm-gcOsgKj1qyx2vYbOWJ3gZ2FJ3c"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً يا زكريا! البوت شغال الآن بنجاح ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "وصلت رسالتك: " + message.text)

if __name__ == "__main__":
    bot.infinity_polling()
