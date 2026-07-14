from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.qna import answer_question
from app.explanation_module import explain_concept
from app.quiz_module import generate_quiz
from app.summary_module import summarize_text
from app.learning_path import generate_learning_path
from app.database import engine, get_db
from app.models import Base, User, UserQuery, AIResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/process", response_class=HTMLResponse)
async def process(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    if task == "qna":
        answer = answer_question(question)

    elif task == "explanation":
        answer = explain_concept(question)

    elif task == "quiz":
        answer = generate_quiz(question)

    elif task == "summary":
        answer = summarize_text(question)

    elif task == "learning_path":
        answer = generate_learning_path(question)

    else:
        answer = "Invalid task selected."

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "question": question,
            "answer": answer
        }
    )
