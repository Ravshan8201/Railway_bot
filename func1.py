from logger import logger
from telegram.error import BadRequest
from telegram.ext import updater

from cons1 import *
from cons1 import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons1 import *
from sql_table_cons import *
import sqlite3
def start(update, context):
    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name


    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    name = cur.execute(name_select.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]
        name = name[0][0]
        lang_ = lang_[0][0]
    except Exception:
        pass



    if user_id != TG_ID:                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang]))
    else:
        pass

    if user_id == TG_ID and user_id != 572735440:
        backbu = [KeyboardButton(text=dct[lang_][16])]
        context.bot.send_message(text=dct[lang_][0].format(name), chat_id=user_id,
                                 reply_markup=ReplyKeyboardMarkup([backbu], resize_keyboard=True))
    else:
        pass
    if user_id == TG_ID and user_id ==572735440:
        admin_panel = [InlineKeyboardButton(text='Отчет', callback_data='xlsx'),
                       InlineKeyboardButton(text='Список пользователей', callback_data='user_list'),]
        admin_panel1 = [InlineKeyboardButton(text='удалить отчет', callback_data='delete_f')]
        context.bot.send_message(chat_id=user_id, text='Админ панель',reply_markup=InlineKeyboardMarkup([admin_panel, admin_panel1]))

    if user_id != TG_ID and user_id ==572735440:
        admin_panel = [InlineKeyboardButton(text='Отчет', callback_data='xlsx'),
                       InlineKeyboardButton(text='Список пользователей', callback_data='user_list'),]
        admin_panel1 = [InlineKeyboardButton(text='удалить отчет', callback_data='delete_f')]
        context.bot.send_message(chat_id=user_id, text='Админ панель',reply_markup=InlineKeyboardMarkup([admin_panel, admin_panel1]))

