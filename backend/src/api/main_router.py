# 백엔드 API 라우터 집합 파일이다.
# 서비스별 라우터를 이곳에서 모아 앱에 단일 진입점으로 제공한다.
# prefix 정책이 필요해지면 include_router 시점에 확장한다.

from fastapi import APIRouter

from src.api.health_router import router as health_router

# 공통 API 루트 라우터: 현재는 health 엔드포인트를 포함한다.
api_router = APIRouter()
api_router.include_router(health_router)
