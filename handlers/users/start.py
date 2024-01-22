from aiogram import Router, types
from aiogram.filters.command import CommandStart

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Hello! I'm a simple bot. Send me a message and I'll try to guess what it is."
    )
