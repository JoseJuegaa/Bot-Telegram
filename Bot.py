from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Reemplaza esto con tu token real del BotFather
TOKEN = "8403502268:AAGCgweu_3MUyjAiL-g6sxvSQkA8pJUTh00"

# 💬 Mensaje que enviará el bot al usar /start o /iniciar
MENSAJE = (
    "👋 ¡Hola!\n\n"
    "Para desbloquear todo el contenido del grupo, comparte este link en 3 grupos distintos:\n"
    "🔗 https://t.me/+ekzc30yAM2dlY2Mx"
)

# Función para /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENSAJE)

# Función para /iniciar
async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENSAJE)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Maneja ambos comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("iniciar", iniciar))

    print("🤖 Bot ejecutándose...")
    app.run_polling()

if __name__ == "__main__":
    main()
