from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func import *

from tg_bot import LOAD, NO_LOAD, LOGGER
from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, DONATION_LINK, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(any(mod == module_name for module_name in all_modules) for mod in to_load):
                LOGGER.error("Invalid loadorder names. Quitting.")
                quit(1)

        else:
            to_load = all_modules

        if NO_LOAD:
            LOGGER.info("Not loading: {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_modules
ALL_MODULES = sorted(__list_all_modules())
LOGGER.info("Modules to load: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]




from cons import *
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(MessageHandler(Filters.text, next_func))

def main():
    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        upd.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)

        if CERT_PATH:
            upd.bot.set_webhook(url=URL + TOKEN,
                                    certificate=open(CERT_PATH, 'rb'))
        else:
            upd.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        upd.start_polling(timeout=15, read_latency=4)

    upd.idle()


if __name__ == 'main':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()

