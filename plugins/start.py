from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/nekosecurity")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/nekosecurity")]
    ])
    welcomed = f"Hai <b>{message.from_user.first_name}</b> saya adalah Bot Youtube download, Cukup kirim link youtube kalian ya 😊 \nKetik /help untuk Melihat Info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
