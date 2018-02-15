import scrapy
import time

class Mql5Spider(scrapy.Spider):
    name = "mql5"
    baseUrl = "https://www.mql5.com/zh/economic-calendar/content?date_mode=0&from={0}T00%3A00%3A00&to={1}T23%3A59%3A59&importance={2}&currencies={3}"
    startDateTick = 1262275200
    #overDateTick = time.time()
    overDateTick = 1282275200
    interval = 7
    intervalTimeOneDay = 86400
    importance = 12
    currencies = 127

    def initUrls(self):
        urls = []
        t = self.startDateTick
        while t < self.overDateTick:
            startTick = t
            overTick = t + self.interval * self.intervalTimeOneDay - 1
            a = time.strftime('%Y-%m-%d', time.localtime(startTick))
            b = time.strftime('%Y-%m-%d', time.localtime(overTick))
            c = self.importance
            d = self.currencies
            urls.append(self.baseUrl.format(a, b, c, d))
            t = overTick + 1
        return urls

    def start_requests(self):
        urls = self.initUrls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)

