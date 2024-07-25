import streamlit as st

# 질문 1 출력
question_1 = "1. 다음 중 경영정보학과의 영문 명을 고르시오"
st.write(question_1)

# 보기
options_1 = ["MIS", "CIA", "FBI", "MI6"]

# 라디오 버튼 생성
selected_option_1 = st.radio("보기", options_1, key="q1_radio")

# 제출 버튼
if st.button("제출", key="submit_button_1"):
    # 정답 확인
    if selected_option_1 == "MIS":
        st.success("정답입니다! 'MIS'는 경영정보학과의 영문 명입니다.")
    else:
        st.error("오답입니다. 정답은 'MIS'입니다.")

st.markdown("---")

# 질문 2 출력
question_2 = "2. 동아대학교 부민캠퍼스의 위치를 고르시오"
st.write(question_2)

# 보기
options_2 = ["부산 사하구", "부산 서구", "부산 해운대구", "부산 진구"]

# 라디오 버튼 생성
selected_option_2 = st.radio("보기", options_2, key="q2_radio")

# 제출 버튼
if st.button("제출", key="submit_button_2"):
    # 정답 확인
    if selected_option_2 == "부산 서구":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 정답은 '부산 서구'입니다.")

st.markdown("---")

# 질문 3 출력
question_3 = "3. 동아대학교 승학캠퍼스의 위치를 고르시오"
st.write(question_3)

# 보기
options_3 = ["부산 사하구", "부산 서구", "부산 해운대구", "부산 진구"]

# 라디오 버튼 생성
selected_option_3 = st.radio("보기", options_3, key="q3_radio")

# 제출 버튼
if st.button("제출", key="submit_button_3"):
    # 정답 확인
    if selected_option_3 == "부산 사하구":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 정답은 '부산 사하구'입니다.")

st.markdown("---")

