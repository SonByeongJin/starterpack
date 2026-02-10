// 포털 프론트 기본 화면 파일이다.
// 통합 시연 시 API 경로는 /{project}/api 규칙을 사용한다.
// 로컬 개발은 VITE_BASE_PATH를 비우고 /api로 호출하는 구성을 권장한다.

import { useEffect, useState } from 'react';
import axios from 'axios';

function normalizeBasePath(value) {
  const raw = (value || '').trim();
  if (!raw || raw === '/') {
    return '';
  }

  const withLeadingSlash = raw.startsWith('/') ? raw : `/${raw}`;
  return withLeadingSlash.replace(/\/+$/, '');
}

function App() {
  const [message, setMessage] = useState('loading...');

  useEffect(() => {
    const basePath = normalizeBasePath(import.meta.env.VITE_BASE_PATH);
    const API_BASE = `${basePath}/api`;

    axios
      .get(`${API_BASE}/hello`)
      .then((response) => {
        setMessage(response?.data?.message || 'api error');
      })
      .catch(() => {
        setMessage('api error');
      });
  }, []);

  return (
    <main>
      <h1>Portal Front</h1>
      <p>{message}</p>
    </main>
  );
}

export default App;
