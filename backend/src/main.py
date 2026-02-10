# FastAPI 엔트리포인트 파일이다.
# 앱 인스턴스를 만들고 메인 API 라우터를 등록한다.
# 실제 업무 라우트는 src/api 하위 모듈에 추가한다.

from fastapi import FastAPI

from src.api.main_router import api_router
from src.core.config import settings

app = FastAPI(title=f"{settings.project_name} Backend")

# 백엔드 기본 API prefix 루트 라우터를 등록한다.
app.include_router(api_router)
