from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'CG0O_introduction7classes': ('INTRODUCTION 7 CLASSES', "['2029', '2030', '2031', '2032', '2033', '2034', '2035']", 'christophereng'), 'U8RA_preposition13classes': ('PREPOSITION 13  CLASSES', "['2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049']", 'christophereng'), '0YMY_voice6classes': ('VOICE 6 CLASSES', "['2051', '2052', '2053', '2054', '2055', '2056']", 'christophereng'), 'HQ7M_narration8classes': ('NARRATION 8 CLASSES', "['2058', '2059', '2060', '2061', '2062', '2063', '2064', '2065']", 'christophereng'), 'L1QF_questiontag1class': ('QUESTION TAG 1 CLASS', "['2067']", 'christophereng'), 'PVA5_article5classes': ('ARTICLE 5 CLASSES', "['2069', '2070', '2071', '2072', '2073']", 'christophereng'), 'A8X2_readingcomprehension7classes': ('READING COMPREHENSION 7 CLASSES', "['2075', '2076', '2077', '2078', '2079', '2080', '2081']", 'christophereng'), 'L290_modal4classes': ('MODAL 4 CLASSES', "['2083', '2084', '2085', '2086']", 'christophereng'), 'D1D5_pqrs7classes': ('PQRS 7 CLASSES', "['2088', '2089', '2090', '2091', '2092', '2093', '2094']", 'christophereng'), 'PYHD_superfluous1class': ('SUPERFLUOUS 1 CLASS', "['2096']", 'christophereng'), 'IRGC_subjectverbagreement17classes': ('SUBJECT VERB AGREEMENT 17 CLASSES', "['2105', '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118', '2119', '2120', '2121']", 'christophereng'), '2Q5W_errors2classes': ('ERRORS 2 CLASSES', "['2123', '2124']", 'christophereng'), '663E_tense21classes': ('TENSE 21 CLASSES', "['2126', '2127', '2128', '2129', '2130', '2131', '2132', '2133', '2134', '2135', '2136', '2137', '2138', '2139', '2140', '2141', '2142', '2143', '2144', '2145', '2146']", 'christophereng'), 'TWP8_noun10classes': ('NOUN 10 CLASSES', "['2148', '2149', '2150', '2151', '2152', '2153', '2154', '2155', '2156', '2157']", 'christophereng'), 'GC91_pronoun17classes': ('PRONOUN 17 CLASSES', "['2159', '2160', '2161', '2162', '2163', '2164', '2165', '2166', '2167', '2168', '2169', '2170', '2171', '2172', '2173', '2174', '2175']", 'christophereng'), 'KNU5_adjective7classes': ('ADJECTIVE 7 CLASSES', "['2177', '2178', '2179', '2180', '2181', '2182', '2186']", 'christophereng'), 'JX12_verb9classes': ('VERB 9 CLASSES', "['2187', '2188', '2189', '2190', '2191', '2192', '2193', '2194', '2195']", 'christophereng'), 'UH22_adverb5classes': ('ADVERB 5 CLASSES', "['2196', '2197', '2198', '2199', '2200']", 'christophereng'), '5UQJ_conjunction6classes': ('CONJUNCTION 6 CLASSES', "['2202', '2201', '2203', '2204', '2205', '2206']", 'christophereng'), '62G5_clozetest6classes': ('CLOZE TEST 6 CLASSES', "['2098', '2099', '2100', '2101', '2102', '2103']", 'christophereng')}
    d = dict(listx)
    vx = d[txt]

    if txt in listx:
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")