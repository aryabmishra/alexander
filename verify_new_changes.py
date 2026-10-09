import asyncio
import os
from playwright.async_api import async_playwright

OUT_DIR = "/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b"

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        
        # 1. Desktop 1440x900
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # Slide to Card 4: Disziplin & Verantwortung
        await page.evaluate("""() => {
            const el = document.getElementById('work');
            if (el) el.scrollIntoView();
            const sw = document.querySelector('.swiper-key-blocks')?.swiper;
            if (sw) sw.slideTo(4);
        }""")
        await page.wait_for_timeout(700)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_disziplin_card_desktop.png"))
        
        # Bottom Schedule a Call Section
        await page.evaluate("() => document.getElementById('connect').scrollIntoView();")
        await page.wait_for_timeout(700)
        await page.screenshot(path=os.path.join(OUT_DIR, "verify_schedule_call_desktop.png"))
        
        # 2. Mobile 390x844
        page_mob = await browser.new_page(viewport={"width": 390, "height": 844})
        await page_mob.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page_mob.wait_for_timeout(1000)
        
        # Mobile Disziplin & Verantwortung
        await page_mob.evaluate("""() => {
            const el = document.getElementById('work');
            if (el) el.scrollIntoView();
            const sw = document.querySelector('.swiper-key-blocks')?.swiper;
            if (sw) sw.slideTo(4);
        }""")
        await page_mob.wait_for_timeout(700)
        await page_mob.screenshot(path=os.path.join(OUT_DIR, "verify_disziplin_card_mobile.png"))
        
        # Mobile Schedule a Call
        await page_mob.evaluate("() => document.getElementById('connect').scrollIntoView();")
        await page_mob.wait_for_timeout(700)
        await page_mob.screenshot(path=os.path.join(OUT_DIR, "verify_schedule_call_mobile.png"))
        
        await browser.close()
        print("Verification complete!")

asyncio.run(verify())
