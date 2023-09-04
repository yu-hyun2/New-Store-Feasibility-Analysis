import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

# 레이아웃
with st.container():
    col_0_0, col_0_1, col_0_2 = st.columns([1,3,1])

with st.container():
    col_1_0, col_1_1, col_1_2, col_1_3 = st.columns([1,1,1,1])

with st.container():
    col_2_0, col_2_1, col_2_2 = st.columns([1,2,2])

with st.container():
    col_3_0, col_3_1, col_3_2, col_3_3 = st.columns([1,1,1,1])

with st.container():
    col_4_0, col_4_1, col_4_2 = st.columns([1,2,2])

with st.container():
    col_5_0, col_5_1, col_5_2, col_5_3 = st.columns([1,1,1,1])


# 데이터 로드
광고 = pd.read_csv('/app/yuhyuns/data/광고.csv')
df = pd.read_csv('/app/yuhyuns/data/날짜별_가게별_카테모리매출합.csv')
df['date'] = pd.to_datetime(df['date'])
df['년도'] = df['date'].dt.year
df['월'] = df['date'].dt.month
df['일'] = df['date'].dt.day

# 시각화
with col_0_1:
    st.markdown("<h1 style='text-align: center; color: grey;'>에콰도르 마트 분석</h1>", unsafe_allow_html=True)

with col_2_1:
    options = st.selectbox(
        '가게 번호를 선택해주세요.',
        (1,2,3,4,5,6,7,8,9,10), key='line_options')
    st.write('가게 번호:', options)
    라인그래프 = df.set_index('date').iloc[:,1:][df.set_index('date')['store_nbr'] == options].sum(axis=1)
    라인그래프 = 라인그래프.reset_index()
    라인그래프.columns = ['date','매출합']
    fig = go.Figure([go.Line(x=라인그래프['date'], y=라인그래프['매출합'])])
    st.plotly_chart(fig, use_container_width=True, key='line')

with col_2_2:
    year = st.selectbox(
    '년도를 선택해주세요',
    (2013,2014,2015,2016,2017), key='year')
    st.write('You selected:', year)
    m = 광고['년도'] == year

    fig = px.scatter(광고[m], x="sales", y="onpromotion", color="store_nbr")
    st.plotly_chart(fig, use_container_width=True, key='promo')

with col_4_1:
    options2 = st.selectbox(
        '가게 번호를 선택해주세요.',
        (1,2,3,4,5,6,7,8,9,10), key='bar_options2')
    st.write('가게 번호:', options2)
    가게25번카테고리매출합 = pd.DataFrame(df.iloc[:,2:][df['store_nbr'] == options2].dropna().sum()).sort_values(0, ascending=False)
    가게25번카테고리매출합 = 가게25번카테고리매출합.reset_index()
    가게25번카테고리매출합.columns = ['카테고리','매출합']
    fig = go.Figure([go.Bar(x=가게25번카테고리매출합['카테고리'], y=가게25번카테고리매출합['매출합'])])
    st.plotly_chart(fig, use_container_width=True, key='bar')

with col_4_2:
    fig = px.treemap(
        가게25번카테고리매출합,
        path=["카테고리"],
        values ='매출합')
    fig.update_layout(margin = dict(t = 50,l = 25, r = 25, b = 25))
    st.plotly_chart(fig, use_container_width=True, key='treemap')