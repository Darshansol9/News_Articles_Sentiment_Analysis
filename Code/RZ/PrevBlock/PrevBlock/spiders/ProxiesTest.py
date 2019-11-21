import scrapy

class ProxiesTest(scrapy.Spider):
    name = 'proxies_scrapy'


    def cnn_sitemap_generator(self):
        date_lst = []
        ori_str1 = 'https://www.cnn.com/sitemap-201'
        ori_str2 = '.html'

        for i in range(1, 9):
            for j in range(1, 13):
                date_lst.append(ori_str1 + str(i) + '-' + str(j) + ori_str2)

        print(date_lst)

        return date_lst

    def start_requests(self):   # start_requests is multiplethreadly crawling
        urls = self.cnn_sitemap_generator() # It will generate the sitemap urls for cnn

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)