def next_func(update, context):
    connect = sqlite3.connect('user_list.sqlite')
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

    if message.lower() == 'davom etish>>>' and stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][0].format(f_name))

        _but = [KeyboardButton(text='далее>>>')]
        context.bot.send_message(text=dct[lang_][1], chat_id=user_id,
                                 reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                  one_time_keyboard=True))

        cur.execute(stagee.format('{}', user_id).format(3))
        connect.commit()
    else:
        pass
    if stage_ == 3:
        message1 = update.message.text
        cur.execute(upd_name.format(message1, user_id))
        connect.commit()

        cur.execute(stagee.format('{}', user_id).format(3.5))
        connect.commit()
    else:
        pass
    stag_ = cur.execute(stage.format(user_id)).fetchall()
    stag_ = stag_[0][0]

    if stag_==3.5:
        obl_but1 =[KeyboardButton(text=obldct[lang_][0]),
                   KeyboardButton(text=obldct[lang_][1])]
        obl_but2 =[KeyboardButton(text=obldct[lang_][2]),
                   KeyboardButton(text=obldct[lang_][3])]
        obl_but3 =[KeyboardButton(text=obldct[lang_][4]),
                   KeyboardButton(text=obldct[lang_][5])]
        obl_but4 =[KeyboardButton(text=obldct[lang_][6]),
                   KeyboardButton(text=obldct[lang_][7])]
        obl_but5 =[KeyboardButton(text=obldct[lang_][8]),
                   KeyboardButton(text=obldct[lang_][9])]
        obl_but6 =[KeyboardButton(text=obldct[lang_][10]),
                   KeyboardButton(text=obldct[lang_][11])]
        obl_but7 =[KeyboardButton(text=obldct[lang_][12]),
                   KeyboardButton(text=obldct[lang_][13])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':',
                                 reply_markup=ReplyKeyboardMarkup([obl_but1,
                                                                   obl_but2,
                                                                   obl_but3,
                                                                   obl_but4,
                                                                   obl_but5,
                                                                   obl_but6,
                                                                   obl_but7,], resize_keyboard=True, one_time_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(3.8))
        connect.commit()
    else:
        pass

    sta_ = cur.execute(stage.format(user_id)).fetchall()
    sta_ = sta_[0][0]
    name = cur.execute(name_select.format(user_id)).fetchall()
    name = name[0][0]
    if sta_ == 3.8 and message != name:
        cur.execute(place_upd.format('{}', user_id).format(message))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(4))
        connect.commit()
    else:
       pass

    st_ = cur.execute(stage.format(user_id)).fetchall()
    st_ = st_[0][0]

    if st_ == 4 :
        name = cur.execute(name_select.format(user_id)).fetchall()
        name = name[0][0]
        b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True,  one_time_keyboard=True))

        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
    else:
        pass
    tel_nomer = cur.execute(phone_select.format(user_id)).fetchall()
    tel_nomer = tel_nomer[0][0]
    if stage_ ==  5 and message == dct[lang_][16] and tel_nomer > 0 or stage_ ==  6.1 and message == dct[lang_][14] or stage_ ==  6.4 and message == dct[lang_][16] or message == dct[lang_][16] or stage_==555:

        main_button = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=dct[lang_][7])]
        main_button1 = [KeyboardButton(text=maindct[lang_][2]),
                        KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][16]+':',
                                 reply_markup=ReplyKeyboardMarkup([main_button,
                                                                   main_button1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
    else:
        pass
    if stage_ == 6 and message ==maindct[lang_][0] or 6.1<stage_<6.15 and message==dct[lang_][14]:
        cur.execute(stagee.format('{}', user_id).format(6.1))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][16]),
                    KeyboardButton(text=dct[lang_][7]),]
        servise_but1 = [KeyboardButton(text=uslugadct[lang_][0])]
        servise_but2 = [KeyboardButton(text=uslugadct[lang_][1])]
        servise_but3 = [KeyboardButton(text=uslugadct[lang_][2])]
        servise_but4 = [KeyboardButton(text=uslugadct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':',
                                 reply_markup=ReplyKeyboardMarkup([back_but,
                                                                   servise_but1,
                                                                   servise_but2,
                                                                   servise_but3,
                                                                   servise_but4], resize_keyboard=True))
    else:
        pass
    # UUUUUUUUUSSSSSSSSSLLLLLLUUUUGGGGGGIIIIIIIIIII
    if stage_ == 6.1 and message == uslugadct[lang_][0] or stage_ == 6.11 and  message== dct[lang_][14][1:]:
        cur.execute(stagee.format('{}', user_id).format(6.11))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][14]),
                    KeyboardButton(text=dct[lang_][7]),
                    KeyboardButton(text=dct[lang_][16])]
        keybut1 = [KeyboardButton(text=uslugadct[lang_][4])]
        keybut2 = [KeyboardButton(text=uslugadct[lang_][5])]
        keybut3 = [KeyboardButton(text=uslugadct[lang_][6])]
        keybut4 = [KeyboardButton(text=uslugadct[lang_][7])]
        keybut5 = [KeyboardButton(text=uslugadct[lang_][8])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':', reply_markup=ReplyKeyboardMarkup([back_but,
                                                                                                         keybut1,
                                                                                                         keybut2,
                                                                                                         keybut3,
                                                                                                         keybut4,
                                                                                                         keybut5,
                                                                                                         ], resize_keyboard=True))

    else:
        pass



    if stage_ == 6.1 and message == uslugadct[lang_][1] or stage_ == 6.12 and  message== dct[lang_][14][1:]:
        cur.execute(stagee.format('{}', user_id).format(6.12))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][14]),
                    KeyboardButton(text=dct[lang_][7]),
                    KeyboardButton(text=dct[lang_][16])]
        keybut1 = [KeyboardButton(text=uslugadct[lang_][9])]
        keybut2 = [KeyboardButton(text=uslugadct[lang_][10])]
        keybut3 = [KeyboardButton(text=uslugadct[lang_][11])]
        keybut4 = [KeyboardButton(text=uslugadct[lang_][12])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':', reply_markup=ReplyKeyboardMarkup([back_but,
                                                                                                         keybut1,
                                                                                                         keybut2,
                                                                                                         keybut3,
                                                                                                         keybut4,

                                                                                                         ], resize_keyboard=True))

    else:
        pass

    if stage_ == 6.1 and message == uslugadct[lang_][2] or stage_ == 6.13 and  message== dct[lang_][14][1:]:
        cur.execute(stagee.format('{}', user_id).format(6.13))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][14]),
                    KeyboardButton(text=dct[lang_][7]),
                    KeyboardButton(text=dct[lang_][16])]

        keybut1 = [KeyboardButton(text=uslugadct[lang_][13])]
        keybut2 = [KeyboardButton(text=uslugadct[lang_][14])]
        keybut3 = [KeyboardButton(text=uslugadct[lang_][15])]
        keybut4 = [KeyboardButton(text=uslugadct[lang_][16])]
        keybut5 = [KeyboardButton(text=uslugadct[lang_][17]),
                   KeyboardButton(text=uslugadct[lang_][18])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':', reply_markup=ReplyKeyboardMarkup([back_but,
                                                                                                         keybut1,
                                                                                                         keybut2,
                                                                                                         keybut3,
                                                                                                         keybut4,
                                                                                                         keybut5,
                                                                                                         ], resize_keyboard=True))
    else:
        pass


    if stage_ == 6.1 and message == uslugadct[lang_][3] or stage_ == 6.14 and message== dct[lang_][14][1:]:
        cur.execute(stagee.format('{}', user_id).format(6.14))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][14]),
                    KeyboardButton(text=dct[lang_][7]),
                    KeyboardButton(text=dct[lang_][16])]
        keybut1 = [KeyboardButton(text=uslugadct[lang_][19])]
        keybut2 = [KeyboardButton(text=uslugadct[lang_][20])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':', reply_markup=ReplyKeyboardMarkup([back_but,
                                                                                                         keybut1,
                                                                                                         keybut2,], resize_keyboard=True))
    else:
        pass

    # UUUUUUUUUSSSSSSSSSLLLLLLUUUUGGGGGGIIIIIIIIIII        TUUUGGGAAADIIII







