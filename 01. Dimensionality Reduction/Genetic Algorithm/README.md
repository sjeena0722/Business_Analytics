# Genetic Algorithm
* generation의 재생산을 반복하여 superior solution을 찾는 방법론

### 핵심적인 요소
* Selection (선택) : solution의 quality를 높일 수 있는 후보군 찾기
* Crossover (교배) : 앞 선 세대의 quality가 우수한 유전자들을 섞어 더 좋은 대안이 있는지 탐색
* Mutation (돌연변이) : local optimum에서 빠져나와서 global optimum으로 갈 수 있는 기회를 만듦

### 절차
![image](https://user-images.githubusercontent.com/80257035/195516461-33e3f43e-0fd9-47fd-94f4-7a45abdb2d42.png)

### Step 1 : Initialization
* 각각의 gene에 random number(0과 1 사이의 값)를 부여 
![image](https://user-images.githubusercontent.com/80257035/195516750-8edb9e2d-3bba-4a1d-84a7-a944fde66051.png)

* Cut-off를 기준으로 Random number를 binary value로 변환 ex) cut-off = 0.5
![image](https://user-images.githubusercontent.com/80257035/195517060-a1a50e2c-5709-4c99-9cb9-ac7945962fe5.png)
