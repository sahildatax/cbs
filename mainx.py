import os
from aiohttp import web
import aiohttp_jinja2
import jinja2
from urllib.request import urlopen
from bs4 import BeautifulSoup

hostx = os.getcwd()

async def hello(request):
    return web.Response(text="Hello, world")

@aiohttp_jinja2.template('t.html')
def streamx(request):
    id1 = request.match_info.get("id1", "")
    id2 = request.match_info.get("id2", "")
    id3 = request.match_info.get("id3", "")
    id4 = request.match_info.get("id4", "")
    id5 = request.match_info.get("id5", "")
    id6 = request.match_info.get("id6", "")
    link = f'https://{id1}/{id2}/{id3}/{id4}/{id5}/{id6}'
    url = f'https://streamx-nolia-repl-co.translate.goog/a30/{id3}/view?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en-GB&_x_tr_pto=wapp'
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    titlexzz1 = soup.title.get_text()
    if link.endswith("////"):
      link = link[:-4]
    if link.endswith("//"):
      link = link[:-2]
    if link.endswith("/"):
      link = link[:-1]
    if link.endswith("///"):
      link = link[:-3]
    if link.endswith("/////"):
      link = link[:-5]
    return {'linkx' : link, 'titlexzz' : titlexzz1}


async def main():
    app = web.Application()
    aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(hostx + '/views'))
    app.add_routes(
        [
            web.get('/stream/{id1}', streamx),
            web.get('/stream/{id1}/{id2}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}/{id5}', streamx),
            web.get('/stream/{id1}/{id2}/{id3}/{id4}/{id5}/{id6}', streamx),
            web.get('/', hello)
        ]
    )
    return app

if __name__ == "__main__":
    web.run_app(main())