# OOOBRAAAATNYAAA SVYYYAAAAAZZZZZ
    if stage_ == 6 and message == maindct[lang_][2]:
        cur.execute(stagee.format('{}', user_id).format(6.3))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][16])]
        o1 =[KeyboardButton(text=otzivdct[lang_][0])]
        o2 =[KeyboardButton(text=otzivdct[lang_][1])]
        o3 =[KeyboardButton(text=otzivdct[lang_][2])]
        o4 =[KeyboardButton(text=otzivdct[lang_][3])]
        o5 =[KeyboardButton(text=otzivdct[lang_][4])]


        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':',
                                 reply_markup=ReplyKeyboardMarkup([back_but,
                                                                   o1,
                                                                   o2,
                                                                   o3,
                                                                   o4,
                                                                   o5,
                                                                  ], resize_keyboard=True))
    else:
        pass
    tel_nomer = cur.execute(phone_select.format(user_id)).fetchall()
    tel_nomer = tel_nomer[0][0]
    town  = cur.execute(place_select.format(user_id)).fetchall()
    town = town[0][0]
    for d in otzivdct[lang_][:-1]:
        if message == d and stage_ == 6.3:
            context.bot.send_message(chat_id=-697834775,
                                     text='👤Имя: {}\n📞Номер телефона: {}\n🏙Город: {}\n\n'.format(
                                         name, tel_nomer, town  )+ 'О Т З Ы В: {}'.format(message))
            back = [KeyboardButton(text=dct[lang_][16])]
            context.bot.send_message(text=otzivdct[lang_][-1],chat_id=user_id,  reply_markup=ReplyKeyboardMarkup([back], resize_keyboard=True))

    # OOOBRAAAATNYAAA SVYYYAAAAAZZZZZ


