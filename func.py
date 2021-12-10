from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
from logger import logger
from telegram.error import BadRequest
from telegram.ext import updater

from sql_cons import *
import sqlite3
def start(update, context):
    user_id = update.effective_user.id
    f_name =update.effective_user.from_user.first_name


    connect = sqlite3.connect('nws.sqlite')
    cur = connect.cursor()


    stage_update = cur.execute(stage.format(user_id)).fetchall()

    cur.execute(first_insert.format(user_id,1))
    connect.commit()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    TG_ID = TG_ID[0][0]
    knopka_lang = [
            InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
            ]
    knopka_lang1 = [
            InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz')
            ]
    context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni taglang:',
                              reply_markup=InlineKeyboardMarkup([knopka_lang,knopka_lang1]))





def next_func(update, context):
    global but01, but11, but151, but14, but13, but10, but12
    connect = sqlite3.connect('nws.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    message = update.message.text
    message = str(message)
    stage_ = stage_[0][0]
    lang_ = lang_[0][0]

    if message.lower() == 'davom etish➡️➡️➡️' and stage_ == 2 or  message ==dct[lang_][0] or stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2 or message == back[lang_][0] and stage_ == 3 :
       cur.execute(stagee.format('{}', user_id).format(3))
       connect.commit()

       but1 = [KeyboardButton(text=keydct[lang_][0])]
       but2 = [KeyboardButton(text=keydct[lang_][1])]
       but3 = [KeyboardButton(text=keydct[lang_][2])]
       but4 = [KeyboardButton(text=keydct[lang_][3])]
       context.bot.send_message(chat_id=user_id, text=dct[lang_][3] , reply_markup=ReplyKeyboardMarkup([but1,but2,but3,but4], resize_keyboard=True))


#111111111111111111111111111111111111111111111111111111

    if message == keydct[lang_][0] and stage_ == 3 or stage_ == 3.1 and message == back[lang_][0]:
        cur.execute(stagee.format('{}', user_id).format(3))
        connect.commit()
        but0 = [KeyboardButton(text= first_dct[lang_][0])]
        but1 = [KeyboardButton(text=first_dct[lang_][1])]
        but2 = [KeyboardButton(text= first_dct[lang_][2])]
        but3 = [KeyboardButton(text=first_dct[lang_][3])]
        but4 = [KeyboardButton(text=first_dct[lang_][4])]
        but5 = [KeyboardButton(text=first_dct[lang_][5])]
        but6 = [KeyboardButton(text=first_dct[lang_][6])]
        but7 = [KeyboardButton(text=first_dct[lang_][7])]
        but8 = [KeyboardButton(text=first_dct[lang_][8])]
        but9 = [KeyboardButton(text=first_dct[lang_][9])]
        but10 = [KeyboardButton(text=first_dct[lang_][10])]
        but11 = [KeyboardButton(text=first_dct[lang_][11])]
        but12 = [KeyboardButton(text=first_dct[lang_][12])]
        but13 = [KeyboardButton(text=first_dct[lang_][13])]
        but14 = [KeyboardButton(text=first_dct[lang_][14])]
        but15 = [KeyboardButton(text=back[lang_][0])]



        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but0,
                                                                   but1,
                                                                   but2,
                                                                   but3,
                                                                   but4,
                                                                   but5,
                                                                   but6,
                                                                   but7,
                                                                   but8,
                                                                   but9,
                                                                   but10,
                                                                   but11,
                                                                   but12,
                                                                   but13,
                                                                   but14,
                                                                   but15], resize_keyboard=True))


    #     SmSsmsmsmsmsmsmsmsm1111111111111111111111111111111
    if message == first_dct[lang_][0] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][0])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][1] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][1])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][2] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][2])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][3] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][3])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][4] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][4])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][5] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][5])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][6] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][6])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][7] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][7])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][8] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][8])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][9] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][9])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][10] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][10])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][11] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][11])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][12] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][12])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][13] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][13])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == first_dct[lang_][14] and stage_ == 3:
        cur.execute(stagee.format('{}', user_id).format(3.1))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=fdct[lang_][14])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))

    # 222222222222222222222222222222222222222222222222



    if message == keydct[lang_][1] and stage_ == 3 or stage_ == 3.21 and message == back[lang_][0] or stage_ == 3.22 and message == back[lang_][0] :
        cur.execute(stagee.format('{}', user_id).format(3))
        connect.commit()
        qwerty = [KeyboardButton(text=second_dct[lang_][0])]
        qwer =  [KeyboardButton(text=second_dct[lang_][1])]
        qwert = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                             reply_markup=ReplyKeyboardMarkup([qwerty,qwer, qwert], resize_keyboard=True))



    if message == second_dct[lang_][0] and stage_ ==3 or message == back[lang_][0] and stage_ ==3.211:
        cur.execute(stagee.format('{}', user_id).format(3.21))
        connect.commit()
        but0 = [KeyboardButton(text=second_dct[lang_][2])]
        but1 = [KeyboardButton(text=second_dct[lang_][3])]
        but2 = [KeyboardButton(text=second_dct[lang_][4])]
        but3 = [KeyboardButton(text=second_dct[lang_][5])]
        but4 = [KeyboardButton(text=second_dct[lang_][6])]
        but5 = [KeyboardButton(text=second_dct[lang_][7])]
        but6 = [KeyboardButton(text=second_dct[lang_][8])]
        but7 = [KeyboardButton(text=second_dct[lang_][9])]
        but8 = [KeyboardButton(text=second_dct[lang_][10])]
        but9 = [KeyboardButton(text=second_dct[lang_][11])]
        but10 = [KeyboardButton(text=second_dct[lang_][12])]
        but11 = [KeyboardButton(text=second_dct[lang_][13])]
        but12 = [KeyboardButton(text=second_dct[lang_][14])]
        but13 = [KeyboardButton(text=second_dct[lang_][15])]
        but14 = [KeyboardButton(text=second_dct[lang_][16])]
        but15 = [KeyboardButton(text=back[lang_][0])]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but0,
                                                                   but1,
                                                                   but2,
                                                                   but3,
                                                                   but4,
                                                                   but5,
                                                                   but6,
                                                                   but7,
                                                                   but8,
                                                                   but9,
                                                                   but10,
                                                                   but11,
                                                                   but12,
                                                                   but13,
                                                                   but14,
                                                                   but15], resize_keyboard=True))



        # !!!!!!!!!!! 2 knopani   1 knopkasini smslaaari!!!!
    if message == second_dct[lang_][2] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][0])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][3] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][1])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][4] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][2])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][5] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][3])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][6] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][4])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][7] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][5])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][8] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][6])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][9] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][7])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][10] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][8])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][11] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][9])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][12] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][10])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][13] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][11])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][14] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][12])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][15] and stage_ == 3.21:
        cur.execute(stagee.format('{}', user_id).format(3.211))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][13])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1tugadi


    if message == second_dct[lang_][1] and stage_ ==3 or message == back[lang_][0] and stage_ ==3.221:
        cur.execute(stagee.format('{}', user_id).format(3.22))
        connect.commit()
        but0 = [KeyboardButton(text=second_dct[lang_][17])]
        but1 = [KeyboardButton(text=second_dct[lang_][18])]
        but2 = [KeyboardButton(text=second_dct[lang_][19])]
        but3 = [KeyboardButton(text=second_dct[lang_][20])]
        but4 = [KeyboardButton(text=second_dct[lang_][21])]
        but5 = [KeyboardButton(text=second_dct[lang_][22])]
        but6 = [KeyboardButton(text=second_dct[lang_][23])]
        but7 = [KeyboardButton(text=second_dct[lang_][24])]
        but8 = [KeyboardButton(text=second_dct[lang_][25])]
        but9 = [KeyboardButton(text=second_dct[lang_][26])]
        but15 = [KeyboardButton(text=back[lang_][0])]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but0,
                                                                   but1,
                                                                   but2,
                                                                   but3,
                                                                   but4,
                                                                   but5,
                                                                   but6,
                                                                   but7,
                                                                   but8,
                                                                   but9,
                                                                   but15], resize_keyboard=True))



        # !!!!!!!!!!! 2 knopani   2 knopkasini smslaaari!!!!

    if message == second_dct[lang_][17] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][15])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][18] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][16])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][19] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][17])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][20] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][18])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][21] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][19])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][22] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][20])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][23] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][21])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][24] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][22])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][25] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][23])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
    if message == second_dct[lang_][26] and stage_ == 3.22:
        cur.execute(stagee.format('{}', user_id).format(3.221))
        connect.commit()

        context.bot.send_message(chat_id=user_id, text=sdct[lang_][24])


        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))
        # !!!!!!!!!!! 2 knopani   2 knopkasini smslaaari!!!!ТУГАДИ



    #3333333333333333333333333333333333333333333333333333333333333333333333333


    if message == keydct[lang_][2] and stage_ == 3:
        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text='⬇️',
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))

        web = [InlineKeyboardButton(text=dct[lang_][5], url='''http://nvs-railway.uz/ru''')]
        context.bot.send_message(chat_id=user_id, text='⬇️',
                                 reply_markup=InlineKeyboardMarkup([web]))


    # 4444444444444444444444444444444444444444444444444

    if message == keydct[lang_][3] and stage_ == 3:
        but15 = [KeyboardButton(text=back[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup([but15], resize_keyboard=True))

        web = [InlineKeyboardButton(text='1 ', url='''https://t.me/Medic_UTY'''),
               InlineKeyboardButton(text='2', url='''https://t.me/joinchat/REPdYVoA2pE3YjVi'''),
                InlineKeyboardButton(text='3', url='''https://t.me/joinchat/IO56bnf1u0BhZGYy''')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][6],
                                         reply_markup=InlineKeyboardMarkup([web]))

def ru(update, context):
    user_id = update.callback_query.from_user.id
    f_name = update.callback_query.from_user.first_name
    connect = sqlite3.connect('nws.sqlite')
    cur = connect.cursor()

    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    lang_ = lang_[0][0]

    k_but = [KeyboardButton(text='далее➡️➡️➡️')]
    context.bot.send_message(text=dct[lang_][2].format(f_name), chat_id=user_id, reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))

def uz(update, context):
    user_id = update.callback_query.from_user.id
    f_name = update.callback_query.from_user.first_name
    connect = sqlite3.connect('nws.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    lang_ = lang_[0][0]

    k_but = [KeyboardButton(text='davom etish➡️➡️➡️')]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(f_name),  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))




def error_callback(bot, update, error):
    try:
        raise error
    except BadRequest:
        # handle malformed requests - read more below!
        print('Same message')



def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    updater.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))

def error_callback(bot, update, error):
    try:
        raise error
    except BadRequest:
        # handle malformed requests - read more below!
        print('Same message')



def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    updater.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))
