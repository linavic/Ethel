import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Absolute path to index.html
        file_path = "file://" + os.path.abspath("index.html")

        # Verify Desktop
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.goto(file_path)
        await page.screenshot(path="screenshot_desktop.png", full_page=True)
        print("Desktop screenshot captured.")

        # Verify Mobile
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.goto(file_path)
        await page.screenshot(path="screenshot_mobile.png", full_page=True)
        print("Mobile screenshot captured.")

        # Check for Lottery Calculator
        lottery = await page.query_selector(".lottery-container")
        if lottery:
            print("Lottery container found.")
        else:
            print("Lottery container NOT found.")

        # Check for Lead Form
        form = await page.query_selector("#mainContactForm")
        if form:
            print("Contact form found.")
        else:
            print("Contact form NOT found.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
