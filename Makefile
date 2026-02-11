# Makefile
# - 루트에서 docker compose 스택을 제어한다.
# - 프로젝트명은 -p 옵션으로 전달해 컨테이너 이름 prefix를 고정한다.
# - APP_ENV 값으로 기본 compose 파일(dev/prod)을 자동 선택한다.
-include .env

PROJECT_NAME ?= temp
APP_ENV ?= development
DEV_COMPOSE_FILE ?= docker-compose.yml
PROD_COMPOSE_FILE ?= docker-compose.prod.yml

ifeq ($(APP_ENV),production)
DEFAULT_COMPOSE_FILE := $(PROD_COMPOSE_FILE)
else
DEFAULT_COMPOSE_FILE := $(DEV_COMPOSE_FILE)
endif

COMPOSE_FILE ?= $(DEFAULT_COMPOSE_FILE)
ENV_FILE ?= .env
COMPOSE := docker compose --env-file $(ENV_FILE) -p $(PROJECT_NAME) -f $(COMPOSE_FILE)
COMPOSE_PROD := docker compose --env-file $(ENV_FILE) -p $(PROJECT_NAME) -f $(PROD_COMPOSE_FILE)

.PHONY: up down logs ps restart up-prod down-prod logs-prod

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
