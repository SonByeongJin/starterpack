# 백엔드 공통 설정 로더 파일이다.
# 환경변수에서 최소 실행 설정만 읽어 Settings 객체로 노출한다.
# 상세 설정은 Step 2 이후 필요한 항목을 점진적으로 추가한다.

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    project_name: str


def _load_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        project_name=os.getenv("PROJECT_NAME", "govpage"),
    )


settings = _load_settings()
