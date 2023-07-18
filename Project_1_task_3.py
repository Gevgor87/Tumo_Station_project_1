# 1.Please install and activate venv(virtual environment). Steps below (write in terminal)
#       python3 -m venv venv
#       .\venv\Scripts\activate         for windows
#       source ./venv/bin/activate      for Mac or Linux
# 2.Install aiogram library
#       pip install aiogram
# 3.In config.py file input Token(get from BotFather in Telegram). config.py must be in the same directory


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

#-------------------------------------------------------------------
#                       Create bot and dispecher
#-------------------------------------------------------------------
bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#-------------------------------------------------------------------
#                       start message in terminal
#-------------------------------------------------------------------
async def start_up(_):
    print("Bot is online")

#-------------------------------------------------------------------
#                       Buttons
#-------------------------------------------------------------------
new_button = ReplyKeyboardMarkup([
    [KeyboardButton(text="/New_text")]
], resize_keyboard=True)

cancel_button = ReplyKeyboardMarkup([
    [KeyboardButton(text="/Cancel")]
], resize_keyboard=True)


#-------------------------------------------------------------------
#                       States
#-------------------------------------------------------------------
class NewtextStatesGroup(StatesGroup):
    name = State()
    adjective_1 = State()
    color_1 = State()
    animal_1 = State()
    place_1 = State()
    adjective_2 = State()
    magical_creature_1 = State()
    adjective_3 = State()
    magical_creature_2 = State()
    room = State()
    noun_1 = State()
    noun_2 = State()
    noun_3 = State()
    adjective_4 = State()
    noun_4 = State()
    number = State()
    meas_time = State()
    verb = State()
    adjective_5 = State()
    noun_5 = State()

#-------------------------------------------------------------------
#                       Bot Body
#-------------------------------------------------------------------
@dp.message_handler(commands=['start', 'help'])
async def start_cmd(message:types.Message):
    await message.answer(f"Hello {message.from_user.first_name}) Nice to meet you! To start creating text please tap on button /New_text 👇", reply_markup=new_button)
    await message.delete()

@dp.message_handler(commands=["Cancel"], state="*")
async def cancel_cmd(msg:types.Message, state:FSMContext):
    await msg.delete()
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id-1)
    await state.finish()
    await bot.send_message(chat_id=msg.from_user.id, text="To start creating text please tap on button /New_text 👇", reply_markup=new_button)
    await bot.delete_message(chat_id=msg.from_user.id, message_id=id_for_del)

@dp.message_handler(commands=["New_text"])
async def new_cmd(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="To cancel creating press /Cancel", reply_markup=cancel_button)
    global id_for_del
    id_for_del = message.message_id + 1
    await bot.send_message(chat_id=message.from_user.id, text="Please input Person’s Name")
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.name.set()
    await message.delete()


@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.name)
async def pers_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["pers_name"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Ok! Please input adjective")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.adjective_1)
async def adject_1(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["adjective_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input color")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.color_1)
async def color_1(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["color_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input animal")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.animal_1)
async def animal_1(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["animal_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input place")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.place_1)
async def place_1(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["place_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input adjective")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.adjective_2)
async def adject_2(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["adjective_2"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input Magical Creature(plural)")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.magical_creature_1)
async def meg_creature(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["magical_creature_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input adjective")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.adjective_3)
async def adject_3(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["adjective_3"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input Magical Creature(plural)")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.magical_creature_2)
async def meg_creature(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["magical_creature_2"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input Room in a House")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.room)
async def room(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["room"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input noun")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.noun_1)
async def noun_1(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["noun_1"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input one more noun")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.noun_2)
async def noun_2(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["noun_2"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input noun(plural)")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.noun_3)
async def noun_3(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["noun_3"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input adjective")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.adjective_4)
async def adject_4(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["adjective_4"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input noun(plural)")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.noun_4)
async def noun_4(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["noun_4"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input number")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.number)
async def number(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["number"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input Measure of time")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.meas_time)
async def meas_time(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["meas_time"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input verb(ending in ing)")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.verb)
async def verb(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["verb"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input adjective")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.adjective_5)
async def adjective_5(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["adjective_5"] = message.text
    await bot.send_message(chat_id=message.from_user.id, text="Please input noun")
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await NewtextStatesGroup.next()

@dp.message_handler(content_types=["text"], state=NewtextStatesGroup.noun_5)
async def noun_5(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["noun_5"] = message.text
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id-1)
    await bot.delete_message(chat_id=message.from_user.id, message_id=id_for_del)
    await bot.send_message(chat_id=message.from_user.id, text=f"Dear {data['pers_name']}, I am writing to you from a {data['adjective_1']}\
 castle in an enchanted forest. I found myself here one day after going for a ride on a\
 {data['color_1']} {data['animal_1']} in {data['place_1']}. There are {data['adjective_2']} {data['magical_creature_1']} and {data['adjective_3']} \
{data['magical_creature_2']} here! In the {data['room']} there is a pool full of {data['noun_1']}. \
I fall asleep each night on a {data['noun_2']} of {data['noun_3']} and dream of {data['adjective_4']} \
{data['noun_4']}. It feels as though I have lived here for {data['number']} {data['meas_time']}. \
I hope one day you can visit, although the only way to get here now is {data['verb']} on a \
{data['adjective_5']} {data['noun_5']}!!")
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text="To start creating new text please tap on button /New_text 👇", reply_markup=new_button)


#-------------------------------------------------------------------
#                       Run
#-------------------------------------------------------------------
if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=start_up)
    