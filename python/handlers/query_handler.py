import time

from aiogram import types, Dispatcher
import serial
import sys
sys.path.append("python")
from Buttons.pBttns_inline import text_and_data_2
from config import aPort

arduino = serial.Serial(port=aPort, baudrate=9600, timeout=.1)


# LED BUTTONS
async def buttns_query(query: types.CallbackQuery):
    global text_and_data_2

    data = query.data.split('_')
    count = 0
    count_2 = 0

    for i in range(64):
        if ((data[0] == str(count_2)) and (data[1] == str(count))) and (text_and_data_2[i][0] == '🟡'):
            text_and_data_2[i] = (['⚪', f"{str(count_2)}_{str(count)}"])
        elif ((data[0] == str(count_2)) and (data[1] == str(count))) or (text_and_data_2[i][0] == '🟡'):
            text_and_data_2[i] = (['🟡', f"{str(count_2)}_{str(count)}"])
        else:
            text_and_data_2[i] = (['⚪', f"{str(count_2)}_{str(count)}"])
        count += 1
        if count == 8:
            count = 0
            count_2 += 1
    digital_screen_2 = types.InlineKeyboardMarkup(row_width=8)
    digital_screen_3 = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data_2)
    digital_screen_2.add(*digital_screen_3)

    try:
        await query.message.edit_reply_markup(reply_markup=digital_screen_2)
    finally:
        pass


# CANCEL BUTTON
async def cancel_func(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('Отменено!')

    global text_and_data_2
    text_and_data_2 = []
    for i in range(8):
        for j in range(8):
            text_and_data_2.append(['⚪', f"{str(i)}_{str(j)}"])
    text_and_data_2.append(['Готово✅', 'end'])
    text_and_data_2.append(['Отмена❌', 'cancel'])


# READY BUTTON
async def end_func(query: types.CallbackQuery):
    global text_and_data_2
    text_and_data_3 = []

    count = 0
    count_2 = 0
    for i in range(64):
        if i % 8 == 0:
            text_and_data_3.append('')
        if text_and_data_2[i][0] == '🟡':
            text_and_data_3[count_2] += '1'
        else:
            text_and_data_3[count_2] += '0'

        count += 1
        if count == 8:
            count = 0
            count_2 += 1

    await query.message.delete_reply_markup()
    await query.message.edit_text('Готово!')

    for i in range(8):
        print(text_and_data_3[i])
        arduino.write(str(int(text_and_data_3[i], 2)).encode())
        print(arduino.readall())

    text_and_data_2 = []
    for i in range(8):
        for j in range(8):
            text_and_data_2.append(['⚪', f"{str(i)}_{str(j)}"])
    text_and_data_2.append(['Готово✅', 'end'])
    text_and_data_2.append(['Отмена❌', 'cancel'])


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(buttns_query, text=[f'{str(i)}_{str(j)}' for i in range(8) for j in range(8)])
    dp.register_callback_query_handler(cancel_func, text='cancel')
    dp.register_callback_query_handler(end_func, text='end')
