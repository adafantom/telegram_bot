import ptbot
import os
from pytimeparse import parse


TG_TOKEN = os.environ['TELEGRAM_TOKEN']
TG_CHAT_ID = os.environ['TG_CHAT_ID']


def reply(chat_id, user_message):
    secs_time = parse(user_message)
    message_id = bot.send_message(chat_id, "Запускаем таймер...")
    bot.create_countdown(secs_time, notify_progress, chat_id=chat_id, message_id=message_id, total_time=secs_time)
    bot.create_timer(secs_time, notify, chat_id=chat_id)


def notify(chat_id):
    bot.send_message(chat_id, "Время вышло!")


def notify_progress(secs_time, chat_id,  message_id, total_time):
    bot.update_message(chat_id, message_id, "Осталось {} секунд \n {}".format(secs_time, render_progressbar(total_time, total_time - secs_time)))
    

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()