import asyncio
import os
from playwright.async_api import async_playwright

OUT_DIR = "/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b"

async def capture_details():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # 1. Intro section
        await page.evaluate("document.getElementById('about').scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_intro.png"))
        
        # 2. Timeline section
        await page.evaluate("document.getElementById('timeline').scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_timeline.png"))
        
        # 3. Speaker section ("Mein Werdegang")
        await page.evaluate("document.getElementById('contact').scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_speaker.png"))
        
        # 4. Contact form
        await page.evaluate("document.getElementById('contact-form').scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_contact_form.png"))
        
        await browser.close()
        print("Detail verification screenshots captured!")

asyncio.run(capture_details())
