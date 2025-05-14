from crewai import Agent
from tools.scraper_tool import TenderScraperTool

ScraperAgent = Agent(
    role='Tender Scraper',
    goal='Scrape latest tenders from West Bengal eProcurement portal',
    backstory='Expert at navigating websites and collecting structured data',
    tools=[TenderScraperTool()],
    verbose=True
) 