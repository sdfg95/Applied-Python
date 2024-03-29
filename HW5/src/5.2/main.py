import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import os

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def scrape_cian():
    url = "https://www.cian.ru/arenda-kvartir/"
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Ваш код для извлечения информации о квартирах с сайта CIAN

async def scrape_yandex():
    url = "https://realty.yandex.ru/moskva/snyat/kvartira/"
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Ваш код для извлечения информации о квартирах с сайта Яндекс.Недвижимость

async def scrape_avito():
    url = "https://www.avito.ru/moskva/kvartiry/sdam"
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Ваш код для извлечения информации о квартирах с сайта Авито

async def main():
    tasks = [scrape_cian(), scrape_yandex(), scrape_avito()]
    results = await asyncio.gather(*tasks)
    # Обработка результатов, сохранение в удобном формате (например, JSON)

if __name__ == "__main__":
    asyncio.run(main())
