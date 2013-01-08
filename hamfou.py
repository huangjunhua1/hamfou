# -*- coding: utf-8 -*-

import redis

class Hamfou:
	def __init__(self, host='localhost', port=6379, db=0):
		self.data = redis.StrictRedis(host=host, port=port, db=db)

	def chat(self, ask):
		ans = self.data.get(ask);
		if ans == None:
			return '呵呵'
		else:
			return ans
			
