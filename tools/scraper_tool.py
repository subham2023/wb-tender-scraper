from crewai_tools import BaseTool
from playwright.sync_api import sync_playwright
import json
import os

class TenderScraperTool(BaseTool):
    name = "WestBengalTenderScraper"
    description = "Scrapes latest tenders from the West Bengal eProcurement portal"
    
    def _run(self, query: str = "") -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://wbtenders.gov.in/nicgep/app?page=FrontEndTendersByOrganisation&service=page")

            # Wait and scrape tender rows
            page.wait_for_selector("table[class*='list_table']")
            tenders = page.query_selector_all("table.list_table tbody tr")

            results = []
            for tender in tenders[:10]:  # Limit to 10 latest tenders
                cols = tender.query_selector_all("td")
                if len(cols) >= 2:
                    title = cols[1].inner_text().strip()
                    link = cols[1].query_selector("a").get_attribute("href")
                    full_link = f"https://wbtenders.gov.in{link}" if link else ""
                    results.append({"title": title, "link": full_link})

            browser.close()

        os.makedirs("data", exist_ok=True)
        with open("data/raw_tenders.json", "w") as f:
            json.dump(results, f, indent=2)

        return f"Scraped {len(results)} tenders. Data saved to 'data/raw_tenders.json'." 