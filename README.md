# Welcome to CaptchaSolver!
<p><img height="20" src="https://img.shields.io/badge/Version-v1.0.0-green"/></p>

Simple reCAPTCHA Solver with Python using accessibility sound option at Recaptcha. Created using Playwright.

## Requirements
Python >= 3.11  
[FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)

## Installation

- Install Dependecies

```bash
$ pip install -r requirements.txt
```

- Install Playwright

```bash
$ playwright install
```

- Intall FFmpeg (extractor texto from audio)

[Install here](https://github.com/BtbN/FFmpeg-Builds/releases)

In case to have trouble in installation, you can follow the steps in this [tutorial](https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/)

## Usage example

```python
from captcha_solver import capcha_solver

def your_page_funcion(page):
    element_handle = await page.wait_for_selector('iframe[title="reCAPTCHA"]')
    captcha = await element_handle.content_frame()
    captcha_checkbox = await captcha.wait_for_selector('.recaptcha-checkbox-border')
    await captcha_checkbox.click()
    await capcha_solver(page)
```

## How it works

1. Change solve type to accessibility

![Captcha](./public/Captcha.png)

2. Listen the audio and extract the text

![Listen](./public/Audio.png)

3. Write the extracted text into result

![WriteText](./public/result.png)

4. Solve the captcha

![SolvedSuccess](./public/success.png)

## Social medias
* [Instagram](https://www.instagram.com/claudiogfez/)
* [Linkedin](https://www.linkedin.com/in/clcostaff/)

# Author
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=120><br><sub>@clcostaf</sub>](https://github.com/clcosta) |
| :---: |
