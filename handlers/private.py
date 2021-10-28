from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USARNAME, BOT_NAME as bot
from helpers.filters import other_filters2


@Client.on_message(command(["start", f"start@{BOT_USARNAME}"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""**Merhaba, {message.from_user.mention} 🎵
Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://t.me/mussic_kanal/135")
                  ],[
                    InlineKeyboardButton(
                        "💬Sohbet Grubum", url="https://t.me/sev_beni"
                    ),
                    InlineKeyboardButton(
                        "🥳 Asistan 🥳", url="https://t.me/MissMuzikAsiistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🥳 Sahibim 🥳", url="https://t.me/beyfendi_47"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command(["reload", f"reload@{BOT_USARNAME}"]) & ~filters.private & ~filters.channel)
async def reload(_, message: Message):
      await message.reply_text("""**Yeniden başlatıldı. Bot çalışıyor ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙ Geliştirici", url="https://t.me/beyfendi_47")
                ]
            ]
        )
   )

