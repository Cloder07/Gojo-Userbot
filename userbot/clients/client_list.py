# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, GOJO2, GOJO3, GOJO4, GOJO5, GOJO6, GOJO7, GOJO8, GOJO9, GOJO10):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if GOJO2 is not None:
            id2 = await GOJO2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if GOJO3 is not None:
            id3 = await GOJO3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if GOJO4 is not None:
            id4 = await GOJO4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if GOJO5 is not None:
            id5 = await GOJO5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    try:
        if GOJO6 is not None:
            id6 = await GOJO6.get_me()
            user_ids.append(id6.id)
    except BaseException:
        pass

    try:
        if GOJO7 is not None:
            id7 = await GOJO7.get_me()
            user_ids.append(id7.id)
    except BaseException:
        pass

    try:
        if GOJO8 is not None:
            id8 = await GOJO8.get_me()
            user_ids.append(id8.id)
    except BaseException:
        pass

    try:
        if GOJO9 is not None:
            id9 = await GOJO9.get_me()
            user_ids.append(id9.id)
    except BaseException:
        pass

    try:
        if GOJO10 is not None:
            id10 = await GOJO10.get_me()
            user_ids.append(id10.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTk3Mjg0ODMxOQ==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        GOJO_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        GOJO_USER = client.first_name
    ayiin_mention = f"[{GOJO_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, GOJO_USER, gojo_mention
