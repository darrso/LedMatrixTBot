from aiogram import types
from aiogram.types import InlineKeyboardButton

digital_screen = types.InlineKeyboardMarkup(row_width=8)

text_and_data = []
for i in range(8):
    for j in range(8):
        text_and_data.append(['⚪', f"{str(i)}_{str(j)}"])
text_and_data.append(['Готово✅', 'end'])
text_and_data.append(['Отмена❌', 'cancel'])

digital_screen_1 = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
digital_screen.add(*digital_screen_1)

text_and_data_2 = text_and_data
