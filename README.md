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

## 3) 새 레포 연결
```bash
git remote add origin https://github.com/<USER>/newpj.git
```
----------------------------------------

## 4) 첫 커밋 + 푸시
```bash
git add .
git commit -m "init from starterpack"
git push -u origin main
```