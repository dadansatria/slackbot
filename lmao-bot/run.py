#!/usr/bin/env python
import sys
import logging
import logging.config

from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('Opo?')
    # react with thumb up emoji
    message.react('+1')

def test_bot_default_reply(driver):
    driver.send_direct_message('youdontunderstandthiscommand do you')
    driver.wait_for_bot_direct_message('.*You can ask me.*')


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
