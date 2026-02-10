// Vite 빌드 설정 파일이다.
// 정적 자산 경로는 VITE_BASE_PATH를 기준으로 생성한다.
// 프로덕션에서는 /{PROJECT_NAME}/ 형태의 base를 사용한다.

import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

function normalizeBasePath(value) {
  const raw = (value || '').trim();
  if (!raw || raw === '/') {
    return '/';
  }

  const withLeadingSlash = raw.startsWith('/') ? raw : `/${raw}`;
  const withoutTrailingSlash = withLeadingSlash.replace(/\/+$/, '');
  return `${withoutTrailingSlash}/`;
}

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');

  return {
    plugins: [react()],
    base: normalizeBasePath(env.VITE_BASE_PATH),
  };
});
