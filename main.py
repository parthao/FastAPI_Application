from fastapi import FastAPI
from app.api import items
from app.api import pdfreader
from app.api import textreader
from app.api import answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multi-layered FastAPI Example")

# Allow requests from your frontend origin
origins = [
    "http://localhost:3000", "http://192.168.1.8:3000" # React frontend
    # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)


app.include_router(items.router)
app.include_router(pdfreader.router)
app.include_router(textreader.router)
app.include_router(answer.router)