# NNNNNNAAAAAASSSSSTTTTTTRRRRROOOOYYYYKKKKIIIIII

    if stage_ == 6 and message == maindct[lang_][3] :

           lang_but = [KeyboardButton(text=dct[lang_][9]),
                       KeyboardButton(text=dct[lang_][8]),
                       KeyboardButton(text=dct[lang_][10])]
           back_but  = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text=maindct[lang_][3] + ':',
                                    reply_markup=ReplyKeyboardMarkup([lang_but,back_but], resize_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
    else:
        pass

    if message == 'Til🇺🇿🇷🇺' and stage_ == 6.4 or message == 'Язык🇷🇺🇺🇿' and stage_ == 6.4:
           knopka_lang = [
               InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru_change')
           ]
           knopka_lang1 = [
               InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz_change')
           ]
           back_bu = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text='Выберите язык:', reply_markup=ReplyKeyboardMarkup([back_bu],  resize_keyboard=True))
           context.bot.send_message(chat_id=user_id, text='Tilni tagnlang:',
                                    reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1],))
    else:
        pass

    if message == '📞Номер телефона' and stage_ == 6.4 or message == 'Telefon nomer☎️' and stage_ == 6.4:
           num_ = cur.execute(phone_select.format(user_id)).fetchall()
           num_ = num_[0][0]
           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
           stage_41 = cur.execute(stage.format(user_id)).fetchall()
           stage_41 = stage_41[0][0]
           cur.execute(phone_upd.format(num_, user_id))
           connect.commit()

           if stage_41 == 6.4:
               b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]
               back_ = [KeyboardButton(text=dct[lang_][16])]
               context.bot.send_message(chat_id=user_id, text=dct[lang_][5].format(f_name),
                                        reply_markup=ReplyKeyboardMarkup([b,back_], resize_keyboard=True))
    else:
        pass
    if message == dct[lang_][8] and stage_ == 6.4:

        obl_bu1 = [KeyboardButton(text=obldct[lang_][0]),
                   KeyboardButton(text=obldct[lang_][1])]
        obl_bu2 = [KeyboardButton(text=obldct[lang_][2]),
                   KeyboardButton(text=obldct[lang_][3])]
        obl_bu3 = [KeyboardButton(text=obldct[lang_][4]),
                   KeyboardButton(text=obldct[lang_][5])]
        obl_bu4 = [KeyboardButton(text=obldct[lang_][6]),
                   KeyboardButton(text=obldct[lang_][7])]
        obl_bu5 = [KeyboardButton(text=obldct[lang_][8]),
                   KeyboardButton(text=obldct[lang_][9])]
        obl_bu6 = [KeyboardButton(text=obldct[lang_][10]),
                   KeyboardButton(text=obldct[lang_][11])]
        obl_bu7 = [KeyboardButton(text=obldct[lang_][12]),
                   KeyboardButton(text=obldct[lang_][13])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15]+':',
                                 reply_markup=ReplyKeyboardMarkup([obl_bu1,
                                                                   obl_bu2,
                                                                   obl_bu3,
                                                                   obl_bu4,
                                                                   obl_bu5,
                                                                   obl_bu6,
                                                                   obl_bu7,], resize_keyboard=True, one_time_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(6.45))
        connect.commit()
    else:
        pass

    sa_ = cur.execute(stage.format(user_id)).fetchall()
    sa_ = sa_[0][0]

    mesage = update.message.text
    if mesage != dct[lang_][8] and sa_ == 6.45:
        cur.execute(place_upd.format('{}', user_id).format(message))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][16])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][11], reply_markup=ReplyKeyboardMarkup([back_but,], resize_keyboard=True, ))
    else:
        pass


# NNNNNNAAAAAASSSSSTTTTTTRRRRROOOOYYYYKKKKIIIIII  TTUUGGAADDII

