from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Locale Modules
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_pdfs_router
from routes.ask_question import router as ask_question_router
import os


app = FastAPI(
    title="Medical Assistant with RAG",
    description="API for Medical Assistant with RAG",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.middleware("http")(catch_exception_middleware)

# Routes Include
app.include_router(upload_pdfs_router)
app.include_router(ask_question_router)
