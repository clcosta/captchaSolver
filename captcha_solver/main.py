import os
import tempfile
import requests
from playwright.async_api import Page, Frame
from .audio_to_text import audio2text

TEN_SECONDS = 10 * 1000

async def get_iframe(page: Page | Frame, selector: str) -> Frame:
    element_handle = await page.wait_for_selector(selector)
    frame = await element_handle.content_frame()
    return frame

async def capcha_solver(page: Page) -> None:
    captcha_frame = await get_iframe(page, 'iframe[title^="o desafio reCAPTCHA"]')
    if not captcha_frame:
        print("Captcha frame not found")
        return
    await captcha_frame.click('[id="recaptcha-audio-button"]')
    await page.wait_for_timeout(TEN_SECONDS)
    audio_element = await captcha_frame.query_selector('audio')
    audio_src = await audio_element.get_attribute('src')
    temp_dir = temp_dir = tempfile.TemporaryDirectory(dir=tempfile.gettempdir())
    audio_path = os.path.join(temp_dir.name,'audio_captcha.mp3')
    with open(audio_path, 'wb') as f:
        audio_content = requests.get(audio_src).content
        f.write(audio_content)
    text = audio2text(audio_path)
    temp_dir.cleanup()
    await captcha_frame.type('[id="audio-response"]', text)
    await captcha_frame.click('[id="recaptcha-verify-button"]')
