import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re


async def fetch_html(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()


async def scrape_yandex():
    url = "https://realty.ya.ru/sankt-peterburg_i_leningradskaya_oblast/snyat/kvartira"
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.find_all('li', class_=re.compile('Item'))

    apartments = []
    for listing in listings:
        apartment = {}
        apartment['title'] = listing.find('span', class_=re.compile("Item__title")).text.strip()
        apartment['Metro'] = listing.find('span', class_='MetroStation__title').text.strip()
        apartment['address'] = listing.find('div', class_=re.compile("Item__address")).text.strip()
        apartment['link'] = 'https://realty.ya.ru/' + listing.find('a', href=re.compile("offer/"))['href'].strip()
        apartments.append(apartment)

    return apartments


async def scrape_avito():
    url = "https://www.avito.ru/sankt-peterburg/kvartiry/sdam/1-komnatnye-ASgBAgICAkSSA8gQzAiOWQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA&footWalkingMetro=5"
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.find_all('div', {"data-marker": "item"})

    apartments = []
    for listing in listings:
        apartment = {}
        apartment['title'] = listing.find('span', class_=re.compile("Item__title")).text.strip()
        apartment['Metro'] = listing.find('span', class_='MetroStation__title').text.strip()
        apartment['address'] = listing.find('div', class_=re.compile("geo-root")).text.strip()
        apartment['link'] = listing.find('a', href=re.compile("iva-item-sliderLink"))['href'].strip()
        apartments.append(apartment)

    return apartments


async def main():
    yandex_apartments = await scrape_yandex()
    all_apartments = yandex_apartments

    with open("../../artifacts/5.2/apartments.json", "w", encoding="utf-8") as file:
        json.dump(all_apartments, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
