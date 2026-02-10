# 프론트 이미지 빌드 파일이다.
# dev 스테이지는 Vite 개발 서버, prod 스테이지는 nginx 정적 서빙을 사용한다.
# prod 빌드 base 경로는 VITE_BASE_PATH로 주입한다.

FROM node:20-alpine AS base

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install

FROM base AS build
ARG VITE_BASE_PATH=/govpage/
ENV VITE_BASE_PATH=${VITE_BASE_PATH}
COPY . .
RUN npm run build

FROM nginx:alpine AS prod
COPY nginx.conf /etc/nginx/templates/default.conf.template
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80

FROM base AS dev
COPY . .
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
