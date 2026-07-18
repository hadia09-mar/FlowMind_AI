from langgraph.graph import StateGraph, END

from app.graph.state import FlowMindState
from app.agents.planner.planner import PlannerAgent
from app.agents.router.router import RouterAgent
from app.agents.hr.hr_agent import HRAgent
from app.agents.docs.docs_agent import DocsAgent
from app.agents.research.research_agent import ResearchAgent

planner = PlannerAgent()
router = RouterAgent()
hr = HRAgent()
docs = DocsAgent()
research = ResearchAgent()

builder = StateGraph(FlowMindState)

builder.add_node("planner", planner.plan)
builder.add_node("router", router.route)
builder.add_node("hr", hr.execute)
builder.add_node("docs", docs.execute)
builder.add_node("research", research.execute)

builder.set_entry_point("planner")

builder.add_edge("planner", "router")
builder.add_conditional_edges(
    "router",
    lambda state: state["current_agent"],
    {
        "hr": "hr",
        "docs": "docs",
        "research": "research",
    },
)

builder.add_edge("hr", END)
builder.add_edge("docs", END)
builder.add_edge("research", END)

graph = builder.compile()