import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()

# 사이드바 아닌 버전
# col1,col2,col3 = st.columns(3)
# col4,col5,col6 = st.columns(3)

# with col1:
#     color1 = st.radio('y1 선의 색을 선택하시오',['red','green','blue','orange'])
# with col2:
#     marker1 = st.radio('y1 선의 형태를 선택하시오',['o','^','s','p','h'])
# with col3:
#     style1 = st.radio('y1 선 스타일을 선택하시오',['-',':','-.','--'])

# with col4:
#     color2 = st.radio('y2 선의 색을 선택하시오',['red','green','blue','orange'])
# with col5:
#     marker2 = st.radio('y2 선의 형태를 선택하시오',['o','^','s','p','h'])
# with col6:
#     style2 = st.radio('y2 선의 스타일을 선택하시오',['-',':','-.','--'])


color1=st.sidebar.radio('y1의 색을 선택하시오',['red','green','blue','orange'])
style1=st.sidebar.radio('y1의 스타일을 선택하시오',['-',':','-.','--'])
marker1=st.sidebar.radio('y1의 형태를 선택하시오',['o','^','s','p','h'])

color2=st.sidebar.radio('y2의 색을 선택하시오',['red','green','blue','orange'])
style2=st.sidebar.radio('y2의 스타일을 선택하시오',['-',':','-.','--'])
marker2=st.sidebar.radio('y2의 선택하시오',['o','^','s','p','h'])

a = st.number_input( 'a의 값을 입력하시오', value=2.0, step = 1.0 )
b = st.number_input( 'b의 값을 입력하시오', value=-1.0, step = 1.0 )
c = st.number_input( 'c의 값을 입력하시오', value=15.0, step = 1.0 )
d = st.number_input( 'd의 값을 입력하시오', value=2000.0, step = 100.0 )

x=[]
y=[]
ycos=[]
for i in range(-20,31,3): 
    x.append(i)
    y.append(a*i**2 + b*i + c)
    ycos.append(d*np.cos(i))

plt.plot(x,y, color=color1, linewidth=2, label='2nd', marker=marker1, linestyle=style1)
plt.plot(x,ycos, color=color2, linewidth=2, label='cos',marker=marker2, linestyle=style2)
plt.legend()

st.pyplot(fig)