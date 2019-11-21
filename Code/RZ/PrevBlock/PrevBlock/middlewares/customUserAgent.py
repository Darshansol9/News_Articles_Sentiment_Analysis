from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from Code.RZ.PrevBlock.PrevBlock.middlewares import resouce

import random

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(resouce.USER_AGENT_LIST)
        request.header.setdefault('User-Agent', ua)
