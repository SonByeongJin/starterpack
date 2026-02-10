# 백엔드 환경설정 로더 파일이다.
# .env 및 시스템 환경변수에서 실행 설정을 읽어 Settings로 제공한다.
# 데이터 경로(DATA_*)와 포트는 추후 기능 확장을 위해 미리 포함한다.

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# 로컬 실행 시 .env 값을 먼저 읽고, 이미 설정된 환경변수는 유지한다.
load_dotenv(override=False)


@dataclass(frozen=True)
class Settings:
    app_env: str
    tz: str
    project_name: str
    portal_http_port: int
    backend_port: int
    frontend_port: int
    vite_base_path: str
    data_root: str
    data_work: str
    data_db: str
    data_logs: str


def _as_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _load_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        tz=os.getenv("TZ", "Asia/Seoul"),
        project_name=os.getenv("PROJECT_NAME", "govpage"),
        portal_http_port=_as_int("PORTAL_HTTP_PORT", 8080),
        backend_port=_as_int("BACKEND_PORT", 8000),
        frontend_port=_as_int("FRONTEND_PORT", 5173),
        vite_base_path=os.getenv("VITE_BASE_PATH", ""),
        data_root=os.getenv("DATA_ROOT", "/data"),
        data_work=os.getenv("DATA_WORK", "/data/work"),
        data_db=os.getenv("DATA_DB", "/data/db"),
        data_logs=os.getenv("DATA_LOGS", "/data/logs"),
    )


settings = _load_settings()
