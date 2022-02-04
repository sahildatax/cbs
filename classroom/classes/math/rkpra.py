from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'cds141': ('B/W 141-142 8 CLASSES SI & CI', ['457', '458', '459', '460', '461', '462', '463', '464'], 'rkpra'), 'cds144': ('B/W 143-144 3 CLASSES GEOMETERY', ['466', '467', '468'], 'rkpra'), 'cds197': ('B/W 196-197 2D MENSURATION  8 CLASSES', ['471', '472', '473', '474', '475', '476', '477', '478'], 'rkpra'), 'cds208': ('3D MENSURATION B/W 207-208 3 CLASSES', ['480', '481', '482'], 'rkpra'), 'cds241': ('NUMBER SYSTEM B/W 241-242 4 CLASSES', ['485', '486', '487', '488'], 'rkpra'), 'cdspc': ('PIPE AND CISTERN B/W 241-242 3 CLASSES', ['490', '491', '492'], 'rkpra'), 'cds2dm3': ('2D MENSURATION B/W 241-242 3 CLASSES', ['494', '495', '496'], 'rkpra'), 'cds242tw2': ('B/W 241-242 TIME AND WORK 2 CLASSES', ['498', '499'], 'rkpra'), 'cdsno9': ('B/W 241-242 NO SYSTEM 9 Classes', ['501', '502', '503', '504', '505', '506', '507', '508', '509'], 'rkpra'), 'cdsalg2': ('B/W 241-242 ALGEBRA 2 Classes', ['511', '512'], 'rkpra'), 'cdssrd3': ('B/W 241-242 SURDS 3 Classes', ['514', '515', '516'], 'rkpra'), 'cdsdec1': ('B/W 241-242 DECIMAL 1 CLASS', ['518'], 'rkpra'), 'cdsdig1': ('B/W 241-242 DIGITAL SUM 1 CLASS', ['520'], 'rkpra'), 'cdstri6': ('B/W 241-242 TRIGO 6 CLASSES', ['522', '523', '524', '525', '526', '527'], 'rkpra'), 'cdshd3': ('B/W 241-242 HEIGHT AND DISTANCE 3 CLASSES', ['529', '530', '531'], 'rkpra'), 'cdsgl2': ('B/W 241-242 GEOMETERY LINE 2 CLASS', ['533', '534'], 'rkpra'), 'cdsgt7': ('B/W 241-242 GEOMETERY TRIANGLE 7 CLASSES', ['536', '537', '538', '539', '540', '541', '542'], 'rkpra'), 'cdsquad4': ('B/W 241-242 QUADRILATERAL 4 CLASSES', ['544', '545', '546', '547'], 'rkpra'), 'cdscir4': ('B/W 241-242 CIRCLE 4 CLASSES', ['549', '550', '551', '552'], 'rkpra'), 'cds2d4mx': ('B/W 241-242 2D MENSURATION 4 CLASSES', ['554', '555', '556', '557'], 'rkpra'), 'cds3d4mx': ('B/W 241-242 3D MENSURATION 4 CLASSES', ['559', '560', '561', '562'], 'rkpra'), 'cdssi4x': ('SI 4 CLASS B/W 266-267', ['565', '566', '567', '568'], 'rkpra'), 'cdsstst6x': ('STATICS 6 CLASS B/W 267-268', ['571', '572', '573', '574', '575', '576'], 'rkpra'), 'cdstri7x': ('B/W 270-271 & 275-276 TRIGO 7 CLASSES', ['580', '581', '582', '583', '584', '585', '586'], 'rkpra'), 'cdsrt3x': ('RATIO 3 CLASSES B/W 283-284', ['589', '590', '591'], 'rkpra'), 'cdsprt1x': ('PARTNERSHIP 1 CLASS B/W 285-286', ['594'], 'rkpra'), 'cdsmx1x': ('MIXTURE 1 CLASS B/W 291-292', ['597'], 'rkpra')}

    if txt in listx:
      d = dict(listx)
      vx = d[txt]
      await get_links(vx[1],vx[0],vx[2],client,callback_query)

  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")