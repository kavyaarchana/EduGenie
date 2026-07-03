from app.ai import generate_response
def summarize_text(text):
    prompt = f"""
Summarize the following text in simple points.

{text}
"""

    return generate_response(prompt)