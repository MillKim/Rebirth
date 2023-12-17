import streamlit as st
import random

example = {
    'A구역' : ['대한민국', '북한', '일본', '중국', '러시아'],
    'B구역' : ['미국', '캐나다', '맥시코', '아르헨티나', '칠레'],
    'C구역' : ['프랑스', '이탈리아', '그리스', '이집트', '소말리아']
}

st.subheader("환생 연습 :man-cartwheeling: ")
st.write("- A구역: 대한민국, 북한, 일본, 중국, 러시아")
st.write("- B구역: 미국, 캐나다, 맥시코, 아르헨티나, 칠레")
st.write("- C구역: 프랑스, 이탈리아, 그리스, 이집트, 소말리아")

choice = st.selectbox("환생할 구역을 선택하세요.", ("A구역", "B구역", "C구역"))

if st.button("환생! :man-raising-hand:"):
    rebirth = random.choice(example[choice])
    st.write(f"{rebirth}에 환생했다!")
