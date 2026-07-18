class Retriever:

    @staticmethod
    def search(vectorstore, query):

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )

        return retriever.invoke(query)