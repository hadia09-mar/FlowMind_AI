from app.llm.gemini import llm
from app.prompts.rag_prompt import RAG_PROMPT


class DocumentQA:

    @staticmethod
    def answer(question, documents):

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        response = llm.invoke(prompt)

        return response.content