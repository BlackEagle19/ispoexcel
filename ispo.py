import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, types
import asyncio

async def send_excel_file(excel_file_path):
    bot = Bot(token='6994284905:AAHhU7PleaVU3eSlMFt_qt3imu_KWHmya0c')
    dispatcher = Dispatcher(bot)

    with open(excel_file_path, 'rb') as file:
        await bot.send_document(chat_id='-4157001586', document=file)

    await bot.close()

file_path = 'linkler.txt'

# Initialize a list to hold the URLs
linkler = []
firma_bilgileri = []

# Open the file and read each line (URL) into the list
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Strip newline and whitespace characters from the end of each line
        clean_line = line.strip()
        if clean_line:
            # Append the clean line to the list
            linkler.append(clean_line)

for link in linkler:
    print(link)
    r=requests.get(link)
    soup=BeautifulSoup(r.content, 'html.parser')
    firma_adi=soup.find('div',class_='ce_cntct').find('div',class_='ce_head').text.strip()
    try:
        firma_adres=soup.find('div',class_='ce_addr').text.strip()
    except:
        firma_adres=''
    try:
        firma_telefon=soup.find('div',class_='ce_phone').text.strip()
    except:
        firma_telefon=''
    try:
        firma_email=soup.find('div',class_='ce_email').text.strip()
    except:
        firma_email=''
    try:
        firma_url=soup.find('div',class_='ce_website').find('a',class_='vam').get('href')
    except:
        firma_url=''

    bilgi={
        "FİRMA ADI":firma_adi,
        "FİRMA ADRES":firma_adres,
        "FİRMA TELEFON":firma_telefon,
        "FİRMA MAİL":firma_email,
        "FİRMA URL":firma_url
    }
    firma_bilgileri.append(bilgi)

df=pd.DataFrame(firma_bilgileri)
df.to_excel("IspoBilgileri.xlsx",index=False)
    
# The path to the Excel file you've created
EXCEL_FILE_PATH = 'IspoBilgileri.xlsx'

# Call the function to send the Excel file
asyncio.run(send_excel_file(EXCEL_FILE_PATH))
