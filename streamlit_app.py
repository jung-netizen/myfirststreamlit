import streamlit as st

st.title("👋🏻 연수실습")
st.subheader("두번째 제목.")
st.write("반갑습니다~~~~")
st.info("이정화입니다")
st.write("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A7%84%EC%A3%BC%EB%AA%A9%EA%B1%B8%EC%9D%B4")


st.link_button("streamlit 매뉴얼 페이지 바로가기!", "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A7%84%EC%A3%BC%EB%AA%A9%EA%B1%B8%EC%9D%B4")

st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjlqcHQ4ZTgycWR0c2dmOXBpZWY0ajFwbXkxZWg1bDBlMW1yejJ5aiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/ERDMbAWVZEMzI0m8wY/giphy.gif", caption="Welcome to coding world") 
st.video("https://youtu.be/utIbM9Iua-k?si=igG_8qgD-cfUIMSc")