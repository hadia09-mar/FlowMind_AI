from app.llm.gemini import llm
from app.prompts.research_prompt import RESEARCH_PROMPT


class ResearchAgent:

    @staticmethod
    def research(topic):

        prompt = RESEARCH_PROMPT.format(
            topic=topic
        )

        return llm.invoke(prompt).content