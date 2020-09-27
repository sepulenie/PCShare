import os, time
from telegram.ext import Updater, CommandHandler
screenshots_path = r"d:/YandexDisk/GameScreenshots/Twitter/"

def start(update, context):
    while True:
        screenshots = [screenshot for screenshot in os.listdir(screenshots_path) if os.path.isfile(os.path.join(screenshots_path, screenshot))]
        if screenshots == []:
            time.sleep(5)
        else:
            for screenshot in screenshots:
                update.message.reply_document(photo = open(screenshots_path + screenshot , 'rb'), caption = '#PCShare')
                os.remove(screenshots_path + screenshot)
                time.sleep(1)

def main():
    updater = Updater("1108001851:AAG-SjRmOqZDOQRpe3-ftXKzy0XqWhBu6kU", use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


main()