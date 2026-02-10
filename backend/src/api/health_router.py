# 기본 동작 확인용 엔드포인트 라우터 파일이다.
# /api/health와 /api/hello를 제공해 프론트/프록시 연동을 검증한다.
# 별도 prefix 없이 메인 라우터(/api)에 결합되어 노출된다.

from fastapi import APIRouter

# 상태 점검/샘플 응답 라우터다.
router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, bool]:
    return {"ok": True}


@router.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "hello world"}
