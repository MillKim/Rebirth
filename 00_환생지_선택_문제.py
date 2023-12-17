import streamlit as st
import pandas as pd
from PIL import Image

st.title("환생지 선택 문제 :baby:")

st.write("여러분은 하나의 구역을 선택하면, 해당 구역에 속한 국가 중 임의의 국가에 태어나게 된다.")
st.write("단, 구역을 선택했을 때 해당 구역에 속한 각 나라에 태어날 가능성은 모두 동일하다.")
st.write("당신은 어느 구역에 태어날 것인가?? :eyes: :thought_balloon:")

worldmap = Image.open('worldmap.jpg')
st.image(worldmap)

