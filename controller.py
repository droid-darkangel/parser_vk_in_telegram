from aiogram import Bot, Dispatcher, executor, types

from config import *
from parser_vk import Parser_vk_api , requests

bot = Bot(token=api_token)
dp = Dispatcher(bot)
parser = Parser_vk_api()
spy_user_id = 'vfangel'# указывай без '@' иначе KeyError это твой ник поставь другой ник который будешь мониторить

@dp.message_handler(commands=['help','помощь'])
async def help(message: types.Message):
    chat_id = message.chat.id

    text1 = help_text_en
    text2 = help_text_ru
    await bot.send_message(chat_id=chat_id , text=text1)
    await bot.send_message(chat_id=chat_id , text=text2)
    await bot.send_message(chat_id=chat_id , text='Не делай частых запросов \nиначе перестанет работать')


@dp.message_handler(commands=['start', 'старт'])
async def start_and_customizate(message: types.Message):
    global spy_user_id
    chat_id = message.chat.id

    delete_symbols = (' ','_','-')
    
    try:
        spy_user_id = message.text.split(' ')[1].strip()
    except IndexError:
        await bot.send_message(chat_id=chat_id , text='Введите после команды id пользователя вк')
    else:
        await bot.send_message(chat_id=chat_id , text=f'Теперь мониторим за {spy_user_id}')

    await message.delete()

@dp.message_handler(commands=['online','онлайн'])
async def is_online(message: types.Message):
    chat_id = message.chat.id
    
    info_online = int(parser.get_user_info(spy_user_id)['online'])
    
    if info_online:
        await bot.send_message(chat_id=chat_id , text='Пользователь в вк')
    else:
        await bot.send_message(chat_id=chat_id , text='Пользователь не в вк')
    
    await message.delete()

@dp.message_handler(commands=['count_of_friends', 'друзья'])
async def count_of_friends(message: types.Message):
    chat_id = message.chat.id

    count_of_friends = parser.get_user_info(spy_user_id)['counters']['friends']
    await bot.send_message(chat_id=chat_id , text=count_of_friends)
    await message.delete()

@dp.message_handler(commands=['counters','основное'])
async def counters(message: types.Message):
    chat_id = message.chat.id

    counters = parser.get_user_info(spy_user_id)['counters']
    keys = counters.keys()

    for key in keys:
        await bot.send_message(chat_id=chat_id , text=f'{key} : {counters[key]}')
    
    await message.delete()

@dp.message_handler(commands=['get_subscriptions','подписчики'])
async def get_count_of_subscriptions(message: types.Message):
    chat_id = message.chat.id

    subscriptions = parser.get_user_info(spy_user_id)['counters']['subscriptions']
    await bot.send_message(chat_id=chat_id , text=subscriptions)
    await message.delete()

@dp.message_handler(commands=['get_url','ссылка'])
async def get_url(message: types.Message):
    chat_id = message.chat.id

    url = r'https://m.vk.com/' + parser.get_user_info(spy_user_id)['domain']
    await bot.send_message(chat_id=chat_id , text=url)
    await message.delete()

@dp.message_handler(commands=['avatar','аватар'])
async def get_avatar(message: types.Message):
    chat_id = message.chat.id
     
    avatar_url = parser.get_user_info(spy_user_id)['photo_50']
    avatar = requests.get(avatar_url).content
    
    await bot.send_photo(chat_id=chat_id , photo=avatar)
    await message.delete()

@dp.message_handler(commands=['phonenumber','номер'])
async def get_url(message: types.Message):
    chat_id = message.chat.id
    
    try:
        contacts = parser.get_user_info(spy_user_id)['contacts']
    except KeyError:
        await bot.send_message(chat_id=chat_id , text='К сожалению контакты скрыты настройками приватности')
    else:
        await bot.send_message(chat_id=chat_id , text=contacts)
    await message.delete()

@dp.message_handler(commands=['status','статус'])
async def status(message: types.Message):
    chat_id = message.chat.id

    try:
       status = parser.get_user_info(spy_user_id)['status']
    except KeyError:
        await bot.send_message(chat_id=chat_id , text='К сожалению статус отсутсвует')
    else:
        await bot.send_message(chat_id=chat_id , text=status)
    await message.delete()

@dp.message_handler(commands=['names','имена'])
async def get_url(message: types.Message):
    chat_id = message.chat.id

    try:
       first_name = parser.get_user_info(spy_user_id)['first_name']
       last_name = parser.get_user_info(spy_user_id)['last_name']
    except KeyError:
        await bot.send_message(chat_id=chat_id , text='Произошла ошибка!')
    else:
        await bot.send_message(chat_id=chat_id , text=first_name + ' ' + last_name)

@dp.message_handler(commands=['mobile','устройство'])
async def is_online(message: types.Message):
    chat_id = message.chat.id
    
    info_mobile = int(parser.get_user_info(spy_user_id)['has_mobile'])
    info_online = int(parser.get_user_info(spy_user_id)['online'])
    
    if info_online:
        if info_mobile == 1:
            await bot.send_message(chat_id=chat_id , text='Пользователь в вк с телефона')
        elif info_mobile == 0:
            await bot.send_message(chat_id=chat_id , text='Пользователь в вк с компьютера')
    else:
        await bot.send_message(chat_id=chat_id , text='Пользователь не в вк')
    
    await message.delete()
