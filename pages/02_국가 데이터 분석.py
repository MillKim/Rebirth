import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
plt.rc('font', family='NanumSquareRound')
mpl.rcParams['axes.unicode_minus'] = False

st.subheader("국가 데이터 분석 :face_with_monocle: ")
df = pd.read_excel('country_data.xlsx')

st.dataframe(df)

index = st.selectbox("비교할 사회 지표를 선택하세요.", ("평균 기온", "1인당 GDP($)", "출산률", "지니계수", "면적(km^2)", "인터넷 이용률", "대학 진학률", "행복지수", "실업률", "평균수명(세)", "보건지표", "환경지표", "범죄율(10만명 당)", "성평등지수", "빈곤율", "자살율(10만명 당)"))
comparison = st.selectbox("비교에 사용할 대푯값, 산포도 또는 그림을 선택하세요", ("평균", "중앙값", "표준편차", "상자 그림"))
row_range = [(1, 11), (11, 21), (21, 31), (31, 41), (41, 51)]

if st.button("출력"):
    column_data = df[index]
    if comparison == "평균":
        mean_values = []
        for start, end in row_range:
            mean_values.append(column_data[start-1:end].mean())
        plot = sns.catplot(x=["A구역", "B구역", "C구역", "D구역", "E구역"], y=mean_values, kind='bar', palette="ch:s=.25,rot=-.25", legend=False)
        plt.title(f"{index}의 {comparison}", fontsize=20)
        plt.xlabel("구역", fontsize=15)
        plt.ylabel(f"{index}", fontsize=15)
        st.pyplot(plot)

    if comparison == "중앙값":
        median_values = []
        for start, end in row_range:
            median_values.append(column_data[start-1:end].median())
        plot = sns.catplot(x=["A구역", "B구역", "C구역", "D구역", "E구역"], y=median_values, kind='bar', palette="ch:s=.25,rot=-.25", legend=False)
        plt.title(f"{index}의 {comparison}", fontsize=20)
        plt.xlabel("구역", fontsize=15)
        plt.ylabel(f"{index}", fontsize=15)
        st.pyplot(plot)

    if comparison == "표준편차":
        std_values = []
        for start, end in row_range:
            std_values.append(column_data[start-1:end].std())
        plot = sns.catplot(x=["A구역", "B구역", "C구역", "D구역", "E구역"], y=std_values, kind='bar', palette="ch:s=.25,rot=-.25", legend=False)
        plt.title(f"{index}의 {comparison}", fontsize=20)
        plt.xlabel("구역", fontsize=15)
        plt.ylabel(f"{index}", fontsize=15)
        st.pyplot(plot)

    if comparison == "상자 그림":
        df1 = df.loc[1:11, index].to_frame().assign(Area='A구역')
        df2 = df.loc[11:21, index].to_frame().assign(Area='B구역')
        df3 = df.loc[21:31, index].to_frame().assign(Area='C구역')
        df4 = df.loc[31:41, index].to_frame().assign(Area='D구역')
        df5 = df.loc[41:51, index].to_frame().assign(Area='E구역')
        df_concat = pd.concat([df1, df2, df3, df4, df5])

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='Area', y=df.columns[df.columns.get_loc(index)], data=df_concat, ax=ax)
        plt.title(f"{index}의 {comparison}", fontsize=20)
        plt.xlabel("구역", fontsize=15)
        plt.ylabel(f"{index}", fontsize=15)
        st.pyplot(fig)



    