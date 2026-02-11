# starterpack

## 0) 사전 준비
- GitHub에 `newpj` 레포를 미리 생성해둔다.
  예: https://github.com/<USER>/newpj

----------------------------------------

## 1) starterpack 클론
```bash
git clone https://github.com/SonByeongJin/starterpack.git newpj
cd newpj
```
----------------------------------------

## 2) starterpack 이력 제거 + 새 Git 이력 시작 (권장: 완전 새 프로젝트로 시작)
```bash
rm -rf .git
git init
git branch -M main
```
----------------------------------------

## 3) 새 레포 연결(조직 private는 ssh 권장
SSH (권장)
```bash
git remote add origin git@github.com:<NAME>/newpj.git
```
---
HTTPS
```bash
git remote add origin https://github.com/<NAME>/newpj.git
```
----------------------------------------

## 4) 첫 커밋 + 푸시
```bash
git add .
git commit -m "init from starterpack"
git push -u origin main
```
----------------------------------------
## 5) 조직 Private 레포에서 자주 나는 오류와 해결
✅ remote: Repository not found.
(레포가 없어서가 아니라) 조직 Private 레포 권한/인증 문제일 때도 동일하게 뜸.
  - 내 계정이 레포에 Write 권한이 없음
  - HTTPS 사용 시 PAT 토큰 미설정/권한 부족
  - 조직이 SSO 사용 시 토큰/키 미승인(Authorize)

해결(가장 빠른 루트): SSH로 전환
```bash
git remote set-url origin git@github.com:<NAME>/newpj.git
git push -u origin main
```
----------------------------------------
## 6) 즉시 점검(문제 생기면 바로)
```bash
git remote -v
ssh -T git@github.com
```

ssh -T git@github.com가 성공하면 SSH 인증은 OK.
그런데도 push가 안 되면 조직 레포 권한(Write) 문제.
