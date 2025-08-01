from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #모든 출처 허용 (예: ["http://127.0.0.1:5500"])
    allow_credentials=True,
    allow_methods=["*"],  #모든 HTTP 메서드 허용
    allow_headers=["*"],  #모든 헤더 허용
)

@app.post("/run-python")
async def run_python():
    try:
        result = subprocess.run(
            ['python', 'test1/crawling.py'],#실행하는 파이썬 코드, 현재 위치 기준 파일
            capture_output=True,
            text=True,
            check=True # 오류 발생 시 CalledProcessError 예외 발생
        )
        return JSONResponse(content={
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode,
            'result': 'Python script executed successfully' # 클라이언트가 기대하는 'result' 필드 추가
        })
    except subprocess.CalledProcessError as e:
        # 스크립트 실행 중 오류가 발생한 경우
        return JSONResponse(
            content={
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': e.returncode,
                'error': 'Failed to execute Python script'
            },
            status_code=500 # 내부 서버 오류 상태 코드 반환
        )
    except Exception as e:
        # 기타 예외 처리
        return JSONResponse(
            content={
                'error': f"An unexpected error occurred: {str(e)}"
            },
            status_code=500
        )

# 이 파일을 직접 실행할 때 (예: python your_fastapi_app.py) Uvicorn으로 실행
# 개발 시에는 터미널에서 'uvicorn your_fastapi_app:app --reload --port 5000' 명령어를 사용합니다.
# (여기서 'your_fastapi_app'은 이 파일의 이름입니다.)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
