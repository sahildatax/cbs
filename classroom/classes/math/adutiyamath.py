from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'CM0T_algebra14classes': ('ALGEBRA 14 CLASSES', "['2408', '2409', '2410', '2411', '2412', '2413', '2414', '2406', '2407', '2405', '2401', '2402', '2403', '2404']", 'adutiyamath'), 'P4BV_coordinategeometry5classes': ('COORDINATE GEOMETRY 5 CLASSES', "['2416', '2417', '2418', '2419', '2420']", 'adutiyamath'), '3DRS_geometry18classes': ('GEOMETRY 18 CLASSES', "['2422', '2423', '2424', '2425', '2426', '2427', '2428', '2429', '2430', '2431', '2432', '2433', '2434', '2435', '2436', '2439', '2437', '2438']", 'adutiyamath'), 'LY1D_heightanddistance1class': ('HEIGHT AND DISTANCE 1 CLASS', "['2441']", 'adutiyamath'), 'LTXP_2dmensuration5classes': ('2D MENSURATION 5 CLASSES', "['2444', '2445', '2446', '2447', '2448']", 'adutiyamath'), 'V3AA_mensuration9classes': ('MENSURATION 9 CLASSES', "['2450', '2451', '2452', '2453', '2454', '2455', '2456', '2457', '2458']", 'adutiyamath'), 'HK0F_numbersystem20classes': ('NUMBER SYSTEM 20 CLASSES', "['2478', '2479', '2477', '2460', '2472', '2473', '2474', '2475', '2476', '2462', '2463', '2464', '2465', '2466', '2467', '2468', '2469', '2470', '2461', '2471']", 'adutiyamath'), 'GD7V_trigonometry8classes': ('TRIGONOMETRY 8 CLASSES', "['2481', '2482', '2483', '2484', '2485', '2486', '2487', '2488']", 'adutiyamath'), 'GYSF_percentage7classes': ('PERCENTAGE 7 CLASSES', "['2491', '2492', '2493', '2494', '2495', '2496', '2497']", 'adutiyamath'), 'PRMW_average4classes': ('AVERAGE 4 CLASSES', "['2499', '2500', '2501', '2502']", 'adutiyamath'), 'I4AG_timeandwork7classes': ('TIME AND WORK 7 CLASSES', "['2506', '2504', '2507', '2505', '2508', '2509', '2510']", 'adutiyamath'), 'ZJOM_workandwages1class': ('WORK AND WAGES 1 CLASS', "['2512']", 'adutiyamath'), 'KRIH_pipeandcistern4classes': ('PIPE AND CISTERN 4 CLASSES', "['2514', '2515', '2516', '2517']", 'adutiyamath'), '8N1L_timespeeddistance7classes': ('TIME SPEED DISTANCE 7 CLASSES', "['2519', '2520', '2521', '2522', '2523', '2524', '2525']", 'adutiyamath'), 'DY2F_train2classes': ('TRAIN 2 CLASSES', "['2528', '2527']", 'adutiyamath'), 'DJER_bostandstreamrace2classes': ('BOST AND STREAM RACE 2 CLASSES', "['2530', '2531']", 'adutiyamath'), 'KXOA_di1class': ('DI 1 CLASS', "['2533']", 'adutiyamath'), 'IWKB_probability2classes': ('PROBABILITY 2 CLASSES', "['2535', '2536']", 'adutiyamath'), 'IDGD_pipeandcistern2classes': ('PERMUTATION & COMBINATION 2 CLASSES', "['2538', '2539']", 'adutiyamath'), 'BL6E_profitandloss6classes': ('PROFIT AND LOSS 6 CLASSES', "['2546', '2545', '2542', '2543', '2544', '2541']", 'adutiyamath'), 'A24Y_statics2classes': ('STATICS 2 CLASSES', "['2548', '2549']", 'adutiyamath'), 'UH3Z_simpleinterest1class': ('SIMPLE INTEREST 1 CLASS', "['2551']", 'adutiyamath'), 'I0OY_compoundinterest5classes': ('COMPOUND INTEREST 5 CLASSES', "['2556', '2553', '2554', '2555', '2557']", 'adutiyamath'), 'GWIZ_lcmandhcf2classes': ('LCM AND HCF 2 CLASSES', "['2560', '2559']", 'adutiyamath'), 'C0G0_ratioandproportion6classes': ('RATIO AND PROPORTION 6 CLASSES', "['2566', '2567', '2562', '2563', '2564', '2565']", 'adutiyamath'), 'SRO4_alligation4classes': ('ALLIGATION 4 CLASSES', "['2569', '2571', '2572', '2570']", 'adutiyamath'), 'N1WP_partnership2classes': ('PARTNERSHIP 2 CLASSES', "['2574', '2575']", 'adutiyamath'), 'VSDW_age1class': ('AGE 1 CLASS', "['2577']", 'adutiyamath')}
    d = dict(listx)
    vx = d[txt]

    if txt in listx:
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")