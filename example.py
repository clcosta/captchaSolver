from playwright.async_api import async_playwright, BrowserType
from captcha_solver import capcha_solver


async def main(chrome: BrowserType):
    browser = await chrome.launch(headless=False)
    page = await browser.new_page()
    await page.goto(
        'https://my.outbrain.com/login?utm_source=www.outbrain.com'
    )
    await page.type(
        '[name="loginUsername"]', 'hekina6541@alvisani.com', delay=100
    )
    await page.type('[name="loginPassword"]', '1231231', delay=100)
    await page.click('[id="loginButton"]')
    await capcha_solver(page)
    await page.wait_for_timeout(10000)


async def run():
    async with async_playwright() as p:
        await main(p.chromium)


if __name__ == '__main__':
    import asyncio

    asyncio.run(run())
