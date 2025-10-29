from smolagents import ToolCallingAgent
import model_utils
from campus_tools import EventsCSVTool, ScrapePageTool ,UTSiteSearchTool

def build_agent(verbose: int = 1) -> ToolCallingAgent:
    model = model_utils.google_build_reasoning_model()

    tools = [
        EventsCSVTool(),
        ScrapePageTool(),
        UTSiteSearchTool(),
    ]

    agent = ToolCallingAgent(
        tools=tools,
        model=model,
        verbosity_level=verbose,
        stream_outputs=False,
        instructions="""You are an agent to help users with questions about Utah Tech University (like a Campus agent).
        When the user asks what courses are offered, search the utah tech catalog and scrape the result. DO NOT GUESS.
        For events, always use events_csv first.
        Always include a brief “Sources:” section with one URL if you used the web. If data is from events.csv, say “Source: events.csv”.
        """
    )
    return agent


