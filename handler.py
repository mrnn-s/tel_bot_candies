from aiogram import types
from loader import dp

total = 100
new_game = False

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
   print('Вам пришло сообщение')
   await message.answer(f'{message.from_user.first_name}, hello')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
   await message.answer(f'Бог поможет\n/hi\n/start\n/help\n/new_game\n/set\n')

@dp.message_handler(commands=['new_game'])
async def mes_help(message: types.Message):
    global new_game
    new_game = True
    await message.answer(f'Начнем игру!')

# /set 200 -> чтобы обратиться к 200 мы делаем split() и обращаемся к элементу с индексом [1]
@dp.message_handler(commands=['set'])
async def mes_help(message: types.Message):
    global total
    global new_game
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            total = int(count)
            await message.answer(f'Теперь конфет в игре будет {count}')
        else:
            await message.answer(f'{message.from_user.first_name}, напиши цифрами')
    else:
        await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global new_game
    if new_game:
        if message.text.isdigit():
            total -= int(message.text)
            if total <= 0:
                await message.answer(f'Ура, {message.from_user.first_name} победил !!!')
                new_game = False
                total = 0
            else:
                await message.answer(f'{message.from_user.first_name} взяла {message.text} конфет. '
                                     f'На столе осталось {total} конфет. ')


