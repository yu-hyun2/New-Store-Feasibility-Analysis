## ⭐ Store Sales - Time Series Forecasting

[kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)

### File Descriptions and Data Field Information
#### train.csv
- The training data, comprising time series of features store_nbr, family, and onpromotion as well as the target sales.
- store_nbr identifies the store at which the products are sold.
- family identifies the type of product sold.
- sales gives the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips).
onpromotion gives the total number of items in a product family that were being promoted at a store at a given date.
#### test.csv
- The test data, having the same features as the training data. You will predict the target sales for the dates in this file.
- The dates in the test data are for the 15 days after the last date in the training data.
#### sample_submission.csv
- A sample submission file in the correct format.
#### stores.csv
- Store metadata, including city, state, type, and cluster.
- cluster is a grouping of similar stores.
#### oil.csv
- Daily oil price. Includes values during both the train and test data timeframes. (Ecuador is an oil-dependent country and it's economical health is highly vulnerable to shocks in oil prices.)
#### holidays_events.csv
- Holidays and Events, with metadata
- NOTE: Pay special attention to the transferred column. A holiday that is transferred officially falls on that calendar day, but was moved to another date by the government. A transferred day is more like a normal day than a holiday. To find the day that it was actually celebrated, look for the corresponding row where type is Transfer. For example, the holiday Independencia de Guayaquil was transferred from 2012-10-09 to 2012-10-12, which means it was celebrated on 2012-10-12. Days that are type Bridge are extra days that are added to a holiday (e.g., to extend the break across a long weekend). These are frequently made up by the type Work Day which is a day not normally scheduled for work (e.g., Saturday) that is meant to payback the Bridge.
Additional holidays are days added a regular calendar holiday, for example, as typically happens around Christmas (making Christmas Eve a holiday).


#### train.csv
- store_nbr, family, onpromotion 및 목표 매출의 시계열로 구성된 학습 데이터입니다.
- store_nbr은 제품이 판매된 매장을 식별합니다.
- family는 판매된 제품 유형을 식별합니다.
- sales는 특정 날짜에 특정 스토어에서 제품군의 총 판매량을 제공합니다. 제품을 분수 단위로 판매할 수 있으므로 분수 값도 가능합니다(예: 칩 1봉지가 아닌 치즈 1.5kg).
- 온프로모션은 지정된 날짜에 스토어에서 프로모션 중인 제품군의 총 품목 수를 제공합니다.

#### test.csv
- 학습 데이터와 동일한 기능을 가진 테스트 데이터입니다. 이 파일에 있는 날짜에 대한 목표 매출을 예측합니다.
- 테스트 데이터의 날짜는 학습 데이터의 마지막 날짜 이후 15일 동안의 날짜입니다.

#### sample_submission.csv
- 올바른 형식의 샘플 제출 파일입니다.

#### stores.csv
- 도시, 주, 유형 및 클러스터를 포함한 스토어 메타데이터.
- 클러스터는 유사한 스토어의 그룹입니다.

#### oil.csv
- 일일 유가. 훈련 및 테스트 데이터 기간 동안의 값을 모두 포함합니다. (에콰도르는 석유 의존도가 높은 국가로 유가 충격에 경제가 매우 취약합니다.)

#### holidays_events.csv
- 휴일 및 이벤트, 메타데이터 포함
- 참고: 이전된 열에 특히 주의하세요. 이전된 공휴일은 공식적으로는 해당 달력 날짜에 해당하지만 정부에서 다른 날짜로 옮긴 것입니다. 이전된 날짜는 공휴일이라기보다는 평일과 비슷합니다. 실제로 공휴일로 지정된 날을 찾으려면 유형이 이전인 해당 행을 찾습니다. 예를 들어, 과야킬의 독립 기념일(Independencia de Guayaquil)은 2012-10-09에서 2012-10-12로 이전되었으므로 2012-10-12에 기념되었습니다. Bridge 유형인 날은 공휴일에 추가되는 추가 날입니다(예: 긴 주말에 걸쳐 휴일을 연장하기 위해). 이러한 휴일은 보통 근무일 유형으로 구성되는데, 근무일 유형은 일반적으로 근무가 예정되어 있지 않은 날(예: 토요일)로 브리지를 보상하기 위해 만들어집니다.
추가 휴일은 일반적으로 크리스마스 전후에 발생하는 것처럼 일반 달력 휴일에 추가되는 날입니다(예: 크리스마스 이브를 휴일로 지정).
