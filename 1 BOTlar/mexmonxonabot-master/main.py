from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handler import chat
from aiogram import executor
from aiogram import types
from config import Token

storage:MemoryStorage = MemoryStorage()

bot = Bot(token=Token)
dp = Dispatcher(bot=bot, storage=storage)

chat.register(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
