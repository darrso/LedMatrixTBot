from aiogram import types, Dispatcher

from python.Buttons.pBttns_inline import digital_screen


async def start_command(message: types.Message):
    await message.answer("Для того, чтоб у вас не лагало, лучше нажимать ОТМЕНА или ГОТОВО после того, как "
                         "вы закончите редактирование.\n", reply_markup=digital_screen)


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
