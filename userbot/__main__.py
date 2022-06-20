# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# ReCode by @Daijobu69

""" Userbot start point """

import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from pytgcalls import idle
from telethon import version
from telethon.tl.alltlobjects import LAYER
from userbot import BOTLOG_CHATID, BOT_TOKEN, LOOP
from userbot.clients import pocong_userbot_on, multigojo
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES
from userbot.utils import GojoDB, HOSTED_ON, autobot, autopilot, gojo_version

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"userbot.modules.{module_name}")
    adB = GojoDB()
    client = multigojo()
    total = 10 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
    LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")
    LOGS.info(f"Userbot Version - {ubotversion} •[{adB.name}]•")
    LOGS.info(f"Gojo Version - {gojo_version} •[{HOSTED_ON}]•")
    LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(pocong_userbot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
