# Genetic Algorithm
* generation의 재생산을 반복하여 superior solution을 찾는 방법론

### 핵심적인 요소
* Selection (선택) : solution의 quality를 높일 수 있는 후보군 찾기
* Crossover (교배) : 앞 선 세대의 quality가 우수한 유전자들을 섞어 더 좋은 대안이 있는지 탐색
* Mutation (돌연변이) : local optimum에서 빠져나와서 global optimum으로 갈 수 있는 기회를 만듦

### 절차
![image](https://user-images.githubusercontent.com/80257035/195516461-33e3f43e-0fd9-47fd-94f4-7a45abdb2d42.png)

---

### Step 1 : Initialization
* 각각의 gene에 random number(0과 1 사이의 값)를 부여 
![image](https://user-images.githubusercontent.com/80257035/195516750-8edb9e2d-3bba-4a1d-84a7-a944fde66051.png)

* Cut-off를 기준으로 Random number를 binary value로 변환 ex) cut-off = 0.5
![image](https://user-images.githubusercontent.com/80257035/195517060-a1a50e2c-5709-4c99-9cb9-ac7945962fe5.png)

---

### Step 2 : 각 염색체 선택 변수 별 모델 학습
* Multivariate linear regression (MLP)라고 가정
![image](https://user-images.githubusercontent.com/80257035/195517480-962b10c2-0ca3-4178-a575-bc6b6c56c484.png)
같은 방식으로 총 4개의 MLR을 학습함

---

### Step 3 : Fitness evaluation
* Fitness Function : 어떤 chromosome이 더 좋은가를 평가하는 기준, Fitness values가 높을 수록 좋은 chromosomes

ex) Fitness function = Adjusted $𝑅^2$
![image](https://user-images.githubusercontent.com/80257035/195517807-d4c36d85-c5e2-41a0-8fbf-263d131f42f6.png)

---

### Step 4 : Selection
* 현재 population 중 우수한 chromosome 선택하여 다음 세대의 population을 생산하는 단계

1️⃣ ***Deterministic Selection***
 * 상위 N%의 chromosome만 선택됨
 * 그 밑은 폐기
ex) 상위 50% 선택
![image](https://user-images.githubusercontent.com/80257035/195541185-94b5ce45-d1c7-40ac-bd9a-214ce41a5d06.png)

2️⃣ ***Probabilistic Selection***
 * 모든 chromosome에게 유전자를 넘겨줄 수 있는 기회를 줌
 * Fitness values가 높았던 chromosome이 높은 확률을 가짐
![image](https://user-images.githubusercontent.com/80257035/195541350-5af9c8ee-b971-4ebb-ba7c-a0b16077bf85.png)

---

### Step 5 : Crossover & Mutation

1️⃣ ***Crossover***

![image](https://user-images.githubusercontent.com/80257035/195542137-847ca4a4-8590-4030-bdb7-7bdd041282fb.png)
(사진 출처 : https://post.naver.com/viewer/postView.nhn?volumeNo=22462557&memberNo=1474987)
* Single Point Crossover Operator : crossover point가 1인 경우
* Multi-Point Crossover Operator : crossover point가 2개 이상인 경우
* Uniform Crossover Operator : random number 생성한 후 threshold보다 큰 것만 crossover

2️⃣ ***Mutation***
* 목적 : Local optimum에 빠질 수 있는 위험을 제거하고 탈출 할 수 있는 기회를 줌
* 주의할 점 : 너무 큰 mutation rate를 사용하면 수렴하는 데 시간이 오래 걸림 (0.01정도가 좋음)

![image](https://user-images.githubusercontent.com/80257035/195542826-e1f6a96b-7766-4679-8784-bc45c8228ade.png)

---

### Step 6 : Find the Best Solution
* 세대가 지나면서 높은 fitness value를 갖는 chromosome이 선택됨(=중요 변수들로 이루어진 부분 집합이 선택됨)
![image](https://user-images.githubusercontent.com/80257035/195543513-603f2f78-6202-4647-bfd2-ccb35fd67d62.png)


