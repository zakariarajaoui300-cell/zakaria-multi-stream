import telebot
import subprocess

# هذا هو التوكن الخاص بك الذي حصلت عليه من BotFather
API_TOKEN = '8277065517:AAEpbvbm-gcOsgKj1qyx2vYb0WJ3gZ2FJ3c'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🏆 أهلاً بك في نظام البث المباشر الخاص بـ زكريا السباعي\n\n"
        "يرجى إرسال رابط القناة الرياضية (m3u8) لنبدأ البث فوراً."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_stream(message):
    url = message.text
    bot.reply_to(message, "⏳ جاري بدء البث المتعدد... يرجى الانتظار.")
    
    # هنا سيتم لاحقاً إضافة روابط RTMP الخاصة بفيسبوك وتيك توك
    bot.reply_to(message, f"✅ تم استلام الرابط: {url}\nالنظام جاهز للربط بالمنصات.")

bot.polling()
