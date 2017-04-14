#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coroweb import get, post
import asyncio
from models import User

@get('/')
async def index(request):
	users = await User.findAll()
	return {
		'__template__': 'test.html',
		'users': users
		}
	