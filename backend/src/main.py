# FastAPI 애플리케이션 진입 파일이다.
# 공통 설정을 읽어 앱 제목을 구성하고 API 라우터를 연결한다.
# 실제 엔드포인트는 src/api 하위 모듈에서 관리한다.

from fastapi import FastAPI

from src.api.main_router import api_router
from src.core.config import settings

app = FastAPI(title=f"{settings.project_name} Backend")

# /api prefix를 포함한 메인 라우터를 앱에 등록한다.
app.include_router(api_router)
