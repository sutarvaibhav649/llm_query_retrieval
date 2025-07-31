def generate_prompt(query: str, context_chunks: list[str]) -> str:
    context = "\n---\n".join(context_chunks)
    return f"""
You are a policy assistant. Use only the below context to answer the query.

Context:
{context}

Question: {query}
Answer:"""
