import streamlit as st

st.title("형성평가")\

option=st.radio("정답은 무엇일까요?",["강남역","역삼역","방배역","서초역","선릉역"])
option=st.radio("집에 몇시에 갈까요?",["8시","8시10분","8시20분","지금당장"])

option=st.multiselect("이것은 중복선택",["1","2","3","4"])

agree=st.checkbox("동의하시나요?")

if agree:
    st.write("동의하셨군요")
else:
    st.write("동의버튼을 눌러주세요.")


name=st.text_input("이름 입력하세요")
if name:
    st.error(f"{name}님 환영합니다!☺️☺️")
             