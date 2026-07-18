from app.graph.state import FlowMindState


class HRAgent:

    def execute(self, state: FlowMindState) -> FlowMindState:

        state["response"] = "Resume analyzed successfully."

        state["status"] = "completed"

        return state