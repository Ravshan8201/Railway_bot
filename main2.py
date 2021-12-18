from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func2 import *
from cons2 import *
upd = Updater(token=TOKE, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='admin', callback=admin))
dis.add_handler(CallbackQueryHandler(pattern='aksiya_tamom', callback=aksiya_tamom))
dis.add_handler(CallbackQueryHandler(pattern='sov', callback=sov))
dis.add_handler(CallbackQueryHandler(pattern='pro_num', callback=pro_num))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
dis.add_handler(MessageHandler(Filters.photo, adm))
dis.add_handler(MessageHandler(Filters.video, adm_v))
def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    upd.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))
upd.start_polling(drop_pending_updates=True)
