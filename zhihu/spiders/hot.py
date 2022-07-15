import re
import scrapy
import json
from zhihu.items import ZhihuItem

class HotSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/hot']
    cookies = {'__snaker__id': 'cseMuX9LLzRpxhxS', '_9755xjdesxxd_': '32',  'captcha_ticket_v2': '2|1:0|10:1656413946|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfUk1sMTdVcU9NQ1ZPcy52WHNMX1pWdDd2NTBBTG1Ja09rajIyQk1uVklyRUVNTloyWU9Gdkp2ZnA0blZfMG1wRWRfSHlMOWg1TjB5QjBWWnZZa0JUdW5lLVllcll2Llh1alZwSGI0OU1vdVd3UWRrNDRyNkNUWFVjaUNuYTFad2tjUEFDYWVISEl0Wkouc2NweDJGRkRjNExvU0FaZ0ZSenIuaTA5aV83WWcwaG1jdkdJX2lfMGRraE9qenZIb3djckVMY1ZlQmVhVmZTLmpHNjdOd21GSzFVUXdBSEQyTURNSjhUZ3JaNE1EUTJQYzk1aS5ELmI5RkdGWnM0emNXRFA5YldXR200dk1kQ0xlaU5NVGdIUThaTVQyMDlTaS5CaXJIeTZRenFfaHJwSVhFZWRrQ1JVcmlGd3hERElkcmoyejlBS0l0c0RaNEZHTi4tYVZqMC5sMG9QYVRfQ0VHQ2tqX1lablouVnQ0WUNuNHZNajIuVGNvbkd1ZkFSdjZyRURBclBFbHZJUV9wVU5KLUpfSE9BSHgyS3U0ZXBOdjBqNEZFVkZEYklKWWFXMEM1RmFZZ1V3bVV4a3NNMm52UU9NVXJFVkpnbzR0Y2xIUVNqdVZLaUxQSnNSTzBPSE01MmM4MjZTRGdYVnIuWmxlS0lCeFl1RzA3LmxwMyJ9|fb17b51348c3bbb87e185f6e616e27a7cab8868d9f7f836e4e0cdca61bbbd460', 'ariaDefaultTheme': 'undefined', 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1657500927,1657535828,1657596979,1657676648', 'captcha_session_v2': '|54796e7588c2e2cf85dd87f44e98fdb6c4817b17e91f53af22f2df6a9fdab044', 'SESSIONID': 'Ww9b9xxlGxIDomBkBHxNYHtcO8xrA0PAhtR50X4SZRt', 'JOID': '', 'osd': '', 'gdxidpyhxdE': 'UcYv3hJdI2j%5C5jRbgUce7e13nOAzRjxUJhkvL%2FV3QaXxaU9sbDNP068wx5W%5Ct7e58xLaLMbBtVSUhh1Jm5BWzOoUGhTZpZM%2BsBmVlPs3lRTRw2sa0AyTEAHIaXjA%2F5lpoNLGM9v2SbTs43U0RxbVi%5Cn0GXZ5lHWgMhK5VPLT%5CorCRpne%3A1657677549995', 'YD00517437729195%3AWM_NI': 'zsspdbikhPhLHWjzJK5QpsID%2F9NACaXpZvli1Xlz65HpB1LISfV7WohStBZELFoS1DJy2oMUNxIOzUbBiA7C%2BtoVCYT9MYz2UGfj6GUyLrlgEI1q5RCUcCJGDqSi3LCPSHg%3D', 'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee86e95b88f58287ae4593e78bb6c84b979a8a82d84bb6acb7b4bc3a98bd83d7b62af0fea7c3b92abaadbd91e76aabb5a8b1eb488c89a69bc941f78fc094cc50ede782a2c26b9cb09697ef63f388a49bb53f8cb08ed2cf4391ba9ad8d665ac8dbca3d94f909aa1b4b4508aa7fe90d05f8ea887b0f95fa29ea7a2b649e9aca1b7c25398e783baf93a9799aa8bb54d97a78493ef6d8797ff92b85a818bada4c94d88af9d8ab24881909da9e637e2a3', 'z_c0': '2|1:0|10:1657676703|4:z_c0|92:Mi4xWkVLRUFnQUFBQUFBVU5MRlFGUVFGU2NBQUFCZ0FsVk5uN0QxWWdBaFc4dFdQSEh6LUhxTlZhMmYyM0p5YWRnNUFB|dfd8045549846f11b4e525e2df98d9855f3e648059a11cb12e3a97972fc20607', 'q_c1': '4f7c776e63bc4d1ea55d8c54193e8304|1657676704000|1657676704000', 'tst': 'h', 'NOT_UNREGISTER_WAITING': '1', 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1657676708', 'KLBRSID': 'ca494ee5d16b14b649673c122ff27291|1657677343|1657676661'}

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url, callback=self.parse_index, cookies=self.cookies)

    def parse_index(self, response):
        hotitems = response.css('.HotItem-content')
        for hoteitem in hotitems:
            url = hoteitem.css('a::attr(href)').extract_first()
            yield scrapy.Request(url, callback=self.parse_detail)


    def parse_detail(self, response):
        json_data = re.findall(r'<script id="js-initialData" type="text/json">(.*?)</script>', response.text, re.S)[0]
        data = json.loads(json_data)
        id = response.url.split('/')[-1]

        item = ZhihuItem()
        item['title'] = data['initialState']['entities']['questions'][id]['title']
        item['excerpt'] = data['initialState']['entities']['questions'][id]['excerpt']
        item['follower'] = data['initialState']['entities']['questions'][id]['followerCount']
        item['visit'] = data['initialState']['entities']['questions'][id]['visitCount']
        item['answers'] = []
        answers = data['initialState']['entities']['answers']
        for answer in answers.values():
            answer_excerpt = answer['content']
            item['answers'].append(answer_excerpt)

        yield item
