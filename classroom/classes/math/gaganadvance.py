from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'K106_mensuration2d10classes': ('MENSURATION 2D 10 CLASSES', "['5', '7', '8', '9', '10', '11', '12', '13', '14', '6']", 'gaganadvance'), '784N_surds&indicies4classes': ('SURDS & INDICIES 4 CLASSES', "['19', '16', '17', '18']", 'gaganadvance'), '0P3O_calculation4classes': ('CALCULATION 4 CLASSES', "['21', '22', '23', '24']", 'gaganadvance'), 'HBNN_di5classes': ('DI 5 CLASSES', "['26', '27', '28', '29', '30']", 'gaganadvance'), 'KUT9_coordinategeometry3classes': ('COORDINATE GEOMETRY 3 CLASSES', "['32', '33', '34']", 'gaganadvance'), '8NPJ_3dmensuration13classes': ('3D MENSURATION 13 CLASSES', "['36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48']", 'gaganadvance'), '83L0_algebra14classes': ('ALGEBRA 14 CLASSES', "['50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63']", 'gaganadvance'), 'XAZV_trigonometry12classes': ('TRIGONOMETRY 12 CLASSES', "['65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76']", 'gaganadvance'), '9COC_geometry40classes': ('GEOMETRY 40 CLASSES', "['78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117']", 'gaganadvance'), 'KU5N_heightanddistance3classes': ('HEIGHT AND DISTANCE 3 CLASSES', "['119', '120', '121']", 'gaganadvance'), '6J43_maximaminima5classes': ('MAXIMA MINIMA 5 CLASSES', "['123', '124', '125', '126', '127']", 'gaganadvance'), '7QHU_numbersystem16classes': ('NUMBER SYSTEM 16 CLASSES', "['141', '142', '143', '144', '136', '137', '138', '139', '140', '129', '130', '131', '132', '133', '134', '135']", 'gaganadvance'), 'M4S2_lcmhcf5classes': ('LCM HCF 5 CLASSES', "['146', '147', '148', '149', '150']", 'gaganadvance')}
    d = dict(listx)
    vx = d[txt]

    if txt in listx:
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")