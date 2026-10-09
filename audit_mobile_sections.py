import asyncio
import os
from playwright.async_api import async_playwright

OUT_DIR = "/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/mobile_audit"
os.makedirs(OUT_DIR, exist_ok=True)

async def audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        page = await browser.new_page(viewport={"width": 390, "height": 844})
        await page.goto("http://localhost:5175/", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        
        # 1. Mobile Hero
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(400)
        await page.screenshot(path=os.path.join(OUT_DIR, "01_hero.png"))
        
        # 2. Burger Menu Open
        await page.click("#menu-trigger")
        await page.wait_for_timeout(500)
        await page.screenshot(path=os.path.join(OUT_DIR, "02_menu_open.png"))
        # Close menu
        await page.click("#menu-trigger")
        await page.wait_for_timeout(500)
        
        # 3. Intro / About
        await page.evaluate("() => { const el = document.getElementById('about'); el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "03_about.png"))
        
        # 4. Work / Key Blocks
        await page.evaluate("() => { const el = document.getElementById('work'); el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "04_work.png"))
        
        # 5. Mobile Timeline
        await page.evaluate("() => { const el = document.querySelector('.timeline-wrap-mob'); if(el) el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "05_timeline.png"))
        
        # 6. Ideas / News Slider
        await page.evaluate("() => { const el = document.getElementById('ideas'); if(el) el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "06_ideas.png"))
        
        # 7. Speaker / Philosophy
        await page.evaluate("() => { const el = document.getElementById('contact'); if(el) el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "07_speaker.png"))
        
        # 8. Connect / Schedule a Call
        await page.evaluate("() => { const el = document.getElementById('connect'); if(el) el.scrollIntoView({ behavior: 'instant', block: 'start' }); }")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "08_connect.png"))
        
        # 9. Footer Social & Footer
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(800)
        await page.screenshot(path=os.path.join(OUT_DIR, "09_footer.png"))
        
        await browser.close()
        print("Mobile audit complete!")

asyncio.run(audit())
