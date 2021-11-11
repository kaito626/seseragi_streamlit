# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:12:41 2021

@author: ItoKaito
"""
import streamlit as sｔ

st.title('初めてのtreamlit')
st.write('私の名前は〇〇です')

text = st.text_input('あなたの名前を教えてください')
'あなたの名前は,',text,'です'

condition = st.slider('あんたの今の調子は？',0,100,50)
'コンディション：',condition

option = st.selectbox( '好きな数字を教えてください',list(['1番','2番','3番','4番']))
'あんたが選択したのは',option,'です'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
from PIL import Image
img = Image.open('room.jpg')
st.image(img,caption='もの技1のイケメン決めポーズ',use_column_width=True)
