from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USARNAME, BOT_NAME as bot
from helpers.filters import other_filters2


@Client.on_message(command(["start", f"start@{BOT_USARNAME}"]))
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Merhaba, {message.from_user.mention} 🎵
Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Talia Müzik 🎙️](https://t.me/Sohbetdestek).
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏷️ Destek Grubu", url="https://t.me/Sohbetdestek"
                    ),
                    InlineKeyboardButton(
                        "🔧 Yardımcı", url = "https://t.me/Bir_Beyfendi"
                    )
                  ],[
                    InlineKeyboardButton(
                        "🛠 Kurucu" , url = "https://t.me/Mahoaga"
                    ),
                    InlineKeyboardButton(
                        "🔊 Asistan" , url = "https://t.me/TaliaMusicAsistant"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌀 Komutlar" , url = "https://telegra.ph/Komutlar-10-22"
                    ),
                    InlineKeyboardButton(
                        "🎮 Oyun Botu", url="https://t.me/BasitOyunBot"
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
                        "⚙ Geliştirici", url="https://t.me/Mahoaga")
                ]
            ]
        )
   )

