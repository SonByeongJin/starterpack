.PHONY: help up down build logs shell test lint

# 기본: make 입력 시 도움말 출력
help:
	@echo ""
	@echo "사용 가능한 명령어:"
	@echo ""
	@echo "  make up       - 컨테이너 시작"
	@echo "  make down     - 컨테이너 종료"
	@echo "  make build    - 이미지 재빌드 (의존성 변경 후)"
	@echo "  make logs     - 로그 확인"
	@echo ""
	@echo "  make shell    - 백엔드 컨테이너 접속"
	@echo "  make test     - 테스트 실행"
	@echo "  make lint     - 린트 실행"
	@echo ""

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

shell:
	docker compose exec backend bash

test:
	docker compose exec backend pytest

lint:
	docker compose exec backend ruff check . --fix
	docker compose exec frontend npm run lint
