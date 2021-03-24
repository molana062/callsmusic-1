from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

ᴇᴜᴘʜᴏʀɪᴀ  ᴍᴜsɪᴄ  ᴀᴅᴀʟᴀʜ  ʙᴏᴛ   ᴍᴜsɪᴄ  ᴄᴀʟʟ  ɢʀᴜᴘ👑!
ᴍᴏʜᴏɴ  ᴍᴀᴋʟᴜᴍ  ᴊɪᴋᴀ  ᴀᴅᴀ  ᴍᴀsᴀʟᴀʜ  ᴘᴀᴅᴀ  ᴋᴜᴀʟɪᴛᴀs  ᴍᴜsɪᴋ.
Jika ingin menggunakan cukup ijin ke owner hehe
Owner ganteng : Molana
Support Channel Owner Ya @ruangpublikk

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://github.com/callsmusic/callsmusic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Cara Pakai", url="https://telegra.ph/ᴏ-ʟ-ᴀ-ɴ-ᴀ-03-14"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://telegram.me/betterthaanhecan"
                    ),
                    InlineKeyboardButton(
                        "Channel owner", url="https://telegram.me/ruangpublikk"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
