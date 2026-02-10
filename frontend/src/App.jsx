// 포털 프론트 기본 화면 파일이다.
// 통합 시연 시 API는 항상 /{project}/api 규칙으로 호출한다.
// 실제 호출은 공통 API 클라이언트(fetchHello) 경유로만 수행한다.

import { useEffect, useState } from 'react';
import { fetchHello } from './api/hello';

export default function App() {
  const [text, setText] = useState('loading...');

  useEffect(() => {
    fetchHello()
      .then((data) => setText(typeof data === 'string' ? data : JSON.stringify(data)))
      .catch((e) => setText(`API error: ${e?.message || 'unknown'}`));
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Portal Front</h1>
      <p>{text}</p>
    </div>
  );
}
