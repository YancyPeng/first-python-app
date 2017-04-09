import logging
logging.basicConfig(level = logging.INFO)   #logging允许指定记录信息的级别，有debug,info,warning,error等级别
'''
日志级别：
critical > error > warning > info > debug,notset
级别越高打印的日志越少，反之亦然，即
debug    : 打印全部的日志(notset等同于debug)
info     : 打印info,warning,error,critical级别的日志
warning  : 打印warning,error,critical级别的日志
error    : 打印error,critical级别的日志
critical : 打印critical级别
'''

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
	return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv
	
	
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()