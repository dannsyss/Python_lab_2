from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from readfile import rf

TOKEN_API = '5781119218:AAGF20L05kM8yBP3Tmn7WbH1e8RPCC5d-cU'

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
lists=rf()
len_list=len(lists)

number = 0
prvOtv=0

def get_inline_keyboard() -> InlineKeyboardMarkup:
        global number
        global lists
        list = []
        list = lists[number]    # ['vopros0','1','2','3','4']
        ikb = InlineKeyboardMarkup(row_width=4)
        b1 = InlineKeyboardButton(list[1][:-1:], callback_data=list[1])
        b2 = InlineKeyboardButton(list[2][:-1:], callback_data=list[2])
        b3 = InlineKeyboardButton(list[3][:-1:], callback_data=list[3])
        b4 = InlineKeyboardButton(list[4][:-1:], callback_data=list[4])
        ikb.add(b1, b2, b3, b4)

        return ikb

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
        await message.answer(lists[number][0],
                             reply_markup=get_inline_keyboard())


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
        global number
        global prvOtv
        otv=callback.data
        if otv[-1]=='1':
                prvOtv+=1
                await callback.answer('Правильно')
        else:
                await callback.answer('Не правильно')
        if number == len_list-1:
                str=f"""<em>Пройдено тестов</em>       -  <b>{number+1}</b>\n<em>Правильных ответов</em> - <b>{prvOtv}</b>"""
                await callback.message.answer(str,parse_mode='HTML')
                await callback.message.delete()
                number = 0
                prvOtv=0
        else:
                number += 1
                await callback.message.edit_text(lists[number][0], reply_markup=get_inline_keyboard())


if __name__ == "__main__":
        executor.start_polling(dispatcher=dp,
                               skip_updates=True)