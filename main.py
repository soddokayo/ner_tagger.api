from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from ner_tagger import ner_tagger
from crime_tagger import crime_tagger

class Query(BaseModel):
    sent: str

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"msg": "Usage: post '/api/ner' with json 'sent'"}

@app.post("/api/ner") # 한국어 문장 -> NER 태그하여 반환
async def api_ner(query:Query):
    res = ner_tagger(query.sent)
    print(res)
    return JSONResponse(content=jsonable_encoder(res))

@app.post("/api/crime") # 한국어 문장 -> crime keywords 태그하여 반환
async def api_crime(query:Query):
    res = crime_tagger(query.sent)
    print(res)
    return JSONResponse(content=jsonable_encoder(res))

@app.post("/api/both") # 위에꺼 두개 다 해서 반환
async def api_crime(query:Query):
    res_ner = ner_tagger(query.sent)
    res_crime = crime_tagger(query.sent)
    print(res_ner, res_crime)
    return JSONResponse(content=jsonable_encoder(res_ner+res_crime))