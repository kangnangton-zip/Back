from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
#import subprocess
import hackiye_def
app = FastAPI()
import webbrowser as w
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server 주소
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

@app.get("/")
async def get_sites():
    return {'Hello':'World'}
@app.get("/api/google")
async def get_sites():
    lst = []
    lst.append(hackiye_def.dark())
    lst.append(hackiye_def.hibp("01034762742ab@gmail.com"))
    lst.append(str(hackiye_def.google()))
    #w.open('http://localhost:5173/google/result')
    # google = hackiye_def.google()
    # for g in google:
    #     lst.append(g)
    return [#python 코드 결과 리턴
        lst
        # {"id": 1, "name": "대성마이맥", "date": "2025-05-01"},
        # {"id": 2, "name": "아디다스", "date": "2025-06-15"e},

    ]

@app.get("/api/naver")
async def get_sites():
    lst = []
    lst.append(hackiye_def.hibp("netstat3476@naver.com"))
    # lst.append(hackiye_def.naver())
    naver = hackiye_def.naver()
    for n in naver:
        lst.append(n)
    #w.open('http://localhost:5173/naver/result')
    return [#python 코드 결과 리턴
        lst
        # {"id": 1, "name": "대성마이맥", "date": "2025-05-01"},
        # {"id": 2, "name": "아디다스", "date": "2025-06-15"},
    ]