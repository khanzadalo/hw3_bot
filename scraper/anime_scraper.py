import asyncio
from parsel import Selector
import httpx
from pprint import pprint


class AnimeScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    MAIN_URL = 'https://animespirit.tv/'

    def __init__(self):
        self.links = []

    async def get_html(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            print(url)
            result = self.parse_links(response.text)
            self.links.extend(result)

    def parse_links(self, response):
        selector = Selector(text=response)
        all_links = selector.xpath('//div[@class="custom-poster"]/a/@href').getall()

        return all_links[:6]


async def main():
    scraper = AnimeScraper()

    pages = []
    throttler = asyncio.Semaphore(5)
    for i in range(1, 25):
        url = f"https://animespirit.tv/?page={i}&pagesize=25"
        task = asyncio.create_task(scraper.get_html(url))
        pages.append(task)

    await asyncio.gather(*pages)



if __name__ == '__main__':
    asyncio.run(main())
