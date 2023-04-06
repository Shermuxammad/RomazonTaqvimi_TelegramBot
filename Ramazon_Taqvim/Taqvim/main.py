"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from telebot import types

API_TOKEN = '5896757639:AAEtZpNfeKC5BCVVs8i2TO0VJlbTZvCp8Z0'

class States(StatesGroup):
    home = State()
    location = State()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#button1 = KeyboardButton("2023 RAMAZON TAQVIMI")
#button2 = KeyboardButton("BUGUNGI RO'ZA VAQTLARI")

buttonLocation = KeyboardButton("HUDUD BO'YICHA RO'ZA VAQTLARI")
button3 = KeyboardButton("RAMAZON OYI HAQIDA MA'LUMOT")
button4 = KeyboardButton("SAHARLIK VA IFTORIK DUOLARI")
button0 = KeyboardButton("Bot adminiga murojaat")

button5 = KeyboardButton("Toshkent sh.")
button6 = KeyboardButton("Toshkent vil.")
button7 = KeyboardButton("Andijon vil.")
button8 = KeyboardButton("Farg'ona vil.")
button9 = KeyboardButton("Namangan vil.")
button10 = KeyboardButton("Sirdaryo vil.")
button11 = KeyboardButton("Jizzax vil.")
button12 = KeyboardButton("Samarqand vil.")
button13 = KeyboardButton("Qashqadaryo vil.")
button14 = KeyboardButton("Surxondaryo vil.")
button15 = KeyboardButton("Navoiy vil.")
button16 = KeyboardButton("Xorazm vil.")
button17 = KeyboardButton("Qoraqalpog'iston Res.")

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .add(buttonLocation)\
    .add(button3)\
    .add(button4)\
    .add(button0)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button5).add(button6).add(
    button7).add(button8).add(button9).add(button10).add(button11).add(button12).add(button13).add(button14).add(
    button15).add(button16).add(button17)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` commandL
    """

    await States.home.set()

    await message.reply(
        "<b>Assalomu aleykum\nRAMAZON taqvimi rasmiy botga\n\n   XUSH KELIBSIZ\n\nMurojaat qiluvchi buyerda 'O'zbekiston Musulmonlar idorasi' tomonidan e'lon qilingan ushbu yilgi Ramazon taqvimini, Ramazon oyida o'qiladigan 'SAHARLIK' va 'IFTORLIK' duolarini qolaversa Mukammal va Go'zal dinimiz haqida go'zal ma'lumotlarni olishi mumkin.</b>",
        parse_mode='HTML')
    await message.reply(
        "Quyidagi xizmatlarning birini 'HUDUD BO'YICHA RO'ZA VAQTLARI' yoki '/location' menyusidan foydalanib O'zbekistondagi istalgan viloyat/shahar ning Romazon vaqtlarini bilishingiz mumkin:"
        "\n\n/start - <i>qayta yuklash</i>"
        "\n/location - <i>Yashayotgan manzilni tanlash</i>",
        parse_mode='HTML', reply_markup=keyboard1)



@dp.message_handler(commands=['location'], state="*")
@dp.message_handler(Text(equals="HUDUD BO'YICHA RO'ZA VAQTLARI", ignore_case=True), state=States.home)
async def send_welcome(message: types.Message):
    print("location command", message.text)
    await States.location.set()

    await message.answer("Iltimos hududni tanlang.", parse_mode='HTML', reply_markup=keyboard2)


@dp.message_handler(Text(equals="Toshkent sh.", ignore_case=True), state=States.location)
async def send_times_for_tashkent_city(message: types.Message):

    await States.home.set()

    await message.answer_photo(
        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FugVdsO19p48%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DugVdsO19p48&tbnid=ZObBjQ_nyPdjeM&vet=12ahUKEwjPhcn_tM79AhWHl4sKHQOIAzkQMygAegUIARC-AQ..i&docid=Q3vwwZxrEfk_KM&w=1280&h=720&q=ramazon%20taqvimi%202023%20toshkent&client=avast-a-1&ved=2ahUKEwjPhcn_tM79AhWHl4sKHQOIAzkQMygAegUIARC-AQ')

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi va Toshkent vaqti bilan ko'rsatildi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:03  IFTORLIK - 18:40 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 18:41 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 18:42 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 04:56  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:54  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:28  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:27  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:19  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:17  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:15  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:13  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:11  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:10  IFTORLIK - 19:11 -</b>",
        parse_mode='HTML')

    await message.answer("\n\n\n<i>Quyosh chiqishi va botishi vaqtidagi farqlar(daqiqalarda):</i>"
                         "\n        <b>TOSHKENT VAQTIDAN OLDIN</b>"
                         "\nBekobod -4/-1, Qo'qon -4/-1, Namangan -8/-10, Farg'ona -7/-10, Andijon -10/-13, Angren -2/-4 Xonobod -13/-15"
                         "\n\n<i>Quyosh chiqishi va botishi vaqtidagi farqlar(daqiqalarda):</i>"
                         "\n        <b>TOSHKENT VAQTIDAN KEYIN</b>"
                         "\nJizzax +10/+5, Guliston +5/+1, Denov +15/+3,"
                         "\nTermiz +20/+5, Samarqand +15/+8, Qarshi +22/+12"
                         "\nNurota +17/+14, Navoiy +20/+15, Uchquduq +20/+23"
                         "\nKattaqo'rg'on -17/+11, Mo'ynoq +33/+42, Buxoro +24/+18"
                         "\n Nukus +35/+39", parse_mode='HTML', reply_markup=keyboard1)


@dp.message_handler(Text(equals="Toshkent vil.", ignore_case=True), state=States.location)
async def send_times_for_tashkent_village(message: types.Message):

    await States.home.set()

    await message.answer_photo(

        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FugVdsO19p48%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DugVdsO19p48&tbnid=ZObBjQ_nyPdjeM&vet=12ahUKEwjPhcn_tM79AhWHl4sKHQOIAzkQMygAegUIARC-AQ..i&docid=Q3vwwZxrEfk_KM&w=1280&h=720&q=ramazon%20taqvimi%202023%20toshkent&client=avast-a-1&ved=2ahUKEwjPhcn_tM79AhWHl4sKHQOIAzkQMygAegUIARC-AQ')

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:03  IFTORLIK - 18:40 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 18:41 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 18:42 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 04:56  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:54  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:28  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:27  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:19  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:17  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:15  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:13  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:11  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:10  IFTORLIK - 19:11 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)


@dp.message_handler(Text(equals="Andijon vil.", ignore_case=True), state=States.location)
async def send_times_for_andijan_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 04:52  IFTORLIK - 18:28 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 18:29 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 18:30 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 18:31 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 18:32 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 18:33 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 18:34 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 18:35 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 18:36 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 18:37 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 18:38 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 18:40 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:31  IFTORLIK - 18:41 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:29  IFTORLIK - 18:42 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:27  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:19  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:17  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:16  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:14  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:12  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:10  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:08  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:06  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:04  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:02  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:00  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 03:59 - 18:58 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)


@dp.message_handler(Text(equals="Farg'ona vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 18:30 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 18:31 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 04:52  IFTORLIK - 18:32 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 18:33 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 04:48  IFTORLIK - 18:34 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 18:35 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 18:36 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 18:37 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:41  IFTORLIK - 18:38 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:39  IFTORLIK - 18:39 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:37  IFTORLIK - 18:40 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:35  IFTORLIK - 18:42 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:28  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:26  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:24  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:20  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:18  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:16  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:14  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:12  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:10  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:08  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:06  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:04  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:03  IFTORLIK - 19:00 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)


@dp.message_handler(Text(equals="Namangan vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 04:54  IFTORLIK - 18:31 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 04:52  IFTORLIK - 18:32 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 18:33 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 18:34 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 18:35 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 18:36 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 18:37 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 18:38 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 18:39 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 18:40 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 18:41 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:33  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:31  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:29  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:27  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:19  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:18  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:16  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:14  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:12  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:10  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:08  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:06  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:04  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:02  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:01  IFTORLIK - 19:01 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)



@dp.message_handler(Text(equals="Sirdaryo vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:07  IFTORLIK - 18:42 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:05  IFTORLIK - 18:43 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 18:44 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:02  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:31  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:29  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:27  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:23  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:19  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:17  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:16  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:15  IFTORLIK - 19:12 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)



@dp.message_handler(Text(equals="Jizzax vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:11  IFTORLIK - 18:45 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:09  IFTORLIK - 18:46 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:08  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:02  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 04:59  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:48  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:39  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:37  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:28  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:26  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:24  IFTORLIK - 19:13 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:22  IFTORLIK - 19:14 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:21  IFTORLIK - 19:14 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:20  IFTORLIK - 19:15 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)




@dp.message_handler(Text(equals="Samarqand vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:15  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:13  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:12  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:10  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:08  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:05  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:03  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 04:59  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:54  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:52  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:48  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:41  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:13 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 19:15 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:28  IFTORLIK - 19:16 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:26  IFTORLIK - 19:17 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:26  IFTORLIK - 19:17 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:25  IFTORLIK - 19:18 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)




@dp.message_handler(Text(equals="Qashqadaryo vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:20  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:18  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:17  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:15  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:13  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:11  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:10  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:10  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:08  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 05:02  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:59  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:48  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:13 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 19:14 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 19:15 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:41  IFTORLIK - 19:16 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:39  IFTORLIK - 19:17 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:37  IFTORLIK - 19:19 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:35  IFTORLIK - 19:20 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:33  IFTORLIK - 19:21 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:33  IFTORLIK - 19:20 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:21 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)




@dp.message_handler(Text(equals="Surxondaryo vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:16  IFTORLIK - 18:47 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:14  IFTORLIK - 18:48 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:13  IFTORLIK - 18:49 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:11  IFTORLIK - 18:50 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:09  IFTORLIK - 18:51 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:07  IFTORLIK - 18:52 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 18:53 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 18:54 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 05:02  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 19:02 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 19:07 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 19:13 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:31  IFTORLIK - 19:13 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)




@dp.message_handler(Text(equals="Navoiy vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:21  IFTORLIK - 18:55 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:19  IFTORLIK - 18:56 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:18  IFTORLIK - 18:57 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:16  IFTORLIK - 18:58 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:14  IFTORLIK - 18:59 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:12  IFTORLIK - 19:00 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:11  IFTORLIK - 19:01 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:09  IFTORLIK - 19:03 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:07  IFTORLIK - 19:04 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 05:05  IFTORLIK - 19:05 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 05:03  IFTORLIK - 19:06 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 19:08 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 19:09 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 19:10 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 04:56  IFTORLIK - 19:11 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 04:54  IFTORLIK - 19:12 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 04:52  IFTORLIK - 19:13 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 04:50  IFTORLIK - 19:14 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 19:14 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:15 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 19:16 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:44  IFTORLIK - 19:17 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:42  IFTORLIK - 19:18 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 19:19 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:38  IFTORLIK - 19:20 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:36  IFTORLIK - 19:22 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:34  IFTORLIK - 19:23 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:32  IFTORLIK - 19:24 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:31  IFTORLIK - 19:24 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:30  IFTORLIK - 19:25 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)




@dp.message_handler(Text(equals="Xorazm vil.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:36  IFTORLIK - 18:15 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:34  IFTORLIK - 18:16 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:33  IFTORLIK - 18:17 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:31  IFTORLIK - 18:18 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:29  IFTORLIK - 18:19 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:27  IFTORLIK - 18:20 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:26  IFTORLIK - 18:21 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:23  IFTORLIK - 18:23 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:21  IFTORLIK - 18:24 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 05:19  IFTORLIK - 18:25 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 05:17  IFTORLIK - 18:26 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 05:15  IFTORLIK - 18:28 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 05:14  IFTORLIK - 18:29 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 05:12  IFTORLIK - 19:30 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 05:10  IFTORLIK - 19:31 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 05:08  IFTORLIK - 19:32 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 19:33 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 19:34 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 05:00  IFTORLIK - 19:36 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 04:58  IFTORLIK - 19:37 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 19:38 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 19:39 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 19:40 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 19:41 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 19:42 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:44 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:45  IFTORLIK - 19:45 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:43  IFTORLIK - 19:46 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:41  IFTORLIK - 19:48 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:40  IFTORLIK - 19:49 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)





@dp.message_handler(Text(equals="Qoraqalpog'iston Res.", ignore_case=True), state=States.location)
async def send_times_for_ferghana_village(message: types.Message):

    await States.home.set()

    await message.answer(
        "<b>Eslatma:</b> <i>Romazon oyi boshlanishi oy chiqishiga qarab, bir kunga farqlanishi mumkin.</i>", parse_mode='HTML')

    await message.answer(
        "Ramazon oyi taqvimi O'zbekiston musulmonlar idorasi tomonidan tasdiqlandi."
        "\n\n\nKun: '1'   Xafta kuni: 'PAYSHANBA'   Sana: '23-MART'\n\n         <b>- SAHARLIK - 05:41  IFTORLIK - 19:18 -</b>"
        "\n\n\nKun: '2'   Xafta kuni: 'JUMA'   Sana: '24-MART'\n\n         <b>- SAHARLIK - 05:39  IFTORLIK - 19:19 -</b>"
        "\n\n\nKun: '3'   Xafta kuni: 'SHANBA'   Sana: '25-MART'\n\n         <b>- SAHARLIK - 05:38  IFTORLIK - 19:20 -</b>"
        "\n\n\nKun: '4'   Xafta kuni: 'YAKSHANBA'   Sana: '26-MART'\n\n         <b>- SAHARLIK - 05:36  IFTORLIK - 19:21 -</b>"
        "\n\n\nKun: '5'   Xafta kuni: 'DUSHANBA'   Sana: '27-MART'\n\n         <b>- SAHARLIK - 05:34  IFTORLIK - 19:22 -</b>"
        "\n\n\nKun: '6'   Xafta kuni: 'SESHANBA'   Sana: '28-MART'\n\n         <b>- SAHARLIK - 05:32  IFTORLIK - 19:23 -</b>"
        "\n\n\nKun: '7'   Xafta kuni: 'CHORSHANBA'   Sana: '29-MART'\n\n         <b>- SAHARLIK - 05:31  IFTORLIK - 19:24 -</b>"
        "\n\n\nKun: '8'   Xafta kuni: 'PAYSHANBA'   Sana: '30-MART'\n\n         <b>- SAHARLIK - 05:28  IFTORLIK - 19:27 -</b>"
        "\n\n\nKun: '9'   Xafta kuni: 'JUMA'   Sana: '31-MART'\n\n         <b>- SAHARLIK - 05:26  IFTORLIK - 19:28 -</b>"
        "\n\n\nKun: '10'   Xafta kuni: 'SHANBA'   Sana: '1-APREL'\n\n         <b>- SAHARLIK - 05:24  IFTORLIK - 19:29 -</b>"
        "\n\n\nKun: '11'   Xafta kuni: 'YAKSHANBA'   Sana: '2-APREL'\n\n         <b>- SAHARLIK - 05:22  IFTORLIK - 19:30 -</b>"
        "\n\n\nKun: '12'   Xafta kuni: 'DUSHANBA'   Sana: '3-APREL'\n\n         <b>- SAHARLIK - 05:20  IFTORLIK - 19:32 -</b>"
        "\n\n\nKun: '13'   Xafta kuni: 'SESHANBA'   Sana: '4-APREL'\n\n         <b>- SAHARLIK - 05:19  IFTORLIK - 19:33 -</b>"
        "\n\n\nKun: '14'   Xafta kuni: 'CHORSHANBA'   Sana: '5-APREL'\n\n         <b>- SAHARLIK - 05:17  IFTORLIK - 19:34 -</b>"
        "\n\n\nKun: '15'   Xafta kuni: 'PAYSHANBA'   Sana: '6-APREL'\n\n         <b>- SAHARLIK - 05:15  IFTORLIK - 19:35 -</b>"
        "\n\n\nKun: '16'   Xafta kuni: 'JUMA'   Sana: '7-APREL'\n\n         <b>- SAHARLIK - 05:13  IFTORLIK - 19:36 -</b>"
        "\n\n\nKun: '17'   Xafta kuni: 'SHANBA'   Sana: '8-APREL'\n\n         <b>- SAHARLIK - 05:11  IFTORLIK - 19:37 -</b>"
        "\n\n\nKun: '18'   Xafta kuni: 'YAKSHANBA'   Sana: '9-APREL'\n\n         <b>- SAHARLIK - 05:09  IFTORLIK - 19:38 -</b>"
        "\n\n\nKun: '19'   Xafta kuni: 'DUSHANBA'   Sana: '10-APREL'\n\n         <b>- SAHARLIK - 05:06  IFTORLIK - 19:39 -</b>"
        "\n\n\nKun: '20'   Xafta kuni: 'SESHANBA'   Sana: '11-APREL'\n\n         <b>- SAHARLIK - 05:04  IFTORLIK - 19:40 -</b>"
        "\n\n\nKun: '21'   Xafta kuni: 'CHORSHANBA'   Sana: '12-APREL'\n\n         <b>- SAHARLIK - 05:03  IFTORLIK - 19:41 -</b>"
        "\n\n\nKun: '22'   Xafta kuni: 'PAYSHANBA'   Sana: '13-APREL'\n\n         <b>- SAHARLIK - 05:01  IFTORLIK - 19:42 -</b>"
        "\n\n\nKun: '23'   Xafta kuni: 'JUMA'   Sana: '14-APREL'\n\n         <b>- SAHARLIK - 04:59  IFTORLIK - 19:43 -</b>"
        "\n\n\nKun: '24'   Xafta kuni: 'SHANBA'   Sana: '15-APREL'\n\n         <b>- SAHARLIK - 04:57  IFTORLIK - 19:44 -</b>"
        "\n\n\nKun: '25'   Xafta kuni: 'YAKSHANBA'   Sana: '16-APREL'\n\n         <b>- SAHARLIK - 04:55  IFTORLIK - 19:45 -</b>"
        "\n\n\nKun: '26'   Xafta kuni: 'DUSHANBA'   Sana: '17-APREL'\n\n         <b>- SAHARLIK - 04:53  IFTORLIK - 19:47 -</b>"
        "\n\n\nKun: '27'   Xafta kuni: 'SESHANBA'   Sana: '18-APREL'\n\n         <b>- SAHARLIK - 04:51  IFTORLIK - 19:48 -</b>"
        "\n\n\nKun: '28'   Xafta kuni: 'CHORSHANBA'   Sana: '19-APREL'\n\n         <b>- SAHARLIK - 04:49  IFTORLIK - 19:49 -</b>"
        "\n\n\nKun: '29'   Xafta kuni: 'PAYSHANBA'   Sana: '20-APREL'\n\n         <b>- SAHARLIK - 04:47  IFTORLIK - 19:51 -</b>"
        "\n\n\nKun: '30'   Xafta kuni: 'JUMA'   Sana: '21-APREL'\n\n         <b>- SAHARLIK - 04:46  IFTORLIK - 19:52 -</b>",
        parse_mode='HTML', reply_markup=keyboard1)








@dp.message_handler(state="*")
async def kb_answer(message: types.Message):

    if message.text == "RAMAZON OYI HAQIDA MA'LUMOT":
        # file = open('Ramazon.mp4', 'rb')
        # await bot.send_video(message.chat.id, "https://youtu.be/qu6p2jF086k")
        await  message.answer("<b>      Ramazon — xayr va baraka oyi</b>"
                              "\n\nMuqaddas islom dinining asosiy ulug‘ ruknlaridan biri ro‘za ibodatidir."
                              " Ramazon ochlik, tashnalik, nafsni qiynash bilan Alloh taologa qurbat, taqvo hosil qilinadigan buyuk oydir."
                              " Alloh taolo bandalari uchun har ikki dunyo saodatini ko‘zlab bu ibodatni islomning ulug‘ farzlari qatoriga qo‘shgan."
                              " Ro‘za nafaqat Muhammad (s.a.v)ning ummatlariga, balki avvalgi payg‘ambarlarning ham ummatlariga ham buyurilgandir."
                              "Ramazon ro‘zasi Hazrati Payg‘ambarimiz (s.a.v) Madinaga hijrat qilganlaridan so‘ng, hijratning ikkinchi yili sha’bon oyida farz qilingan."
                              "\nAlloh Taolo Baqara surasining 183-oyatida marhamat qiladi: "
                              "<b>«Ey iymon keltirganlar! Sizlardan avvalgilarga farz qilinganidek, sizlarga ham ro‘za farz qilindi. Shoyadki, taqvodor bo‘lsangiz».</b>"
                              "Ushbu oyati karima bilan dinimizning beshta asosiy ustunlaridan bo‘lgan ramazon ro‘zasi farz bo‘ldi."
                              "\nAbu Hurayra roziyallohu anhudan rivoyat qilinadi: Payg‘ambar (s.a.v) dedilar: "
                              "<b>«Sizlarga muborak ramazon oyi keldi. Alloh azza va jalla uning ro‘zasini tutmoqlikni farz qildi. "
                              "Unda osmonlarning eshiklari ochiladi. Unda jahannamning eshiklari yopiladi. "
                              "Unda shaytonlar kishanband qilinadi. Unda Allohning bir kechasi bo‘lib, u ming oydan yaxshidir. "
                              "Kim u kechaning yaxshiligidan mahrum bo‘lsa, batahqiq (juda ko‘p narsadan) mahrum qolibdi»</b> — dedilar. (Nasoiy va Bayhaqiy rivoyati)."
                              "\nRo‘za eng uzun ibodatlardan biri sanaladi. Boshqa ibodatlarning vaqti juda qisqa bo‘ladi."
                              " Ro‘za ibodati bizning o‘lkalarda kun eng qisqargan vaqt — qishga to‘g‘ri kelsa, 11-12 soat davom etadi."
                              " Kun eng uzun vaqt — yozga to‘g‘ri kelsa, 17-18 soat davom etadi. Bu ro‘za ibodatida riyo bo‘lmaydi."
                              " Boshqa ibodatlarda biroz bo‘lsada riyosi bor, namoz o‘qisak hamma ko‘radi. "
                              "Zakotni yashirib bergan taqdirda ham zakot oluvchi buni biladi. Haj ibodati ham barcha biladigan ibodatdir."
                              " Ammo ro‘zani Alloxdan boshqa hech kim bilmaydi. Shuning uchun savobini Allohning o‘zi beradi. Hadisi qudsiyda aytiladi:"
                              "\nAbu Hurayra roziyallohu anhu ushbu hadisi qudsiyni rivoyat qiladilar: "
                              "Rasululloh (s.a.v) marhamat qiladilar: "
                              "<b>«Alloh taolo aytadiki: «Har bir yaxshi amal uchun o‘n barobardan yetti yuz barobargacha savob beraman, faqat ro‘za bundan mustasno. "
                              "U men uchun tutiladi, uning ajrini ham o‘zim beraman.» — degan»</b> (muttafaqun alayh)"
                              "\nRasululloh (s.a.v): <b>«Kimki ramazon ro‘zasini iymon e’tiqod va Allohdan savob umid qilib tutsa uning o‘tgan gunohlari kechirilib yuboriladi»</b> — dedilar (Buxoriy rivoyati)."
                              "\n Alloh taolo tomonidan ro‘za ibodatining bandalariga farz qilinishi juda ko‘p hikmatga ega:"
                              "Ro‘za tutgan banda, eng avvalo, Allohga taqvo qilgan bo‘ladi, taqvodorligi oshadi. Alloh taolo Qur’onda <b>«Shoyadki, taqvo qilsangiz»</b> — degan.",
                              reply_markup=keyboard1, parse_mode='HTML')

    elif message.text == "SAHARLIK VA IFTORIK DUOLARI":
        await message.answer_photo(
            'https://i.mycdn.me/i?r=AzEPZsRbOZEKgBhR0XGMT1RkqbQMeZTt5H9Uq1q37d_zxqaKTM5SRkZCeTgDn6uOyic')

        await message.answer("\n\n\nRo‘za tutish (saharlik, og‘iz yopish) duosi"
                             "\n\n                                       <b>نَوَيْتُ أَنْ أَصُومَ صَوْمَ شَهْرَ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ، خَالِصًا لِلهِ تَعَالَى أَللهُ أَكْبَرُ</b>"
                             "\n    NAVAYTU AN ASSUMA SOVMA SHAHRI ROMAZONA MINAL FAJRI ILAL MAG'RIBI, XOLISAN LILLAHI TA’AALAA ALLOHU AKBAR."
                             "\n    Ma’nosi: <i>Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.</i>"
                             "\n\n\nIftorlik (og‘iz ochish) duosi"
                             "\n                 اَللَّهُمَّ لَكَ صُمْتُ وَ بِكَ آمَنْتُ وَ عَلَيْكَ تَوَكَّلْتُ وَ عَلَى رِزْقِكَ أَفْتَرْتُ، فَغْفِرْلِى مَا قَدَّمْتُ وَ مَا أَخَّرْتُ بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِينَ"
                             "\n    ALLOHUMMA LAKA SUMTU VA BIKA AMANTU VA A’LAYKA TAVAKALTU VA A’LAA RIZQIKA AFTARTU, FAG‘FIRLIY MA QODDAMTU VA MAA AXXORTU BIROHMATIKA YA ARHAMAR ROHIMIYN."
                             "\n    Ma’nosi: <i>Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.</i>",
                             parse_mode='HTML', reply_markup=keyboard1)


    elif message.text == "Bot adminiga murojaat":
        await  message.answer("     Siz admin bilan ushbu ssilkalar orqali murojaat qilishingiz mumkin:"
                              "\n\n Telegram: https://t.me/KayumovSher592"
                              "\n\n Instagramm/username: kayumovsher592", reply_markup=keyboard1)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
