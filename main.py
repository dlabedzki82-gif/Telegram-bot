import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOARD_SIZE = 25
MINES_COUNT = 3
MINES_PICKS = 5
CHICKEN_STEPS = 10


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot symulacyjny Mines & Chicken Road\n\n"
        "Komendy:\n"
        "/mines – symulacja Mines\n"
        "/chicken – symulacja Chicken Road\n\n"
        "⚠️ To jest symulator / trening"
    )


async def mines(update: Update, context: ContextTypes.DEFAULT_TYPE):
    picks = random.sample(range(1, BOARD_SIZE + 1), MINES_PICKS)
    await update.message.reply_text(
        f"💣 MINES\n"
        f"Bezpieczne pola: {sorted(picks)}\n"
        f"Ryzyko: LOW"
    )


async def chicken(update: Update, context: ContextTypes.DEFAULT_TYPE):
    steps = random.randint(2, CHICKEN_STEPS)
    await update.message.reply_text(
        f"🐔 CHICKEN ROAD\n"
        f"Bezpieczne kroki: {steps}\n"
        f"Ryzyko: LOW"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("❌ Brak BOT_TOKEN")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("mines", mines))
    app.add_handler(CommandHandler("chicken", chicken))

    app.run_polling()


if __name__ == "__main__":
    main()
