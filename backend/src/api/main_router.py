# 백엔드 메인 라우터 파일이다.
# 모든 API 엔드포인트를 /api prefix 아래로 통합한다.
# 서비스별 라우터는 이 파일에서 include_router로 모은다.

from fastapi import APIRouter

from src.api.health_router import router as health_router

# 공통 API prefix 라우터다.
api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)
