# Makefile
# - 루트에서 docker compose 스택을 제어한다.
# - 프로젝트명은 -p 옵션으로 전달해 컨테이너 이름 prefix를 고정한다.
# - 개발/프로덕션 compose 파일을 각각 분리해 실행한다.
-include .env

PROJECT_NAME ?= govpage

COMPOSE_FILE ?= compose/docker-compose.yml
PROD_COMPOSE_FILE ?= compose/docker-compose.prod.yml
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

# 프로덕션 실행
up-prod:
	$(COMPOSE_PROD) up -d --build

# 프로덕션 종료
down-prod:
	$(COMPOSE_PROD) down

# 프로덕션 로그
logs-prod:
	$(COMPOSE_PROD) logs -f --tail=200
