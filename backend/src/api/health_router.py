# 헬스체크 전용 라우터 파일이다.
# 컨테이너/리버스프록시 연동 확인용 최소 엔드포인트를 제공한다.
# 기본 prefix 없이 /health 경로로 응답한다.

from fastapi import APIRouter

# 헬스체크 라우터: 운영 점검 시 가장 먼저 호출하는 엔드포인트다.
router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
