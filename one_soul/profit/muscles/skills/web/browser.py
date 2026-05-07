import logging
import asyncio
from playwright.async_api import async_playwright
from one_soul.profit.muscles.registry import Skill

logger = logging.getLogger("BrowserSkill")

class BrowserSkill(Skill):
    name = "browser_action"
    description = "Advanced browser automation using Playwright for full web autonomy."

    async def execute(self, url: str, actions: list = None) -> dict:
        """
        Execute complex actions in a real browser.
        actions: list of dicts like {'type': 'click', 'selector': '#login'}
        """
        logger.info(f"Opening browser to: {url}")
        results = {"screenshot": None, "content": "", "errors": []}

        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                await page.goto(url, wait_until="networkidle")

                if actions:
                    for action in actions:
                        try:
                            a_type = action.get("type")
                            selector = action.get("selector")
                            value = action.get("value")

                            if a_type == "click":
                                await page.click(selector)
                            elif a_type == "fill":
                                await page.fill(selector, value)
                            elif a_type == "wait":
                                await asyncio.sleep(float(value))

                            await page.wait_for_load_state("networkidle")
                        except Exception as ae:
                            results["errors"].append(f"Action {a_type} failed: {ae}")

                results["content"] = await page.content()
                # Optional: results["screenshot"] = await page.screenshot()

                await browser.close()
                return results
        except Exception as e:
            logger.error(f"Browser automation failed: {e}")
            return {"errors": [str(e)]}
