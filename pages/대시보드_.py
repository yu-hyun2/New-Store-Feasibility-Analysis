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
마트정보_5가지_점수 = pd.read_csv('/app/yuhyuns/data/마트정보_5가지_점수.csv')

with col_2_1:
    fig = go.Figure()

    tmp1 = 마트정보_5가지_점수[마트정보_5가지_점수['store_nbr'] == 44][['브랜드내일일매출백분율','지역내백비율','프로모션효과','기름가격민감도','거래당평균매출']].T.reset_index()
    tmp1.columns = ['theta', 'r']

    tmp2 = 마트정보_5가지_점수[마트정보_5가지_점수['store_nbr'] == 25][['브랜드내일일매출백분율','지역내백비율','프로모션효과','기름가격민감도','거래당평균매출']].T.reset_index()
    tmp2.columns = ['theta', 'r']

    fig.add_trace(go.Scatterpolar(
        r=tmp1['r'],
        theta=tmp1['theta'],
        fill='toself',
        name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
        r=tmp2['r'],
        theta=tmp2['theta'],
        fill='toself',
        name='Product B'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True, key='radar')