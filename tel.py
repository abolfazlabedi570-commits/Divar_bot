from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes , MessageHandler , filters
from scraper import get_avg_price_from_divar

TOKEN = "8478782867:AAEVyTqU98-Zxx2jjR0UmcqzgrfAcOjD2qY"

async def handler_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text.strip()
    await update.message.reply_text(f"در حال جستجو برای {query}...")

    avg = get_avg_price_from_divar(query)
    if avg :
        await update.message.reply_text(f"میانگین قیمت برای {avg} تومان")
    else:
        await update.message.reply_to_message("محصول مورد نظر پیدا نشد")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & filters.COMMAND , handler_query))

app.run_polling()