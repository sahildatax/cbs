from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'CZ14_percentage10classes': ('PERCENTAGE 10 CLASSES', "['1502', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1503']", 'gaganarithmetic'), 'UP5N_timeandwork7classes': ('TIME AND WORK 7 CLASSES', "['1513', '1514', '1515', '1516', '1517', '1518', '1519']", 'gaganarithmetic'), 'TXHH_pipe&cistern2classes': ('PIPE & CISTERN 2 CLASSES', "['1521', '1522']", 'gaganarithmetic'), 'FRIQ_si3classes': ('SI 3 CLASSES', "['1525', '1526', '1527']", 'gaganarithmetic'), 'RS7K_ci9classes': ('CI 9 CLASSES', "['1529', '1530', '1531', '1532', '1533', '1534', '1535', '1536', '1537']", 'gaganarithmetic'), '52CM_timespeed&distance7classes': ('TIME SPEED & DISTANCE 7 CLASSES', "['1539', '1540', '1541', '1542', '1543', '1544', '1545']", 'gaganarithmetic'), '7WB8_train2classes': ('TRAIN 2 CLASSES', "['1547', '1548']", 'gaganarithmetic'), 'YE2N_boat&stream3classes': ('BOAT & STREAM 3 CLASSES', "['1551', '1550', '1552']", 'gaganarithmetic'), 'F2RA_partnership2classes': ('PARTNERSHIP 2 CLASSES', "['1554', '1555']", 'gaganarithmetic'), '5S1V_average4classes': ('AVERAGE 4 CLASSES', "['1557', '1558', '1559', '1560']", 'gaganarithmetic'), '2EW3_di5classes': ('DI 5 CLASSES', "['1562', '1563', '1564', '1565', '1566']", 'gaganarithmetic'), 'EI90_ratio&proportion6classes': ('RATIO & PROPORTION 6 CLASSES', "['1568', '1569', '1570', '1571', '1572', '1573']", 'gaganarithmetic'), '9LUQ_mixture3classes': ('MIXTURE 3 CLASSES', "['1575', '1576', '1577']", 'gaganarithmetic'), 'BYUN_alligation6classes': ('ALLIGATION 6 CLASSES', "['1579', '1580', '1581', '1582', '1583', '1584']", 'gaganarithmetic'), '1HSR_numbersystem12classes': ('NUMBER SYSTEM 12 CLASSES', "['1586', '1590', '1591', '1592', '1593', '1594', '1595', '1596', '1597', '1587', '1588', '1589']", 'gaganarithmetic'), 'A4OZ_lcm&hcf4classes': ('LCM & HCF 4 CLASSES', "['1599', '1600', '1601', '1602']", 'gaganarithmetic'), '9B6L_calculation5classes': ('CALCULATION 5 CLASSES', "['1604', '1605', '1606', '1607', '1608']", 'gaganarithmetic'), 'RHLZ_surds3classes': ('SURDS 3 CLASSES', "['1610', '1611', '1612']", 'gaganarithmetic'), '0Q78_profit&loss9classes': ('PROFIT & LOSS 9 CLASSES', "['1614', '1615', '1616', '1617', '1618', '1619', '1620', '1621', '1622']", 'gaganarithmetic')}
    d = dict(listx)
    vx = d[txt]

    if txt in listx:
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")