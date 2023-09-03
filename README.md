# New Store Feasibility Analysis Report
- [Kaggle) Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview)데이터로 분석

## ✅ Assuming a Business Case
| 5W1H | CONTENT |
| --- | --- |
| Who | Favorita 전략 기획실 이사(가정) |
| When | 2017년 8월 이후 |
| Where | 에콰도르 수도, 키토 |
| How | 키토 지역 내 타입별 매장 분포와 타입별 특징 분석을 통한 의사결정 |
| What | 새로운 지점 설립 |
| Why | 경제 성장으로 인한 수요 증가 → 수요 충족을 위한 새로운 매장 설립 |

## 🎯 타겟 및 상황
- 타겟은 파보리타의 전략기획실 이사로, 새로운 지점을 오픈할 것인지 고민하고 있다.  
- 새로운 매장을 오픈하는 게 맞는지, 오픈한다면 매장이 어느 위치와 시간에 입점하면 좋을지 기존 매출 데이터와 더불어 다양한 추가 데이터들을 고려해 선정하려고 한다.  

## 📃 분석 과정
- 매장별 특징, 경제 현황, 소비자 특징 파악을 위한 EDA
- 매출 예측
- 타입별 특징 분석, 실제 매장 위치 유추
- 신설 매장 타당성 검토(위치, 타입)
- 신설 매장 후보 선정 및 위치별 타입 최종 결정

## 📂 About Data
| csv 데이터 | 내용 |
| --- | --- |
| train.csv | store_nbr, family, onpromotion 및 목표 매출의 시계열로 구성된 학습 데이터 |
| stores.csv | 도시, 주, 유형 및 클러스터를 포함한 스토어 메타데이터 |
| transactions.csv | 일반적으로 판매와 상관없는 기타 거래를 제외한 순수한 판매 건수 |
| oil.csv | 일일 유가. 훈련 및 테스트 데이터 기간 동안의 값을 모두 포함(에콰도르는 석유 의존도가 높은 국가) |
| holidays_events.csv | 휴일 및 이벤트, 메타데이터 포함 [캐글 사이트 데이터 설명 참고](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)|  

## 🔍 참고 자료
- [에콰도르 즉석 식품 시장동향](www.kiep.go.kr)
- [에콰도르 국가 정보](https://ko.wikipedia.org/wiki/%EC%97%90%EC%BD%B0%EB%8F%84%EB%A5%B4)
- [에콰도르 통계 자료](https://www.theglobaleconomy.com/Ecuador/consumption/)
- [Store 자료](https://es.foursquare.com/v/gran-aki/54f1faa0498edddc47fc747f)
- [Kotra 해외시장뉴스](https://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=200&CONTENTS_NO=1&bbsSn=403&pNttSn=192484)
- [파보리따 2017 보고서 ](https://www.corporacionfavorita.com/en/annual-report/)
- [파보리따 유튜브](https://www.youtube.com/@corporacionfavorita1947/videos)
- [에콰도르는 어떤 나라?](https://www.youtube.com/watch?v=XH81Z0dfjww&t=245s)
- [트렌드 - KOTRA 해외시장뉴스](https://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=180&CONTENTS_NO=1&bbsGbn=243&bbsSn=243&pNttSn=155811)
- [에콰도르 식품산업 현황](https://repository.krei.re.kr/bitstream/2018.oak/24747/1/E03-2020-03-05.pdf)
- [참고한 노트북1](https://kubig-2021-2.tistory.com/58)
- [참고한 노트북2](https://www.kaggle.com/code/ekrembayar/store-sales-ts-forecasting-a-comprehensive-guide)










