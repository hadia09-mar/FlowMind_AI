from app.graph.state import FlowMindState


class RouterAgent:

    def route(self, state: FlowMindState):

        first_task = state["plan"][0]

        if first_task.startswith("resume") or first_task.startswith("candidate") or first_task.startswith("interview"):
            state["current_agent"] = "hr"

        elif first_task.startswith("document"):
            state["current_agent"] = "docs"

        elif first_task.startswith("web") or first_task.startswith("market"):
            state["current_agent"] = "research"

        else:
            state["current_agent"] = "general"

        return state