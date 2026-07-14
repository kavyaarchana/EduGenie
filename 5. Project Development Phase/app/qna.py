from app.ai import generate_response

def answer_question(question):
    prompt = f"""
You are EduGenie, an AI educational assistant.

Answer the following question in a clear, simple, and educational way.

Question:
{question}
"""

    return generate_response(prompt)