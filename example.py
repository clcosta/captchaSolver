from playwright.async_api import async_playwright, BrowserType
from captcha_solver import capcha_solver


async def main(chrome: BrowserType):
    browser = await chrome.launch(headless=False)
    page = await browser.new_page()
    await page.goto(
        'https://patrickhlauke.github.io/recaptcha/'
    )
    element_handle = await page.wait_for_selector('iframe[title="reCAPTCHA"]')
    captcha = await element_handle.content_frame()
    captcha_checkbox = await captcha.wait_for_selector('.recaptcha-checkbox-border')
    await captcha_checkbox.click()
    await capcha_solver(page)
    await page.wait_for_timeout(10000)


async def run():
    async with async_playwright() as p:
        await main(p.chromium)


if __name__ == '__main__':
    import asyncio

    asyncio.run(run())
