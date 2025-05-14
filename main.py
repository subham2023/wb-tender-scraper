from crewai import Crew, Task
from agents.scraper_agent import ScraperAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.exporter_agent import ExporterAgent
from tasks.analyze_task import build_analyze_task
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure LLM
llm = ChatOpenAI(
    model_name=os.getenv("MODEL_NAME", "gpt-4"),
    temperature=float(os.getenv("TEMPERATURE", "0.7")),
    api_key=os.getenv("OPENAI_API_KEY")
)

def main():
    # Initialize agents
    scraper = ScraperAgent
    analyzer = AnalyzerAgent
    exporter = ExporterAgent

    # Define tasks
    scraping_task = Task(
        description="Scrape tender information from wbtenders.gov.in",
        agent=scraper
    )

    analysis_task = build_analyze_task(analyzer)

    export_task = Task(
        description="Export the structured data to CSV format",
        agent=exporter
    )

    # Create and run the crew
    crew = Crew(
        agents=[scraper, analyzer, exporter],
        tasks=[scraping_task, analysis_task, export_task],
        verbose=True,
        llm=llm
    )

    result = crew.kickoff()
    print("Scraping completed successfully!")

if __name__ == "__main__":
    main() 