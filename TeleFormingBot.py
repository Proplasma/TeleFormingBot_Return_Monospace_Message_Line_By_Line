from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import re

def format_monospace(text):
    return f"`{text}`"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.strip()
    lines = [line.strip() for line in message.split('\n') if line.strip()]

    if not lines:
        await update.message.reply_text("Bạn chưa gửi gì cả 😅")
        return

    prefix = ""
    # Kiểm tra nếu dòng đầu nằm trong dấu ngoặc kép
    match = re.match(r'^"(.+?)"$', lines[0])
    if match and len(lines) > 1:
        prefix = match.group(1)
        lines = lines[1:]

    for code in lines:
        response_text = f"{prefix} {code}".strip()
        await update.message.reply_text(format_monospace(response_text), parse_mode="Markdown")

# 🚀 Khởi chạy bot
app = ApplicationBuilder().token("API Key Of Your Telegram Bot").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
