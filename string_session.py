#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677 and SpEcHiDe
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from telethon.sessions import StringSession, STRING_2, STRING_3, STRING_4, STRING_5, STRING_6, STRING_7, STRING_8, STRING_9, STRING_10
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check your Telegram saved messages section to copy the STRING_SESSION"""
)
API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check Telegram Save Message Mu Untuk Copy STRING_SESSION ")
    session_string = client.session.save()
    saved_messages_template = """Grup Support @GojoSupport

<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <i>Please be careful before passing this value to third parties</i>""".format(
        session_string
    )
    client.send_message("me", saved_messages_template, parse_mode="html")
