from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

    


quran = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="AL-QURAN"), KeyboardButton(text="XADISLAR")],
        [KeyboardButton(text="MUALLIMA-SONIY"), KeyboardButton(text="ARABTILI-KITOBI")],
        [KeyboardButton(text="ARABTILI-GRAMMATIKASI"), KeyboardButton(text="Chiqish <-")],
    ],
    resize_keyboard=True,
    
    one_time_keyboard=True
)


Aljomiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="AL-JOMI'AS-SAHIH (1-jild)"), KeyboardButton(text="AL-JOMI'AS-SAHIH (2-jild)")],
        [KeyboardButton(text="AL-JOMI'AS-SAHIH (3-jild)"), KeyboardButton(text="AL-JOMI'AS-SAHIH (4-jild)")],
        [KeyboardButton(text="chiqish <-"),]
    ],
    resize_keyboard=True,
    
    one_time_keyboard=True
)


menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Arab Harflari"), KeyboardButton(text="Arab Harflari O`qilish")],
        [KeyboardButton(text="Kitoblar")],
    ],
    resize_keyboard=True,
    
    one_time_keyboard=True
)


oqish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-dars"), KeyboardButton(text="2-dars"), KeyboardButton(text="3-dars")],
        [KeyboardButton(text="4-dars"), KeyboardButton(text="5-dars"), KeyboardButton(text="6-dars")],
        [KeyboardButton(text="7-dars"), KeyboardButton(text="8-dars"), KeyboardButton(text="9-dars")],
        [KeyboardButton(text="10-dars"), KeyboardButton(text="11-dars"), KeyboardButton(text="12-dars")],
        [KeyboardButton(text="13-dars"), KeyboardButton(text="14-dars"), KeyboardButton(text="15-dars")],
        [KeyboardButton(text="16-dars"), KeyboardButton(text="17-dars"), KeyboardButton(text="18-dars")],
        [KeyboardButton(text="19-dars"), KeyboardButton(text="20-dars"), KeyboardButton(text="21-dars")],
        [KeyboardButton(text="22-dars"), KeyboardButton(text="23-dars"), KeyboardButton(text="24-dars")],
        [KeyboardButton(text="25-dars"), KeyboardButton(text="26-dars"), KeyboardButton(text="27-dars")],
        [KeyboardButton(text="28-dars"), KeyboardButton(text="29-dars"), KeyboardButton(text="30-dars")],
        [KeyboardButton(text="31-dars"), KeyboardButton(text="32-dars"), KeyboardButton(text="33-dars")],
        [KeyboardButton(text="34-dars"), KeyboardButton(text="35-dars"), KeyboardButton(text="36-dars")],
        [KeyboardButton(text="37-dars"), KeyboardButton(text="38-dars"), KeyboardButton(text="39-dars")],
        [KeyboardButton(text="40-dars"), KeyboardButton(text="41-dars"), KeyboardButton(text="42-dars")],
        [KeyboardButton(text="43-dars"), KeyboardButton(text="44-dars"), KeyboardButton(text="45-dars")],
        [KeyboardButton(text="46-dars"), KeyboardButton(text="47-dars"), KeyboardButton(text="48-dars")],
        [KeyboardButton(text="49-dars"), KeyboardButton(text="50-dars"), KeyboardButton(text="51-dars")],
        [KeyboardButton(text="52-dars"), KeyboardButton(text="53-dars"), KeyboardButton(text="54-dars")],
        [KeyboardButton(text="55-dars"), KeyboardButton(text="56-dars"), KeyboardButton(text="57-dars")],
        [KeyboardButton(text="58-dars"), KeyboardButton(text="59-dars"), KeyboardButton(text="60-dars")],
        [KeyboardButton(text="61-dars"), KeyboardButton(text="62-dars"), KeyboardButton(text="63-dars")],
        [KeyboardButton(text="64-dars"), KeyboardButton(text="65-dars"), KeyboardButton(text="66-dars")],
        [KeyboardButton(text="67-dars"), KeyboardButton(text="68-dars"), KeyboardButton(text="69-dars")],
        [KeyboardButton(text="70-dars"), KeyboardButton(text="71-dars"), KeyboardButton(text="72-dars")],
        [KeyboardButton(text="73-dars"), KeyboardButton(text="74-dars"), KeyboardButton(text="75-dars")],
        [KeyboardButton(text="76-dars"), KeyboardButton(text="77-dars"), KeyboardButton(text="78-dars")],
        [KeyboardButton(text="79-dars"), KeyboardButton(text="80-dars"),KeyboardButton(text="Ortga <-")] 
            

        
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
