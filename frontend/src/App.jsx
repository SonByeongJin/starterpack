function App() {
  // Vite base path는 VITE_BASE_PATH 값을 기준으로 동작한다.
  // 통합 시연에서는 /{프로젝트명} 경로 하위에서 UI를 서비스한다.
  // nginx의 /{프로젝트명}/api 템플릿과 함께 경로 정책을 맞춰 사용한다.
  return (
    <main>
      <h1>Starterpack Frontend</h1>
      <p>Step 1 placeholder UI is ready.</p>
    </main>
  );
}

export default App;
