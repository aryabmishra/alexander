import asyncio
import os
from playwright.async_api import async_playwright

OUT_DIR = "/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b"

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        
        # 1. Desktop 1440x900
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # Desktop Hero
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_desktop_hero.png"))
        
        # Desktop Intro & Work
        await page.evaluate("const el = document.getElementById('work'); if(el) el.scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_desktop_work.png"))
        
        # Desktop Timeline
        await page.evaluate("const el = document.getElementById('story'); if(el) el.scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_desktop_timeline.png"))
        
        # Desktop Contact & Speaker
        await page.evaluate("const el = document.getElementById('contact-form'); if(el) el.scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_desktop_contact.png"))
        
        # 2. Desktop Insights Page
        await page.goto("http://localhost:5175/insights.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_insights_hero.png"))
        
        await page.evaluate("const el = document.getElementById('insights-grid'); if(el) el.scrollIntoView();")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(OUT_DIR, "navy_insights_grid.png"))
        
        # 3. Mobile 390x844
        page_mob = await browser.new_page(viewport={"width": 390, "height": 844})
        await page_mob.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page_mob.wait_for_timeout(1000)
        await page_mob.screenshot(path=os.path.join(OUT_DIR, "navy_mobile_hero.png"))
        
        await page_mob.goto("http://localhost:5175/insights.html", wait_until="domcontentloaded")
        await page_mob.wait_for_timeout(1000)
        await page_mob.screenshot(path=os.path.join(OUT_DIR, "navy_mobile_insights.png"))
        
        await browser.close()
        print("Screenshots captured successfully!")

asyncio.run(capture())
