from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from database.database import Database


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
database = Database(
    Path(__file__).parent / "db1.sqlite3"
)