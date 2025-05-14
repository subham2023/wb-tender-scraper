from crewai import Agent
from tools.export_tool import ExporterTool

ExporterAgent = Agent(
    role='Data Exporter',
    goal='Save structured data into CSV format',
    backstory='Knows how to format and store analyzed tenders in standard formats',
    tools=[ExporterTool()],
    verbose=True
) 