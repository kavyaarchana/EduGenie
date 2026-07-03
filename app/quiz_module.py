from app.ai import generate_response

def generate_quiz(topic):
    prompt = f"""
Generate 5 multiple-choice questions with answers on:

{topic}
"""

    return generate_response(prompt)