import asyncio
from playwright.async_api import async_playwright

async def run_full_suite():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        
        # ----------------- DESKTOP 1440x900 -----------------
        page_desk = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page_desk.goto("http://localhost:5175/", wait_until="networkidle")
        await page_desk.wait_for_timeout(800)
        
        # 1. Desktop Intro Section
        await page_desk.evaluate("const el = document.getElementById('about'); if(el) el.scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_intro.png")

        # 2. Desktop Timeline 2022
        await page_desk.evaluate("const els = document.querySelectorAll('.tl-block'); if(els.length > 2) els[2].scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_timeline_2022.png")

        # 3. Desktop Gedanken & Einblicke
        await page_desk.evaluate("const el = document.getElementById('ideas'); if(el) el.scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_insights_slider.png")

        # 4. Desktop Speaker / Future Positioning
        await page_desk.evaluate("const el = document.getElementById('contact'); if(el) el.scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_speaker_section.png")

        # 5. Desktop Contact Section
        await page_desk.evaluate("const el = document.getElementById('contact-form'); if(el) el.scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_contact.png")

        # 6. Desktop Insights Page
        await page_desk.goto("http://localhost:5175/insights.html", wait_until="networkidle")
        await page_desk.wait_for_timeout(800)
        await page_desk.evaluate("const el = document.getElementById('insights-grid'); if(el) el.scrollIntoView();")
        await page_desk.wait_for_timeout(600)
        await page_desk.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_desktop_insights_page_grid.png")

        # ----------------- TABLET 768x1024 -----------------
        page_tab = await browser.new_page(viewport={"width": 768, "height": 1024})
        await page_tab.goto("http://localhost:5175/", wait_until="networkidle")
        await page_tab.wait_for_timeout(800)

        # 7. Tablet Timeline 2022
        await page_tab.evaluate("const els = document.querySelectorAll('.tl-block'); if(els.length > 2) els[2].scrollIntoView();")
        await page_tab.wait_for_timeout(600)
        await page_tab.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_tablet_timeline_2022.png")

        # 8. Tablet Speaker Section
        await page_tab.evaluate("const el = document.getElementById('contact'); if(el) el.scrollIntoView();")
        await page_tab.wait_for_timeout(600)
        await page_tab.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_tablet_speaker.png")

        # ----------------- MOBILE 375x812 -----------------
        page_mob = await browser.new_page(viewport={"width": 375, "height": 812})
        await page_mob.goto("http://localhost:5175/", wait_until="networkidle")
        await page_mob.wait_for_timeout(800)

        # 9. Mobile Timeline 2022
        await page_mob.evaluate("const el = document.querySelector('.timeline-wrap-mob'); if(el) el.scrollIntoView();")
        await page_mob.wait_for_timeout(400)
        await page_mob.evaluate("const sw = document.querySelector('.timeline-mob').swiper; if (sw) sw.slideTo(2);")
        await page_mob.wait_for_timeout(600)
        await page_mob.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_mobile_timeline_2022.png")

        # 10. Mobile Contact Form
        await page_mob.evaluate("const el = document.getElementById('contact-form'); if(el) el.scrollIntoView();")
        await page_mob.wait_for_timeout(600)
        await page_mob.screenshot(path="/Users/aryabmishra/.gemini/antigravity/brain/ceada575-6614-43c8-b57a-42304542476b/final_mobile_contact.png")

        await browser.close()
        print("ALL VERIFICATION SCREENSHOTS CAPTURED SUCCESSFULLY!")

asyncio.run(run_full_suite())
