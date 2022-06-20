# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import GOJO2, GOJO3, GOJO4, GOJO5, GOJO6, GOJO7, GOJO8, GOJO9, GOJO10, bot, branch, tgbot
from userbot.utils import gojo_version as py_ver
from userbot.utils import HOSTED_ON, checking

MSG_ON = """
❏  🔥GOJO-USERBOT🔥 ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼┅━━━━━╍━━━━━┅╾
├▹ 🔥GOJO-USERBOT🔥 Vᴇʀsɪᴏɴ - {} •[{}]•
├▹ Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {}
├▹ @{}
├▹ Kᴇᴛɪᴋ {}alive Uɴᴛᴜᴋ Mᴇɴɢᴇᴄᴇᴋ Bᴏᴛ
╰╼┅━━━━━╍━━━━━┅╾
"""


async def pocong_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            GojoUBOT = await tgbot.get_me()
            BOT_USERNAME = GojoUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            GojoUBOT = await tgbot.get_me()
            BOT_USERNAME = GojoUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "Assɪsᴛᴀɴᴛ Aʏɪɪɴ"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO2:
            await checking(GOJO2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO3:
            await checking(GOJO3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO4:
            await checking(GOJO4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO5:
            await checking(GOJO5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO6:
            await checking(GOJO6)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO6.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO7:
            await checking(GOJO7)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO7.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO8:
            await checking(GOJO8)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO8.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO9:
            await checking(GOJO9)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO9.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if GOJO10:
            await checking(GOJO10)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await GOJO10.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
