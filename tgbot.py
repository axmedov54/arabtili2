import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message,KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils import executor
import random


from config import BOT_TOKEN as token
from button import menyu,oqish,quran,Aljomiy



bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menyu)




@dp.message(F.text=='Arab Harflari')
async def echo_handler(message: Message) -> None:
    await message.answer_photo(photo="https://t.me/arab_alifbosi_Tajvid_darslari/4",caption='Мазкур 28 ҳарфнинг барчаси ундош ҳарфлар ҳисобланиб, улар мабоний (ўзгармайдиган) ҳарфлар деб айтилади.', reply_markup=menyu)
    await message.answer_video(video="https://t.me/arab_tili_alifbosi/48", reply_markup=menyu)


@dp.message(F.text=='Kitoblar')
async def namoz2(message:Message):
  await message.answer(text='kitoblar',reply_markup=quran)

@dp.message(F.text=='Arab Harflari O`qilish')
async def namoz2(message:Message):
  await message.answer(text='Arab alifbosi',reply_markup=oqish)  



@dp.message(F.text=='XADISLAR')
async def namoz2(message:Message):
  await message.answer(text='Kitoblar',reply_markup=Aljomiy)

@dp.message(F.text=='''AL-JOMI'AS-SAHIH (1-jild)''')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/62',reply_markup=Aljomiy)

@dp.message(F.text=='''AL-JOMI'AS-SAHIH (2-jild)''')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/63',reply_markup=Aljomiy)


@dp.message(F.text=='''AL-JOMI'AS-SAHIH (3-jild)''')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/64',reply_markup=Aljomiy)

@dp.message(F.text=='''AL-JOMI'AS-SAHIH (4-jild)''')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/65',reply_markup=Aljomiy)    

@dp.message(F.text=='AL-QURAN')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/8',reply_markup=quran)

@dp.message(F.text=='MUALLIMA-SONIY')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/60',reply_markup=quran)


@dp.message(F.text=='ARABTILI-KITOBI')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/59',reply_markup=quran)


@dp.message(F.text=='ARABTILI-GRAMMATIKASI')
async def namoz2(message:Message):
  await message.answer_document(document='https://t.me/arabtilibotu/61',reply_markup=quran)    



