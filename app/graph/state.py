from typing import TypedDict, List, Optional


class FlowMindState(TypedDict):
    request: str
    current_agent: Optional[str]
    response: Optional[str]
    documents: List[str]
    status: str
    history: List[str]
    plan: List[str]