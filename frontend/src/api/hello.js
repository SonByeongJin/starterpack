// hello 샘플 호출 전용 API 파일이다.
// backend의 /hello 엔드포인트를 조회해 응답 데이터를 반환한다.

import { api } from './client';

export async function fetchHello() {
  const res = await api.get('/hello');
  return res.data;
}
