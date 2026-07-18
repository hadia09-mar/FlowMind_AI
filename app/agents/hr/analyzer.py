from app.llm.gemini import llm
from app.prompts.hr_prompt import HR_PROMPT


class HRAnalyzer:

    @staticmethod
    def analyze(resume_text):

        prompt = HR_PROMPT.format(
            resume=resume_text
        )

        response = llm.invoke(prompt)

        return response.content