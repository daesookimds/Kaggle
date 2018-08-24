<img src="image/title.png" alt="subject_image" width="650" height="150">

```Project Period : 2018.06.14 ~ 2018.07.08```

```선형회귀로 풀어보는 질로우 집 가치 예측 (Zillow's Home Value Prediction using LinearRegression)```

### Aim of Regression
- Predict Zestimate value(Zillow's own model for predict house value)


### Data Description
- train_2016_v2.csv : 90275 rows, 3 columns(parcelid,	logerror,	transactiondate)
- train_2017.csv : 77613 rows, 3 columns(parcelid,	logerror,	transactiondate)
- properties_2016.csv : 2985217 rows, 58 columns
- properties_2017.csv : 2985217 rows, 58 columns
- sample_submission.csv


### File Description
- columns_dictionary_2016.ipynb : classify type of value for each 58 columns (category / scalar)
    ```columns_dictionary_2016.ipynb : 특성(열)의 데이터 종류를 카테고리와 수치를 나타내는 숫자 값으로 분류한 2016년 사전```

- columns_dictionary_2017.ipynb : classify type of value for each 58 columns (category / scalar)
    ```columns_dictionary_2017.ipynb : 특성(열)의 데이터 종류를 카테고리와 수치를 나타내는 숫자 값으로 분류한 2017년 사전```

- LinearRegression_model_2016.ipynb : LinearRegression model for 2016
    ```LinearRegression_model_2016.ipynb : scikit-learn의 선형회귀 모델을 사용하여 만든 2016년 zillow 모델 (propeties2016년 사용)```
    
- LinearRegression_model_2017.ipynb : LinearRegression model for 2017
    ```LinearRegression_model_2017.ipynb : scikit-learn의 선형회귀 모델을 사용하여 만든 2017년 zillow 모델 (properties2017 사용)```
    
    
### Preprocessing

1. fill in mssing value

- Category data
    - fill in missing value with most frequent value
- Scalar data
    - fill in missing value using MICEdata imputation

2. Featrue Selection

- Select only those that are linearly correlated with our target 'logerror'


### Model

- LinearRegression of sklearn


### Result

- 2666 / 3779 : top 70%

<img src="image/score.png" alt="subject_image" width="600" height="100">

### Feedback

- Initially there was a constraint that the project only use linear model
- If I try a nonlinear model, I'll get better results.



----------------------------------------------------------------------------------------------

```프로젝트 기간 : 2018.06.14 ~ 2018.07.08```

```선형회귀로 풀어보는 질로우 집 가치 예측 (Zillow's Home Value Prediction using LinearRegression)```

### 회귀 목적
- Zillow사가 만든 Zestimate 모델이 측정한 집값을 예측하기


### 데이터 설명
- train_2016_v2.csv : 90275 행, 3 열(parcelid,	logerror,	transactiondate)
- train_2017.csv : 77613 행, 3 열(parcelid,	logerror,	transactiondate)
- properties_2016.csv : 2985217 행, 58 열
- properties_2017.csv : 2985217 행, 58 열
- sample_submission.csv


### 파일 설명
- columns_dictionary_2016.ipynb : classify type of value for each 58 columns (category / scalar)
    ```columns_dictionary_2016.ipynb : 특성(열)의 데이터 종류를 카테고리와 수치를 나타내는 숫자 값으로 분류한 2016년 사전```

- columns_dictionary_2017.ipynb : classify type of value for each 58 columns (category / scalar)
    ```columns_dictionary_2017.ipynb : 특성(열)의 데이터 종류를 카테고리와 수치를 나타내는 숫자 값으로 분류한 2017년 사전```

- LinearRegression_model_2016.ipynb : LinearRegression model for 2016
    ```LinearRegression_model_2016.ipynb : scikit-learn의 선형회귀 모델을 사용하여 만든 2016년 zillow 모델 (propeties2016년 사용)```
    
- LinearRegression_model_2017.ipynb : LinearRegression model for 2017
    ```LinearRegression_model_2017.ipynb : scikit-learn의 선형회귀 모델을 사용하여 만든 2017년 zillow 모델 (properties2017 사용)```
    
    
### 전처리

1. 누락된 값 채우기

- 카테고리 데이터
    - 같은 특성내 가장 자주 등장한 값으로 빈값을 채운다.
- 수치 데이터
    - statsmodels이 제공하는 MICEdata을 사용하여 빈값을 채운다.

2. 모델링 특성 선택

- 오직 우리가 예측하고자 하는 logerror의 값과 상관관계(correlation 값이 0이 아닌)가 있는 특성만을 선택한다.


### 모델

- LinearRegression of sklearn


### 결과

- 2666 / 3779 : 상위 70%

<img src="image/score.png" alt="subject_image" width="600" height="100">

### Feedback

- 처음 프로젝트를 시작할 때 선형 회귀만으로 문제를 풀어보라는 제약조건을 가지고 시작하였다.
- 비선형회귀 모형을 사용한다면 더 좋은 결과를 만들어 낼 수 있을 것 같다.
