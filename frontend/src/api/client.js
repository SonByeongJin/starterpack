// 프론트 공통 API 클라이언트 파일이다.
// API 경로는 항상 {VITE_BASE_PATH}/api 규칙으로 고정한다.
// base path가 '/'일 때는 중복 슬래시를 제거한다.

import axios from 'axios';

const basePath = import.meta.env.VITE_BASE_PATH || '/';
const apiPrefix = import.meta.env.VITE_API_PREFIX || '/api';

const normBasePath = basePath === '/' ? '' : basePath.replace(/\/$/, '');
const normApiPrefix = apiPrefix.startsWith('/') ? apiPrefix : `/${apiPrefix}`;

export const api = axios.create({
  baseURL: `${normBasePath}${normApiPrefix}`,
  timeout: 30000,
});
