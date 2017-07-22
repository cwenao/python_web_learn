import logging
import asyncio,os,json,time

from aiohttp import web

logging.basicConfig(level=logging.DEBUG)


def index(request):
    return web.Response(body=b'<h1>good good study, day day up</h1>')


@asyncio.coroutine
def init(loop):
    webapp = web.Application(loop=loop)
    webapp.router.add_route('GET','/',index)
    srv = yield from loop.create_server(webapp.make_handler(), '127.0.0.1',9001)

    logging.info('server started : http://127.0.0.1:9001')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
