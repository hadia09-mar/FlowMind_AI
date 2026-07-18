from langchain_chroma import Chroma

from app.knowledge.embeddings import embeddings


class VectorStore:

    @staticmethod
    def create(documents):

        return Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory="./chroma_db",
        )