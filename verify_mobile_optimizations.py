import asyncio
import os
from playwright.async_api import async_playwright

OUT_DIR = "/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/mobile_verified"
os.makedirs(OUT_DIR, exist_ok=True)

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        
        # ----------------- MOBILE 390x844 -----------------
        page = await browser.new_page(viewport={"width": 390, "height": 844})
        await page.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # 1. Hero
        await page.screenshot(path=os.path.join(OUT_DIR, "01_hero.png"))
        
        # 2. Open Menu
        await page.click("#menu-trigger")
        await page.wait_for_timeout(500)
        await page.screenshot(path=os.path.join(OUT_DIR, "02_menu_open.png"))
        await page.click("#menu-trigger")
        await page.wait_for_timeout(500)
        
        # 3. About
        await page.evaluate("() => document.getElementById('about').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "03_about.png"))
        
        # 4. Work / Key blocks
        await page.evaluate("() => document.getElementById('work').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "04_work.png"))
        
        # 5. Timeline
        await page.evaluate("() => document.querySelector('.timeline-wrap-mob').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "05_timeline.png"))
        
        # 6. Ideas
        await page.evaluate("() => document.getElementById('ideas').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "06_ideas.png"))
        
        # 7. Speaker (Fixed collision check)
        await page.evaluate("() => document.getElementById('contact').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "07_speaker.png"))
        
        # 8. Connect (Schedule a Call)
        await page.evaluate("() => document.getElementById('connect').scrollIntoView({ behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "08_connect.png"))
        
        # 9. Footer
        await page.evaluate("() => window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "09_footer.png"))
        
        # ----------------- DESKTOP VERIFICATION (1440x900) -----------------
        page_desk = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page_desk.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page_desk.wait_for_timeout(1000)
        await page_desk.screenshot(path=os.path.join(OUT_DIR, "10_desktop_hero.png"))
        
        await page_desk.evaluate("() => document.getElementById('contact').scrollIntoView({ behavior: 'smooth' })")
        await page_desk.wait_for_timeout(800)
        await page_desk.screenshot(path=os.path.join(OUT_DIR, "11_desktop_speaker.png"))
        
        await browser.close()
        print("All mobile and desktop verification screenshots captured!")

asyncio.run(verify())
