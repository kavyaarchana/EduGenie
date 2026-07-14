from app.ai import generate_response

def explain_concept(topic):
    prompt = f"""
Explain the following concept in a simple and beginner-friendly way.

Topic:
{topic}
"""

    return generate_response(prompt)