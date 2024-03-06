from telegram import Bot
from telegram import InputFile
import telegram.ext
import logging

def send_excel_file(excel_file_path, bot_token, chat_id):
    # Bot'u başlat
    bot = Bot(token=bot_token)

    # Loglama yapısını ayarla (isteğe bağlı)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # Excel dosyasını gönder
    with open(excel_file_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)

# Bot token'ınızı ve hedef chat ID'nizi girin
BOT_TOKEN = '6994284905:AAHhU7PleaVU3eSlMFt_qt3imu_KWHmya0c'
CHAT_ID = '-4157001586'  # Kanal için "@channelusername" şeklinde de kullanılabilir

# Göndermek istediğiniz Excel dosyasının yolu
EXCEL_FILE_PATH = 'IspoBilgileri.xlsx'

# Fonksiyonu çağır
send_excel_file(EXCEL_FILE_PATH, BOT_TOKEN, CHAT_ID)
