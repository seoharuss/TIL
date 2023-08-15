# TIL

## 브랜치 정의
1. A branch in Git is simply a lightweight movable pointer to one of these commits.
  - 참고 : https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80
2. Git branches are effectively a pointer to a snapshot of your changes.
  - 참고 : https://www.atlassian.com/git/tutorials/using-branches

## 브랜치 합치기
- 이슈에 해당하는 작업을 수행할 때, 별도의 브랜치를 만들고 작업한다.
- 작업이 끝난 후에는, PULL REQUEST를 사용해 내가 작업한 브랜치를 중요 브랜치 (`main`, `master`, `development`, `devel`)로 병합 시켜야 한다.

### 명령어
- `git merge`
- 주의할 점 : `A`브랜치를 `B`브랜치로 병합하려 할 때는 `A`브랜치를 체크아웃 한 상태에서 `git merge B`를 입력한다.