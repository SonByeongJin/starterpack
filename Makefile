# Makefile
# - 루트에서 docker compose 스택을 제어한다.
# - .env의 APP_ENV 값을 기준으로 dev/prod compose 파일을 자동 선택한다.
# - 필요하면 COMPOSE_FILE=... 로 compose 파일을 강제 지정할 수 있다.
-include .env

APP_ENV ?= development

ifeq ($(APP_ENV),production)
DEFAULT_COMPOSE_FILE := compose/docker-compose.prod.yml
else
DEFAULT_COMPOSE_FILE := compose/docker-compose.yml
endif

# 필요하면: COMPOSE_FILE=compose/docker-compose.yml make up
COMPOSE_FILE ?= $(DEFAULT_COMPOSE_FILE)
COMPOSE := docker compose -f $(COMPOSE_FILE)

.PHONY: up down logs ps restart

# 실행
up:
	$(COMPOSE) up -d --build

# 종료
down:
	$(COMPOSE) down

# 로그
logs:
	$(COMPOSE) logs -f --tail=200

# 상태
ps:
	$(COMPOSE) ps

# 재시작
restart:
	$(COMPOSE) down
	$(COMPOSE) up -d --build
