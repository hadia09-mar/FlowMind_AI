from app.graph.state import FlowMindState


class DocsAgent:

    def execute(self, state: FlowMindState):

        state["response"] = "Document processed successfully."

        state["status"] = "completed"

        return state