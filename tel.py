
from aiogram import Bot
from aiogram.types import InputFile
import asyncio

async def send_excel_file(excel_file_path):
    bot = Bot(token='6994284905:AAHhU7PleaVU3eSlMFt_qt3imu_KWHmya0c')

     # Wrap the file object with InputFile
    with open(excel_file_path, 'rb') as file:
        excel_file = InputFile(file)

    await bot.send_document(chat_id='-4157001586', document=excel_file)

    await bot.close()

    
# The path to the Excel file you've created
EXCEL_FILE_PATH = 'IspoBilgileri.xlsx'

# Call the function to send the Excel file
asyncio.run(send_excel_file(EXCEL_FILE_PATH))