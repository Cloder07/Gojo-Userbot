# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from userbot import BOT_TOKEN
from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    GOJO2,
    GOJO3,
    GOJO4,
    GOJO5,
    GOJO6,
    GOJO7,
    GOJO8,
    GOJO9,
    GOJO10,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    STRING_SESSION,
    blacklist,
    bot,
    call_py,
    tgbot,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nGojo-UserBot v{}, Copyright © 2021-2022 Gojo-Userboy• <https://github.com/Cloder07>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nGojo-UserBot v{}, Copyright © 2021-2022 Gojo-Userbot• <https://github.com/Cloder07>"


async def gojo_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multigojo():
    if 1972848319 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001681101717 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1972848319 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(gojo_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            GOJO2.start()
            LOOP.run_until_complete(gojo_client(GOJO2))
            user = GOJO2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            GOJO3.start()
            LOOP.run_until_complete(gojo_client(GOJO3))
            user = GOJO3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            GOJO4.start()
            LOOP.run_until_complete(gojo_client(GOJO4))
            user = GOJO4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            GOJO5.start()
            LOOP.run_until_complete(gojo_client(GOJO5))
            user = GOJO5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_6:
        try:
            GOJO6.start()
            LOOP.run_until_complete(gojo_client(GOJO6))
            user = GOJO6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            GOJO7.start()
            LOOP.run_until_complete(gojo_client(GOJO7))
            user = GOJO7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            GOJO8.start()
            LOOP.run_until_complete(gojo_client(GOJO8))
            user = GOJO8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            GOJO9.start()
            LOOP.run_until_complete(gojo_client(GOJO9))
            user = GOJO9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_10:
        try:
            GOJO10.start()
            LOOP.run_until_complete(gojo_client(GOJO10))
            user = GOJO10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1
    if not STRING_10:
        failed += 1
    return failed
