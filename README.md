# starterpack

## 0) GitHub에 newpj 레포는 미리 만들어 둠 (https://github.com/<USER>/newpj)

## 1) starterpack 클론
'''python
git clone https://github.com/SonByeongJin/starterpack.git newpj
cd newpj
'''
## 2) starterpack 원격(origin) 끊기 + git 히스토리까지 새로 시작(깨끗한 신규 레포 권장)
'''python
rm -rf .git
git init
git branch -M main
'''

## 3) 새 레포 연결
'''python
git remote add origin https://github.com/<USER>/newpj.git
'''
## 4) 첫 커밋 + 푸시
'''python
git add .
git commit -m "init from starterpack"
git push -u origin main
'''