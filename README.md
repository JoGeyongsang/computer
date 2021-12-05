# git 01

## NEVER

1. `~` 에서 `$ git init` 진행
2. 리포 안에 리포 만들기
3. **`$ git init` 입력 전 확인할 점**
   1. `~` 인지
   2. `(master)` 떠 있는지

## 프로젝트 초기화 진행

```sh
# pjt 폴더 생성
$ mkdir new_project

# 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore
# gitignore.io 에 접속하여 필요한 내용 복-붙

# 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# 원격 저장소 생성 @ github.com
# 생성한 원격 저장소 등록
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit push
$ git push origin master
```

### 계정 세팅

```sh
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig  
```



## 명령어 정리

- 초기화 시점에 1회 입력

```sh
$ git init 
```

- 작업중

```sh
$ git add <filename>
$ git commit -m 'MESSAGE'
```

- 모니터링 명령어

```sh
$ git status  # 현재 상황
$ git log     # commit 로그 
```

- github 에 원격 저장소 생성하기
- 원격 저장소(remote repo) 추가하기

```sh
$ git remote add origin <URL>
```

- 원격 저장소 확인하기

```sh
$ git remote -v
```

- 원격 저장소에 지금까지의 commit 들 PUSH 하기

```sh
$ git push origin master
```

- 새로운 컴퓨터에서 기존 원격 저장소 복제하기
```sh
$ git clone <URL>
```

- 원격 저장소의 내용 받아오기
```sh
$ git pull origin master
```

# git 02
그러나 반가시당 충돌
2개 이상의 컴퓨터에서 같은 원격 저장소 사용시

$ git add .

$ git commit -m '메세지'

$ git push origin master

잘 된다 => 8번으로

안된다 => 4번으로

hint: Updates were "rejected" because the tip of your 
current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: '"git pull" ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
$ git pull origin master

자동 병합 (자동 병합)이 일대. =>8번으로

$ git status 에 아무런 알림이 없다.
자동 병합에 실패 => 5번으로

...
Automatic merge failed; fix conflicts and then commit the result.

vscode 에서 직접 빨간불 들어온 파일을 수정한다.

$ git add .

$ git commit -m '충돌 해결'

$ git push origin master

지점 오이스 오이스
$ git branch <branch-name> 으로 새로운 브랜치 생성

$ git switch <branch-name> 으로 브랜치 변경

$ git switch -c <branch-name> 으로 한번에 새로운 브랜치 생성 및 변경 가능
작업 및 add & commit

$ git switch master 로 브랜치 변경

$ git merge <branch-name> 으로 병합

Fast Forward => 9번으로

Auto Merge => 9번으로

Conflict => 6번으로

...
Automatic merge failed; fix conflicts and then commit the result.
vscode 에서 직접 빨간불 들어온 파일을 수정한다.

$ git add .

$ git commit -m '충돌 해결'

종료

$ git branch -d <branch-name> 으로 수명이 다한 브랜치 삭제

지점 오이스 오이스
리모트 리모트 리모트 포포
콜라브라토르
팀원들 각자 clone
$ git switch -c <my-branch> 로 각자 리포에서 브랜치 생성
작업 => => => 반복...addcommit
$ git push origin <my-branch>
리모에이드홍보(풀요청) []
아침리리 리 드 드 리 수리 비에이드, 결합 한 수
자동 병합(초초)=>
충돌 (적) = > github 거머리수당 부수 합병 후진
로컬 브랜치에서 master$ git pull origin master
작업 반복