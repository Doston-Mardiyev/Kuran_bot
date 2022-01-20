from subprocess import call
from tokenize import String
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Message, CallbackQuery
from keyboards import default
from aiogram.dispatcher import FSMContext
from keyboards.default.Main_menu import menu_uz 
from keyboards.inline.numbers_keyboard import number_key, authors
# from utils.db_api.api import res, res2, sura, oyat
from states.My_state import NewPost
import requests
from pprint import pprint as print

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalom alekum, {message.from_user.full_name}!\n ", reply_markup = menu_uz)


@dp.message_handler(text_contains = "Quron manolari")
async def aftor_book(message: Message):
    await message.answer(f"Mualifni tanlang", reply_markup= authors)

    # await message.answer(res2)

@dp.callback_query_handler(text_contains = "muhammad_sodiq")
async def msmy(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Surani kiriting")#, reply_markup=number_key)
   
    await call.answer(cache_time=60)
    await NewPost.Sura_state.set() 



@dp.callback_query_handler(text = "alauddin_mansur")
async def select_category(call: CallbackQuery):
    await call.answer(f"Surani kiriting", reply_markup=number_key)
    
    # author_state = message.text
    # await state.update_data(author_state=author_state)
    # await NewPost.next()
    await call.answer(cache_time=60)



# @dp.message_handler(state=NewPost.Sura_state)
# async def sura_function(message: Message, state: FSMContext):
#     Sura_state = message.text
#     await state.update_data(Sura_state=Sura_state)
#     await message.answer("Oyatni kiriting:")
#     await NewPost.next()

@dp.message_handler(state=NewPost.Sura_state)
async def sura_function(call: CallbackQuery, state: FSMContext):
    Sura_state = call.data
    muhammad_sodiq = call.data

    await state.update_data(Oyat_state=Sura_state)
    
    async with state.proxy() as data: 
        Sura_state = data.get("Sura_state")
        muhammad_sodiq = data.get('muhammad_sodiq')
        # author_state = data.get("author_state")
        # Oyat_state = data.get("Oyat_state")
        # tafsir='uzb-muhammadsodikmu'
        url_oyat=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{muhammad_sodiq}/{Sura_state}.json"
        r = requests.get(url_oyat)
        res = r.json()
    await call.message.answer(res)    

    await state.finish()
