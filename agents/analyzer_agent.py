from crewai import Agent

AnalyzerAgent = Agent(
    role='Tender Analyzer',
    goal='Extract WHAT, WHO, WHEN, and WHERE from scraped tender text',
    backstory='Reads raw data and uses LLM reasoning to structure it intelligently',
    tools=[],  # Uses just LLM
    verbose=True
) 