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

## 혼자 작업시 conflict 해결하기

2개 이상의 컴퓨터에서 같은 원격 저장소 사용시

1. `$ git add .`

2. `$ git commit -m '메세지'`

3. `$ git push origin master`

   1. 잘 된다 => 8번으로

   2. 안된다 => 4번으로

      ```
      hint: Updates were "rejected" because the tip of your 
      current branch is behind
      hint: its remote counterpart. Integrate the remote changes (e.g.
      hint: '"git pull" ...') before pushing again.
      hint: See the 'Note about fast-forwards' in 'git push --help' for details.
      ```

4. `$ git pull origin master`

   1. 자동 병합(auto merge)이 일어난다.  =>8번으로

      - `$ git status` 에 아무런 알림이 없다.

   2. 자동 병합에 실패 => 5번으로

      ```
      ...
      Automatic merge failed; fix conflicts and then commit the result.
      
      ```

5. `vscode` 에서 직접 빨간불 들어온 파일을 수정한다.

6. `$ git add .`

7. `$ git commit -m '충돌 해결'`

8. `$ git push origin master`

   

## branch 혼자 사용하기

1. `$ git branch <branch-name>` 으로 새로운 브랜치 생성

2. `$ git switch <branch-name>` 으로 브랜치 변경

   1. `$ git switch -c <branch-name>` 으로 한번에 새로운 브랜치 생성 및 변경 가능

3. 작업 및 `add` & `commit`

4. `$ git switch master` 로 브랜치 변경

5. `$ git merge <branch-name>` 으로 병합

   1. Fast Forward => 9번으로

   2. Auto Merge => 9번으로

   3. Conflict => 6번으로

      ```
      ...
      Automatic merge failed; fix conflicts and then commit the result.
      ```

6. `vscode` 에서 직접 빨간불 들어온 파일을 수정한다.

7. `$ git add .`

8. `$ git commit -m '충돌 해결'`

9. 종료

10. `$ git branch -d <branch-name>` 으로 수명이 다한 브랜치 삭제



## branch 혼자 사용하기

1. remote 에서 리포 생성
2. collabrator 추가
3. 팀원들 각자 `clone`
4. `$ git switch -c <my-branch>` 로 각자 리포에서 브랜치 생성
5. 작업 => `add` => `commit` => 반복...
6. `$ git push origin <my-branch>`
7. 리모트에서 PR(pull request) 생성
8. 팀원들끼리 코드 리뷰 및 최종 merge 결정
   1. Auto merge 가능(초록색) => 진행
   2. Conflict 발생(빨간색) => github에서 수동으로 수정 후 merge 진행
9. 로컬 `master` 브랜치에서 `$ git pull origin master`
10. 작업 반복