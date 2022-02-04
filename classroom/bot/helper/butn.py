from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

sx = str('[InlineKeyboardButton("')
sxx = str('", callback_data="')
sxxx = str('")],')

async def butn(lis1,lis2,text,client,callback_query):
    new_friends = ''.join([sx + eval(lis1)[i] + sxx + eval(lis2)[i] + sxxx for i in range(len(eval(lis1)))])
    bcv = eval(str(new_friends))
    callx = await client.send_message(chat_id=callback_query.message.chat.id, text=text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(bcv))
    await callback_query.message.delete()