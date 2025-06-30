import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.environ.get("7004135727:AAG0SHRKPFtoKfFU2cWd1rxjXWmkfat6sGE")
YOUR_USERNAME = os.environ.get("@canxuanquang")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    text = message.text.lower()

    if YOUR_USERNAME.lower() in text and "ăn" in text:
        await message.reply_text("Đừng rủ chủ nhân của tôi đi NHẬU nữa !!")

if __name__ == '__main__':
    print("🤖 Bot is starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_message))
    app.run_polling()