@dp.message(F.text == '1-dars')
async def namoz1(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/9', reply_markup=oqish)

@dp.message(F.text == '2-dars')
async def namoz2(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/10', reply_markup=oqish)

@dp.message(F.text == '3-dars')
async def namoz3(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/11', reply_markup=oqish)

@dp.message(F.text == '4-dars')
async def namoz4(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/12', reply_markup=oqish)

@dp.message(F.text == '5-dars')
async def namoz5(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/13', reply_markup=oqish)

@dp.message(F.text == '6-dars')
async def namoz6(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/14', reply_markup=oqish)

@dp.message(F.text == '7-dars')
async def namoz7(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/15', reply_markup=oqish)

@dp.message(F.text == '8-dars')
async def namoz8(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/16', reply_markup=oqish)

@dp.message(F.text == '9-dars')
async def namoz9(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/17', reply_markup=oqish)

@dp.message(F.text == '10-dars')
async def namoz10(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/18', reply_markup=oqish)

@dp.message(F.text == '11-dars')
async def namoz11(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/19', reply_markup=oqish)

@dp.message(F.text == '12-dars')
async def namoz12(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/20', reply_markup=oqish)

@dp.message(F.text == '13-dars')
async def namoz13(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/21', reply_markup=oqish)

@dp.message(F.text == '14-dars')
async def namoz14(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/22', reply_markup=oqish)

@dp.message(F.text == '15-dars')
async def namoz15(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/23', reply_markup=oqish)

@dp.message(F.text == '16-dars')
async def namoz16(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/24', reply_markup=oqish)

@dp.message(F.text == '17-dars')
async def namoz17(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/25', reply_markup=oqish)

@dp.message(F.text == '18-dars')
async def namoz18(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/26', reply_markup=oqish)

@dp.message(F.text == '19-dars')
async def namoz19(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/27', reply_markup=oqish)

@dp.message(F.text == '20-dars')
async def namoz20(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/28', reply_markup=oqish)

@dp.message(F.text == '21-dars')
async def namoz21(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/29', reply_markup=oqish)

@dp.message(F.text == '22-dars')
async def namoz22(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/30', reply_markup=oqish)

@dp.message(F.text == '23-dars')
async def namoz23(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/31', reply_markup=oqish)

@dp.message(F.text == '24-dars')
async def namoz24(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/32', reply_markup=oqish)

@dp.message(F.text == '25-dars')
async def namoz25(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/33', reply_markup=oqish)

@dp.message(F.text == '26-dars')
async def namoz26(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/34', reply_markup=oqish)

@dp.message(F.text == '27-dars')
async def namoz27(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/35', reply_markup=oqish)

@dp.message(F.text == '28-dars')
async def namoz28(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/36', reply_markup=oqish)

@dp.message(F.text == '29-dars')
async def namoz29(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/37', reply_markup=oqish)

@dp.message(F.text == '30-dars')
async def namoz30(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/38', reply_markup=oqish)

@dp.message(F.text == '31-dars')
async def namoz31(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/39', reply_markup=oqish)

@dp.message(F.text == '32-dars')
async def namoz32(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/40', reply_markup=oqish)

@dp.message(F.text == '33-dars')
async def namoz33(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/41', reply_markup=oqish)

@dp.message(F.text == '34-dars')
async def namoz34(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/42', reply_markup=oqish)

@dp.message(F.text == '35-dars')
async def namoz35(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/43', reply_markup=oqish)

@dp.message(F.text == '36-dars')
async def namoz36(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/44', reply_markup=oqish)

@dp.message(F.text == '37-dars')
async def namoz37(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/45', reply_markup=oqish)

@dp.message(F.text == '38-dars')
async def namoz38(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/46', reply_markup=oqish)

@dp.message(F.text == '39-dars')
async def namoz39(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/47', reply_markup=oqish)

@dp.message(F.text == '40-dars')
async def namoz40(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/48', reply_markup=oqish)

@dp.message(F.text == '41-dars')
async def namoz41(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/49', reply_markup=oqish)

@dp.message(F.text == '42-dars')
async def namoz42(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/50', reply_markup=oqish)

@dp.message(F.text == '43-dars')
async def namoz43(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/51', reply_markup=oqish)

@dp.message(F.text == '44-dars')
async def namoz44(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/52', reply_markup=oqish)

@dp.message(F.text == '45-dars')
async def namoz45(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/53', reply_markup=oqish)

@dp.message(F.text == '46-dars')
async def namoz46(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/54', reply_markup=oqish)

@dp.message(F.text == '47-dars')
async def namoz47(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/55', reply_markup=oqish)

@dp.message(F.text == '48-dars')
async def namoz48(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/56', reply_markup=oqish)

@dp.message(F.text == '49-dars')
async def namoz49(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/57', reply_markup=oqish)

@dp.message(F.text == '50-dars')
async def namoz50(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/58', reply_markup=oqish)

@dp.message(F.text == '51-dars')
async def namoz51(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/66', reply_markup=oqish)

@dp.message(F.text == '52-dars')
async def namoz52(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/67', reply_markup=oqish)

@dp.message(F.text == '53-dars')
async def namoz53(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/68', reply_markup=oqish)

@dp.message(F.text == '54-dars')
async def namoz54(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/69', reply_markup=oqish)

@dp.message(F.text == '55-dars')
async def namoz55(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/70', reply_markup=oqish)

@dp.message(F.text == '56-dars')
async def namoz56(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/71', reply_markup=oqish)

@dp.message(F.text == '57-dars')
async def namoz57(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/72', reply_markup=oqish)

@dp.message(F.text == '58-dars')
async def namoz58(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/73', reply_markup=oqish)

@dp.message(F.text == '59-dars')
async def namoz59(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/74', reply_markup=oqish)

@dp.message(F.text == '60-dars')
async def namoz60(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/75', reply_markup=oqish)

@dp.message(F.text == '61-dars')
async def namoz61(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/76', reply_markup=oqish)

@dp.message(F.text == '62-dars')
async def namoz62(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/77', reply_markup=oqish)

@dp.message(F.text == '63-dars')
async def namoz63(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/78', reply_markup=oqish)

@dp.message(F.text == '64-dars')
async def namoz64(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/79', reply_markup=oqish)

@dp.message(F.text == '65-dars')
async def namoz65(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/80', reply_markup=oqish)

@dp.message(F.text == '66-dars')
async def namoz66(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/81', reply_markup=oqish)

@dp.message(F.text == '67-dars')
async def namoz67(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/82', reply_markup=oqish)

@dp.message(F.text == '68-dars')
async def namoz68(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/83', reply_markup=oqish)

@dp.message(F.text == '69-dars')
async def namoz69(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/84', reply_markup=oqish)

@dp.message(F.text == '70-dars')
async def namoz70(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/85', reply_markup=oqish)

@dp.message(F.text == '71-dars')
async def namoz71(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/86', reply_markup=oqish)

@dp.message(F.text == '72-dars')
async def namoz72(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/87', reply_markup=oqish)

@dp.message(F.text == '73-dars')
async def namoz73(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/88', reply_markup=oqish)


@dp.message(F.text == '75-dars')
async def namoz75(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/89', reply_markup=oqish)

@dp.message(F.text == '76-dars')
async def namoz76(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/90', reply_markup=oqish)

@dp.message(F.text == '77-dars')
async def namoz77(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/91', reply_markup=oqish)

@dp.message(F.text == '78-dars')
async def namoz78(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/92', reply_markup=oqish)

@dp.message(F.text == '79-dars')
async def namoz79(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/93', reply_markup=oqish)

@dp.message(F.text == '80-dars')
async def namoz80(message: Message):
    await message.answer_video(video='https://t.me/arabtilibotu/94', reply_markup=oqish)    

@dp.message(F.text == 'Ortga <-')
async def namoz50(message: Message):
    await message.answer(text='Assasiy Menyu', reply_markup=menyu)  

@dp.message(F.text == 'chiqish <-')
async def namoz50(message: Message):
    await message.answer(text='Kitoblar', reply_markup=quran)     

@dp.message(F.text == 'Chiqish <-')
async def namoz50(message: Message):
    await message.answer(text='Assosiy Menyu', reply_markup=menyu) 


lugatlar = [
    "Ota", "أب", "Ab",
    "Ona", "أم", "Um",
    "Aka", "أخ", "Akh",
    "Opa", "أخت", "Ukht",
    "Bola", "طفل", "Tifl",
    "Uy", "بيت", "Bayt",
    "Maktab", "مدرسة", "Madrasa",
    "Kitob", "كتاب", "Kitab",
    "Qalam", "قلم", "Qalam",
    "Stol", "طاولة", "Tawila",
    "Stul", "كرسي", "Kursi",
    "Deraza", "نافذة", "Nafiza",
    "Eshik", "باب", "Bab",
    "Yoz", "صيف", "Sayf",
    "Qish", "شتاء", "Shita'",
    "Bahor", "ربيع", "Rabi'",
    "Kuz", "خريف", "Kharif",
    "Daraxt", "شجرة", "Shajara",
    "Gull", "زهرة", "Zahra",
    "Suv", "ماء", "Ma'",
    "Non", "خبز", "Khobz",
    "Go'sht", "لحم", "Lahm",
    "Sut", "حليب", "Halib",
    "Choy", "شاي", "Shay",
    "Meva", "فاكهة", "Fakiha",
    "Sabzavot", "خضروات", "Khudrawat",
    "Mahalla", "حي", "Hayy",
    "Shaharcha", "مدينة", "Madina",
    "Do'st", "صديق", "Sadiq",
    "Yordam", "مساعدة", "Musa'ada",
    "Ish", "عمل", "Amal",
    "Pul", "مال", "Mal",
    "Sog'liq", "صحة", "Sihha",
    "Sevgi", "حب", "Hubb",
    "Oq", "أبيض", "Abyad",
    "Qora", "أسود", "Aswad",
    "Qizil", "أحمر", "Ahmar",
    "Yashil", "أخضر", "Akhzar",
    "Moviy", "أزرق", "Azraq",
    "Sariq", "أصفر", "Asfar",
    "Osmon", "سماء", "Sama'",
    "Quyosh", "شمس", "Shams",
    "Oy", "قمر", "Qamar",
    "Yulduz", "نجم", "Najm",
    "Mashina", "سيارة", "Sayyara",
    "Velosiped", "دراجة", "Daraja",
    "Avtobus", "حافلة", "Hafila",
    "Poyezd", "قطار", "Qitar",
    "Samolyot", "طائرة", "Tayara",
    "Oyoq", "قدم", "Qadam",
    "Qo'l", "يد", "Yad",
    "Bosh", "رأس", "Ra's",
    "Ko'z", "عين", "Ayn",
    "Quloq", "أذن", "Udhun",
    "Burun", "أنف", "Anf",
    "Og'iz", "فم", "Fam",
    "Yurak", "قلب", "Qalb",
    "Oshqozon", "معدة", "Mi'da",
    "Tish", "سن", "Sinn",
    "Soch", "شعر", "Sha'r",
    "Tungi", "ليل", "Layl",
    "Kunduz", "نهار", "Nahar",
    "Erta", "مبكر", "Mubakir",
    "Kech", "متأخر", "Muta'akhir",
    "Havo", "هواء", "Hawa'",
    "Yomg'ir", "مطر", "Matar",
    "Qor", "ثلج", "Thalj",
    "Shamol", "ريح", "Rih",
    "Tog'", "جبل", "Jabal",
    "Daryo", "نهر", "Nahr",
    "Ko'l", "بحيرة", "Buhayra",
    "Dengiz", "بحر", "Bahr",
    "Okean", "محيط", "Muhit",
    "Qo'ng'iroq", "جرس", "Jaras",
    "Xabar", "رسالة", "Rasala",
    "Rasm", "صورة", "Sura",
    "Musiqa", "موسيقى", "Musiqa",
    "Kino", "فيلم", "Film",
    "Kitobxona", "مكتبة", "Maktaba",
    "Muzey", "متحف", "Mathaf",
    "Stadion", "ملعب", "Mal'ab",
    "Do'kon", "متجر", "Matjar",
    "Bozor", "سوق", "Suq",
    "Tushlik", "غداء", "Ghada",
    "Kechki ovqat", "عشاء", "Asha",
    "Nonushta", "إفطار", "Iftar",
    "Osh", "بيلاف", "Pilaf",
    "Salat", "سلطة", "Salata",
    "Sho'rva", "حساء", "Hisau",
    "Pishloq", "جبن", "Jubn",
    "Yog'", "زيت", "Zayt",
    "Shakar", "سكر", "Sukkar",
    "Tuz", "ملح", "Milh",
    "Mavzu", "موضوع", "Mawdu'",
    "Savol", "سؤال", "Su'al",
    "Javob", "جواب", "Jawab",
    "To'g'ri", "صحيح", "Sahih",
    "Noto'g'ri", "خطأ", "Khata'",
    "Xato", "خطأ", "Khata'",
    "Yaxshi", "جيد", "Jayid"
]

# Lug'atlar tugmasi
button_dictionary = KeyboardButton('Lug`atlar')
markup = ReplyKeyboardMarkup().add(button_dictionary)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Tugmani bosing:", reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Lug`atlar')
async def send_random_dictionaries(message: types.Message):
    # Tasodifiy 20 ta lug'atni tanlash
    random_dictionaries = random.sample(lugatlar, 20)
   # Tanlangan lug'atlarni formatlash va jo'natish
    response = "\n".join(random_dictionaries)
    await message.reply(response)
 

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")
