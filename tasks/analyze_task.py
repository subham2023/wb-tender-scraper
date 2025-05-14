from crewai import Task
import json

def build_analyze_task(agent):
    with open("data/raw_tenders.json", "r") as f:
        tender_data = json.load(f)

    joined_text = "\n".join(
        [f"Title: {item['title']}\nLink: {item['link']}" for item in tender_data]
    )

    prompt = f"""
Below is a list of tender titles and links from West Bengal. For each tender, extract:

- What is the construction work?
- Who is issuing the tender (department/agency)?
- When is the work expected or deadline?
- Where is the location?

Return in this CSV format (no headers):

What,Who,When,Where

Tender List:
{joined_text}
"""

    return Task(
        description="Analyze tender data and extract structured answers: What, Who, When, Where",
        expected_output="A CSV string containing tender info in format: What,Who,When,Where",
        agent=agent,
        input=prompt
    ) 