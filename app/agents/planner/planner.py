import json

from app.graph.state import FlowMindState
from app.llm.gemini import llm
from app.prompts.planner_prompt import PLANNER_PROMPT


class PlannerAgent:

    def plan(self, state: FlowMindState):

        prompt = PLANNER_PROMPT.format(
            request=state["request"]
        )

        response = llm.invoke(prompt)

        from app.utils.json_parser import parse_json_response

        result = parse_json_response(response.content)

        state["plan"] = result["plan"]

        state["status"] = "planned"

        return state