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
           KeyboardButton(text = "âšī¸ Biz haqimizda"),
           KeyboardButton(text = "đ Kontakt"),
            
        ],
        [
           KeyboardButton(text = "đ Biz bilan bog'lanish"), 
        ],
    ],
    resize_keyboard=True
)