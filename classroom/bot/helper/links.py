from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

headlink = str("https://classroombysahil.nolia.repl.co/stream/streamx.nolia.repl.co/a30/")
backlink = str("/download")
sx = str('[InlineKeyboardButton("Class - ')
sxx = str('", url="')
sxxx = str('")],')
backz = str('[InlineKeyboardButton("Back", callback_data="')
bv = str('")]')
async def get_links(lis,text,call,client,callback_query):
    count = len(lis)
    myx = list(range(1, count+1))
    new_friends = ''.join([sx + str(myx[i]) + sxx + headlink + lis[i] + backlink + sxxx for i in range(len(lis) & len(myx))])
    bcv = eval(str(new_friends) + str(backz) + str(call) + str(bv))
    callx = await client.send_message(chat_id=callback_query.message.chat.id, text=text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(bcv))
    await callback_query.message.delete()