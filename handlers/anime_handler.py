import asyncio
from aiogram import types
from config import dp
from scraper.anime_scraper import AnimeScraper


async def scrape_links(call: types.CallbackQuery):
    scraper = AnimeScraper()
    # data = scraper.parse_data()
    # for url in data:
    #     await call.message.answer(
    #         f"{AnimeScraper.MAIN_URL}{url}",
    #     )
    pages = []
    throttler = asyncio.Semaphore(5)
    for i in range(1, 25):
        url = f"https://animespirit.tv/?page={i}&pagesize=25"
        task = asyncio.create_task(scraper.get_html(url))
        pages.append(task)
    await asyncio.gather(*pages)

    data = scraper.links
    for url in data[:6]:
        await call.message.answer(
            f"{AnimeScraper.MAIN_URL}{url}",
        )

def register_links_handlers(dp):
    dp.register_callback_query_handler(scrape_links, lambda c: c.data == "parser_links")

