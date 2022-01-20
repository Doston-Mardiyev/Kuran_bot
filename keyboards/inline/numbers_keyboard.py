from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



authors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Muhammad Sodiq Muhammad Yusuf", callback_data='muhammad_sodiq'),
            
        ],
        [
           InlineKeyboardButton(text = "Alauddin Mansour", callback_data='alauddin_mansur'),
            
        ],
       
    ],
   
)





number_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "1️⃣", callback_data='one'),
           InlineKeyboardButton(text = "2️⃣", callback_data='two'),
           InlineKeyboardButton(text = "3️⃣", callback_data='three'),

            
        ],
        [
           InlineKeyboardButton(text = "4️⃣", callback_data='four'),
           InlineKeyboardButton(text = "5️⃣", callback_data='five'),
           InlineKeyboardButton(text = "6️⃣", callback_data='six'),

            
        ],
        [
           InlineKeyboardButton(text = "7️⃣", callback_data='seven'),
           InlineKeyboardButton(text = "8️⃣", callback_data='eight'),
           InlineKeyboardButton(text = "9️⃣", callback_data='night'),

            
        ],
         [
           InlineKeyboardButton(text = "0️⃣", callback_data='zero'),
           InlineKeyboardButton(text = "⬅️", callback_data='back'),
            
        ],
    ],
   
)


