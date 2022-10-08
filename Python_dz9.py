# 3. Загрузчик видео с YouTube (в видео и аудио версиях)

import ssl
from pytube import YouTube
from telegram import Update
from telegram.ext import Updater
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

# updater = Updater("y5741971548:AAEq_sXjdbCz0mtJKX-qx0bunXdNnP2SwIc",
#                   use_context=True)
                  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, Please write\
        /help to see the commands available.')

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("""Available Commands :-/url ссылка для скачивания - To get the youtube URL -> ссылка""")

async def sslk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Секундочку....')
    url = update.message.text.split()
    url_origin = url[1]
    print(url_origin)
    yt = YouTube(url_origin)
    stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
    stream.download() #загружаем видео.
    t=yt.streams.filter(only_audio=True).all()
    t[0].download()
    await update.message.reply_text(f'Готово! Ваше видео на сервере!')

app = ApplicationBuilder().token("5741971548:AAEq_sXjdbCz0mtJKX-qx0bunXdNnP2SwIc").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("url", sslk))
print('server start')
app.run_polling()



# https://github.com/KotegovAlex/Seminar10.git
# билблиотке pyowm
# https://github.com/RomanBusygin/phone_book 
# aiogram