# ФУНКЦИИИИИИИ  ОТЕПРАВКА Админа
    name = cur.execute(name_select.format(user_id)).fetchall()
    name = name[0][0]
    tel_nomer = cur.execute(phone_select.format(user_id)).fetchall()
    tel_nomer = tel_nomer[0][0]
    town  = cur.execute(place_select.format(user_id)).fetchall()
    town = town[0][0]
    mesage = update.message.text
    s_ = cur.execute(stage.format(user_id)).fetchall()
    s_ = s_[0][0]

    for e in uslugadct[lang_][3:]:
        if  mesage == e and 6.1<stage_<6.15 :
            usluga = mesage
            cur.execute(ser_upd.format('{}',user_id).format(usluga))
            connect.commit()
            cost = cost_dct[lang_][usluga]
            back_but = [KeyboardButton(text=dct[lang_][14][1:]),
                       KeyboardButton(text=dct[lang_][16])]


            knopka_pod  =[ KeyboardButton(text=dct[lang_][13])]
            if lang_ == 1:
               context.bot.send_message(chat_id=user_id, text='👤Имя: {}\n📞Номер телефона: {}\n🏙Город: {}\n\n⚒Услуга: {}\n💵Стоимость: {}'.format(name,tel_nomer,town,usluga,cost),  reply_markup=ReplyKeyboardMarkup([knopka_pod,back_but], resize_keyboard=True))
            if lang_ == 2:
               context.bot.send_message(chat_id=user_id, text='👤Ismi: {}\n📞Telefon raqami: {}\n🏙Shahar: {}\n\n⚒Xizmat turi: {}\n💵Narxi: {}'.format(name,tel_nomer,town,usluga,cost),  reply_markup=ReplyKeyboardMarkup([knopka_pod,back_but], resize_keyboard=True))








# ФУНКЦИИИИИИИ  ОТЕПРАВКА Админа ТУГАДИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ
    zakaz = cur.execute(ser_select.format(user_id)).fetchall()
    zakaz = zakaz[0][0]
# KORZINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     STAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRTTTTTTTTTTTTTT
    if message == dct[lang_][13] and 6.1<stage_<6.15 :
        tg_ = cur.execute(tg_id_select.format(user_id)).fetchall()
        try:
            tg_ = tg_[0][0]

        except Exception:
            pass


        cur.execute(first_insert2.format(user_id, zakaz))
        connect.commit()
        back_but = [KeyboardButton(text=dct[lang_][14][1:]),
                    KeyboardButton(text=dct[lang_][7]),
                        KeyboardButton(text=dct[lang_][16])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][6],  reply_markup=ReplyKeyboardMarkup([back_but], resize_keyboard=True))

    if message==dct[lang_][7] and 6.09<stage_<6.15 or message == dct[lang_][7] and stage_ ==6 :
        connect = sqlite3.connect('user_list.sqlite')
        cur = connect.cursor()
        try:
               id = cur.execute('''
               SELECT ZAKAZ
               FROM korzina
               WHERE TG_ID ='{}'
               '''.format(user_id)).fetchall()
               q = ''
               w = 0

               g = []
               for e in id:
                   e = e[0]
                   w+=1
                   delete_but = KeyboardButton(text='❌'+str(e))
                   r = []
                   r.append(delete_but)
                   g.append(r)
                   q+=str(w)+'.'+str(e)+'\n'

               zakaz_but = [KeyboardButton(text=dct[lang_][17])]
               zakaz_but2 = [KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16]) ]
               g.insert(0,[KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16]) ])
               g.insert(0, [KeyboardButton(text=dct[lang_][17])])
               if lang_ == 1 and w !=0:
                   context.bot.send_message(chat_id=user_id, text='👤Имя: {}\n📞Номер телефона: {}\n🏙Город: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q,  reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               elif lang_ == 2 and w !=0:
                   context.bot.send_message(chat_id=user_id, text='👤Ismi: {}\n📞Telefon raqami: {}\n🏙Shahar: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q,  reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               else:
                   if lang_ == 1:

                       context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️')
                   if lang_ == 2:


                       context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''')
        except Exception:
            if lang_ == 1:
               context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️')
            if lang_ == 2:
                context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''')


    if message[0] == '❌':

        cur.execute("""
        DELETE  FROM korzina WHERE TG_ID = '{}' and ZAKAZ = '{}' 
        """.format( user_id, message[1:]))
        connect.commit()
        try:
               id = cur.execute('''
               SELECT ZAKAZ
               FROM korzina
               WHERE TG_ID ='{}'
               '''.format(user_id)).fetchall()
               q = ''
               w = 0

               g = []
               for e in id:
                   e = e[0]
                   w+=1
                   delete_but = KeyboardButton(text='❌'+str(e))
                   r = []
                   r.append(delete_but)
                   g.append(r)
                   q+=str(w)+'.'+str(e)+'\n'

               zakaz_but = [KeyboardButton(text=dct[lang_][17])]
               zakaz_but2 = [KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16]) ]
               g.insert(0,[KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16]) ])
               g.insert(0, [KeyboardButton(text=dct[lang_][17])])
               if lang_ == 1 and w !=0:
                   context.bot.send_message(chat_id=user_id, text='👤Имя: {}\n📞Номер телефона: {}\n🏙Город: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q,  reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               elif lang_ == 2 and w !=0:
                   context.bot.send_message(chat_id=user_id, text='👤Ismi: {}\n📞Telefon raqami: {}\n🏙Shahar: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q,  reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               else:
                   if lang_ == 1:
                       back_bu = [KeyboardButton(text=dct[lang_][16])]
                       context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️',
                                                reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))
                   if lang_ == 2:
                       back_bu = [KeyboardButton(text=dct[lang_][16])]
                       context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''',
                                                reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))

                       context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''')
        except Exception:
            if lang_ == 1:
               back_bu = [KeyboardButton(text=dct[lang_][16])]
               context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️', reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))
            if lang_ == 2:
                back_bu = [KeyboardButton(text=dct[lang_][16])]
                context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''', reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))


    if message==dct[lang_][17]:
        connect = sqlite3.connect('user_list.sqlite')
        cur = connect.cursor()

        id = cur.execute('''
        SELECT ZAKAZ
        FROM korzina
        WHERE TG_ID ='{}'
        '''.format(user_id)).fetchall()
        q = ''
        w = 0
        for e in id:
            e = e[0]
            cur.execute(first_insert5.format(user_id, str(e)))
            connect.commit()
            w+=1


            q+=str(w)+'.'+str(e)+'\n'


        if lang_ == 1:
            context.bot.send_message(chat_id=-697834775, text='👤Имя: {}\n📞Номер телефона: {}\n🏙Город: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q)

        if lang_ == 2:
            context.bot.send_message(chat_id=-697834775, text='👤Ismi: {}\n📞Telefon raqami: {}\n🏙Shahar: {}\n\n'.format(name,tel_nomer,town,)+dct[lang_][7][1:].upper()+'\n\n'+q)


        TG_ID = cur.execute(sel_id.format(user_id)).fetchall()
        try:
            TG_ID = TG_ID[0][0]
        except Exception:
            pass
        if TG_ID != user_id:
            cur.execute(first_insert3.format(user_id, lang_, name, tel_nomer, town, w))
            connect.commit()
        if TG_ID == user_id:
            f = cur.execute(s_select.format(user_id)).fetchall()
            f = f[0][0]

            f = f+w
            cur.execute(s_upd.format(f, user_id))
            connect.commit()
        cur.execute("""
        DELETE  FROM korzina WHERE TG_ID = '{}'
        """.format(user_id))
        connect.commit()
        if lang_ == 1:
            back_ = [KeyboardButton(text=dct[lang_][16])]
            context.bot.send_message(chat_id=user_id, text='Ваш заказ принят',  reply_markup=ReplyKeyboardMarkup([back_], resize_keyboard=True))
        if lang_ == 2:
            back_ = [KeyboardButton(text=dct[lang_][16])]
            context.bot.send_message(chat_id=user_id, text='Buyurtmangiz qabul qilindi',  reply_markup=ReplyKeyboardMarkup([back_], resize_keyboard=True))

# KORZINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     STAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRTTTTTTTTTTTTTT

# Udalit

    if message == dct[lang_][18]:
        cur.execute("""
        DELETE  FROM korzina WHERE TG_ID = '{}'
        """.format(user_id))
        connect.commit()
        back = [KeyboardButton(text=dct[lang_][16])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][11],  reply_markup=ReplyKeyboardMarkup([back], resize_keyboard=True))



# Udalit

def ru_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k2_but = [KeyboardButton(text='🏠Главное меню')]
    context.bot.send_message(chat_id=user_id, text='🏠Нажмите на кнопку Главное меню...',
                             reply_markup=ReplyKeyboardMarkup([k2_but], resize_keyboard=True))
def uz_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k1_but = [KeyboardButton(text='🏠Asosiy menyu')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k1_but], resize_keyboard=True))
def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...' , chat_id=user_id,  reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('user_list.sqlite')
    cur = conn.cursor()
    cur.execute(phone_upd.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()

    name = cur.execute(name_select.format(user_id)).fetchall()
    town  = cur.execute(place_select.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()
    name=name[0][0]
    town = town[0][0]
    lang_ = lang_[0][0]
    cur.execute(first_insert4.format(user_id, lang_, name, num, town))
    conn.commit()
    main_button = [KeyboardButton(text=maindct[lang_][0]),
                   KeyboardButton(text=dct[lang_][7])]
    main_button1 = [KeyboardButton(text=maindct[lang_][2]),
                    KeyboardButton(text=maindct[lang_][3])]

    context.bot.send_message(chat_id=user_id, text=dct[lang_][16]+':',
                             reply_markup=ReplyKeyboardMarkup([main_button,
                                                               main_button1], resize_keyboard=True))

def podver(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    name = cur.execute(name_select.format(user_id)).fetchall()
    tel_nomer = cur.execute(phone_select.format(user_id)).fetchall()
    town  = cur.execute(place_select.format(user_id)).fetchall()
    s_ = cur.execute(stage.format(user_id)).fetchall()
    usluga = cur.execute(ser_select.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    lang_ = lang_[0][0]
    usluga = usluga[0][0]
    s_ = s_[0][0]
    town = town[0][0]
    tel_nomer = tel_nomer[0][0]
    name = name[0][0]
    connect.commit()
    cost = cost_dct[lang_][usluga]
    if user_id ==957531477:
        cur.execute(s_s_upd.format('{}', user_id).format(2))
        connect.commit()
    if 6.1<s_<6.15 and user_id!=957531477:
            adm_pod_but =[

                           InlineKeyboardButton(text=dct[lang_][12], callback_data='podver')
                         ]

            context.bot.send_message(chat_id=-697834775, text='Имя: {}\nНомер телефона: {}\nГород: {}\n\nУслуна: {}\nСтоимость: {}'.format(name,tel_nomer,town,usluga,cost),  reply_markup=InlineKeyboardMarkup([adm_pod_but],))





def xlsx(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    import xlsxwriter
    import pandas as pd
    import xlsxwriter
    try:
        workbook = xlsxwriter.Workbook('user_exel_list.xlsx')
        worksheet = workbook.add_worksheet()
        ids = cur.execute('''
                    SELECT TG_ID
                    FROM ADM
                    WHERE TG_ID !=0
                    ''').fetchall()
        nam = cur.execute('''
                    SELECT F_name
                    FROM ADM
                    ''').fetchall()
        te = cur.execute('''
                    SELECT Pho_num
                    FROM ADM
                    ''').fetchall()
        town = cur.execute('''
                    SELECT Place
                    FROM ADM
                    ''').fetchall()
        lang = cur.execute('''
                    SELECT Lang
                    FROM ADM
                    ''').fetchall()

        usluga = cur.execute('''
                    SELECT Ser_Stage
                    FROM ADM
                    ''').fetchall()
        dd = []
        for e in ids:
            e=e[0]

            list_usl = cur.execute('''SELECT USLUG FROM L_TABLE  WHERE TG_ID = '{}' '''.format(e)).fetchall()
            dd.append(list_usl)


        id = []
        name = []
        tel=[]
        tow = []
        lan = []
        uslug = []
        for i in range(len(ids)):
            id.append(ids[i][0])

            name.append(nam[i][0])
            tel.append(te[i][0])
            lan.append(lang[i][0])
            tow.append(town[i][0])
            uslug.append(usluga[i][0])

        df = pd.DataFrame({'TG_ID': id,
                           'NAME?': name,
                           'TOWN': tow,
                           'LANG': lan,
                           'TEL_NUM': tel,
                           'Количество заказов': uslug,
                           'Заказанные услуги': dd})
        df.to_excel('user_exel_list.xlsx', sheet_name='Result', index=False)
        context.bot.send_document(document=open('user_exel_list.xlsx', 'rb'),filename='user_exel_list.xlsx', caption='Отчет', chat_id=user_id)
    except Exception:
        context.bot.send_message(chat_id=user_id, text='Что-то пошло не так или таблица пустая)))')

def delete_f(update,context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute('''DELETE  FROM ADM''')
    cur.execute('''DELETE FROM L_TABLE''')
    connect.commit()
    context.bot.send_message(chat_id=user_id, text='отчет удален')

def user_list(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    import pandas as pd
    import xlsxwriter
    try:
        workbook = xlsxwriter.Workbook('user_exel_list.xlsx')
        worksheet = workbook.add_worksheet()
        ids = cur.execute('''
                            SELECT TG_ID
                            FROM COMMON
                            WHERE TG_ID !=0
                            ''').fetchall()
        nam = cur.execute('''
                            SELECT F_name
                            FROM COMMON
                            ''').fetchall()
        te = cur.execute('''
                            SELECT Pho_num
                            FROM COMMON
                            ''').fetchall()
        town = cur.execute('''
                            SELECT Place
                            FROM COMMON
                            ''').fetchall()
        lang = cur.execute('''
                            SELECT Lang
                            FROM COMMON
                            ''').fetchall()

        id = []
        name = []
        tel = []
        tow = []
        lan = []

        for i in range(len(ids)):
            id.append(ids[i][0])

            name.append(nam[i][0])

            tel.append(te[i][0])
            lan.append(lang[i][0])
            tow.append(town[i][0])

        df = pd.DataFrame({'TG_ID': id,
                           'NAME?': name,
                           'TOWN': tow,
                           'LANG': lan,
                           'TEL_NUM': tel,})
        df.to_excel('user_exel_list.xlsx', sheet_name='Result', index=False)
        context.bot.send_document(document=open('user_exel_list.xlsx', 'rb'), filename='user_exel_list.xlsx',caption='Список пользователей', chat_id=user_id)

    except Exception:
        context.bot.send_message(chat_id=user_id, text='что-пошло не так')

def adm(update, context):
    user_id = update.message.chat_id
    if user_id ==572735440 or user_id ==957531477:
            text = update.message.caption
            photo_id = update.message.photo[-1].file_id
            file = context.bot.getFile(photo_id)
            file.download('Picture.jpeg')
            if text == None:
                pass
            else:
                try:
                    connect = sqlite3.connect('user_list.sqlite')
                    cur = connect.cursor()
                    id = cur.execute('''
                    SELECT TG_ID
                    FROM Users
                    WHERE TG_ID !=0
                    ''').fetchall()
                    for e in id:
                        e = e[0]
                        context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=e, caption=text)
                        sleep(1.5)
                except Exception:

                     pass



def adm_v(update, context):
    user_id = update.message.chat_id
    if user_id ==572735440 or user_id ==957531477:
            text = update.message.caption
            photo_id = update.message.video.file_id
            file = context.bot.getFile(photo_id)
            file.download('Picture.mp4')
            if text == None:
                pass
            else:
                try:
                    connect = sqlite3.connect('user_list.sqlite')
                    cur = connect.cursor()
                    id = cur.execute('''
                SELECT TG_ID
                FROM Users
                WHERE TG_ID !=0
                ''').fetchall()
                    for e in id:
                        e = e[0]
                        context.bot.send_video(video=open('Picture.mp4', 'rb'), chat_id=e, caption=text)
                        sleep(1.5)
                except Exception:

                     pass
 
    
        # handle malformed requests - read more below!
        
