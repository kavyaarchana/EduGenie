from app.ai import generate_response
def generate_learning_path(topic):
    prompt = f"""
Create a learning roadmap for:

{topic}

Include:
- Beginner
- Intermediate
- Advanced
- Recommended resources
"""
    return generate_response(prompt)