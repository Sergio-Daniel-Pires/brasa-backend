import asyncio
import datetime as dt

import requests
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        response = requests.get("https://cbv.com.br/praia/calendario-praia-2024/")

        await page.set_content(response.text, wait_until="domcontentloaded")

        cards = await page.query_selector_all("article > div > section > div > div > div")
        results = []

        for card in cards:
            header_title = await (await card.query_selector('.post-title h2')).inner_text()
            etapa = await (await card.query_selector('.etapa h2')).inner_text()
            local = await (await card.query_selector('.local h2')).inner_text()
            inf = f"{etapa} {local}"
            date = await (await card.query_selector('.post-title2 h2')).inner_text()

            start_date, end_date = date.split(" a ")
            year_now = dt.datetime.now().year
            start_date = int(dt.datetime.strptime(start_date, "%d/%m").replace(year=year_now).timestamp() * 1000)
            end_date = int(dt.datetime.strptime(end_date, "%d/%m").replace(year=year_now).timestamp() * 1000)
            results.append({
                "title": header_title, "extra_info": inf,
                "start_date": start_date, "end_date": end_date
            })

        await browser.close()

        return results

if __name__ == "__main__":
    print(asyncio.run(main()))