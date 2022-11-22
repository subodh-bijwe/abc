from fastapi import FastAPI, Request, Form, Body
from fastapi.middleware.cors import CORSMiddleware
from src.cu_flow import CUFlow
import requests_cache

CUFLOW = CUFlow()

app = FastAPI()
requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/paragraph_grammar/health_check")
async def hc():
    #print("health check %%%%")
    return {"Status": "Congratulations! Paragraph Grammar Service is Up and Running."}

@app.post("/paragraph_grammar/parse_paragraph/")
async def solutionparagraph(request: Request, para: dict=Body("")):
    auth_token = request.headers['Authorization']
    lang = request.headers.get("accept-language", "en").lower()
    #print('paragraph recieved', para, auth_token)
    return CUFLOW.get_cu_flow(para['para'], auth_token, lang)
