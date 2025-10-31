import streamlit as st

st.title("🧮 간단한 계산기")

expr = st.text_input("수식을 입력하세요 (예: 3*(4+2)/5):")

if st.button("계산하기"):
    try:
        result = eval(expr)
        st.success(f"결과: {result}")
    except Exception as e:
        st.error(f"오류: {e}")
