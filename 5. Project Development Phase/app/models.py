from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class UserQuery(Base):
    __tablename__ = "user_queries"

    query_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    query_type = Column(String)
    query_text = Column(Text)


class AIResponse(Base):
    __tablename__ = "ai_responses"

    response_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"))
    response_text = Column(Text)
    model_used = Column(String)


class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"))

    question_text = Column(Text)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)
    correct_answer = Column(String)


class Summary(Base):
    __tablename__ = "summaries"

    summary_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"))
    summary_text = Column(Text)


class LearningPath(Base):
    __tablename__ = "learning_paths"

    path_id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("user_queries.query_id"))

    topic = Column(String)
    difficulty_level = Column(String)
    recommended_resources = Column(Text)