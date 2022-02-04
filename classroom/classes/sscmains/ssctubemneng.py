from pyrogram import Client
from generator import app, sudo_users
from classroom.bot.helper.utils import get_formatted_chat
from classroom.bot.helper.links import get_links
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def mydata(client,callback_query):
  if str(callback_query.message.chat.id) in sudo_users:
    txt=callback_query.data
    listx = {'AM3I_narration9classes': ('NARRATION 9 CLASSES', "['1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859']", 'ssctubemneng'), 'R5YD_parajumbles5classes': ('PARAJUMBLES 5 CLASSES', "['1861', '1862', '1863', '1864', '1865']", 'ssctubemneng'), 'LS1J_preparation4classes': ('PREPARATION 4 CLASSES', "['1867', '1868', '1869', '1870']", 'ssctubemneng'), '3O8A_conjunction5classes': ('CONJUNCTION 5 CLASSES', "['1872', '1873', '1874', '1875', '1876']", 'ssctubemneng'), 'XEE3_adverb4classes': ('ADVERB 4 CLASSES', "['1878', '1879', '1880', '1881']", 'ssctubemneng'), 'F8QU_subjectverbagreement3classes': ('SUBJECT VERB AGREEMENT 3 CLASSES', "['1883', '1884', '1885']", 'ssctubemneng'), 'VFBP_readingcomprehension2classes': ('READING COMPREHENSION 2 CLASSES', "['1887', '1888']", 'ssctubemneng'), 'ZZ2Y_vocab10classes': ('VOCAB 10 CLASSES', "['1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899']", 'ssctubemneng'), '36H2_clozetest12classes': ('CLOZE TEST 12 CLASSES', "['1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912']", 'ssctubemneng'), 'MJ6T_article4classes': ('ARTICLE 4 CLASSES', "['1914', '1915', '1916', '1917']", 'ssctubemneng'), '6TLD_noun6classes': ('NOUN 6 CLASSES', "['1919', '1920', '1921', '1922', '1923', '1924']", 'ssctubemneng'), 'UBGQ_pronoun4classes': ('PRONOUN 4 CLASSES', "['1926', '1927', '1928', '1929']", 'ssctubemneng'), '6Z2A_adjective4classes': ('ADJECTIVE 4 CLASSES', "['1931', '1932', '1933', '1934']", 'ssctubemneng'), 'Y77C_verb9classes': ('VERB 9 CLASSES', "['1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944']", 'ssctubemneng'), 'ITZ5_activepassive6classes': ('ACTIVE PASSIVE 6 CLASSES', "['1946', '1947', '1948', '1949', '1950', '1951']", 'ssctubemneng')}
    d = dict(listx)
    vx = d[txt]

    if txt in listx:
      await get_links(eval(vx[1]),vx[0],vx[2],client,callback_query)


  else:
    await client.send_message(chat_id=callback_query.message.chat.id,
                        text=f"What are you doing buddy.")