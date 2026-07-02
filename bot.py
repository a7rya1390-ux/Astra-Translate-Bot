from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

TOKEN = "8830629420:AAG5ZgGSTJX1ZHML7WhcWmamE7_lF6oLr1A"

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text

        translated = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        await update.message.reply_text(translated)

app = Application.builder().token(TOKEN).build()

# مهم: ساده‌ترش کردیم
app.add_handler(MessageHandler(filters.TEXT, translate))

print("Bot is running...")

app.run_polling()
