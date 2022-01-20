from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Quron manolari"),
           KeyboardButton(text = "Namoz vaqtlari"),
            
        ],

        [
           KeyboardButton(text = "Qiblani aniqlash"),
           KeyboardButton(text = "Yaqin atrofdagi Masjidlar"),
            
        ],

        [
           KeyboardButton(text = "ℹ️ Biz haqimizda"),
           KeyboardButton(text = "📞 Kontakt"),
            
        ],
        [
           KeyboardButton(text = "📞 Biz bilan bog'lanish"), 
        ],
    ],
    resize_keyboard=True
)