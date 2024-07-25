import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, firestore

# 비밀값 읽기
json_text = st.secrets["textkey"]["value"]

# JSON 문자열 파싱
key_dict = json.loads(json_text)

# Firebase Admin SDK 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate('secrets.json')  # 서비스 계정 키 파일 경로
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

# 사용자 로그인 함수
def login(username, password):
    users_ref = db.collection('users')
    query = users_ref.where('username', '==', username).where('password', '==', password).stream()
    for doc in query:
        return True
    return False

# 사용자 회원가입 함수
def signup(username, password):
    users_ref = db.collection('users')
    if not users_ref.where('username', '==', username).get():
        users_ref.add({
            'username': username,
            'password': password  # 비밀번호는 일반적으로 해시화하여 저장하는 것이 좋습니다.
        })
        return True
    return False

# 사용자 퀴즈 결과 저장 함수
def save_quiz_results(username, results):
    results_ref = db.collection('user_results').document(username)
    results_ref.set(results)
    st.success("Quiz results saved successfully!")

# Streamlit UI
st.title('Streamlit App with Firebase Authentication')

# 로그인 및 회원가입 선택
choice = st.sidebar.selectbox("Select an option", ["Login", "Sign Up", "Quiz"])

if choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.username = username  # 사용자 이름 세션에 저장
        else:
            st.error("Invalid username or password.")

elif choice == "Sign Up":
    st.subheader("Sign Up")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type='password', key="signup_password")
    if st.button("Sign Up"):
        if signup(username, password):
            st.success("Account created successfully!")
        else:
            st.error("Username already exists.")

elif choice == "Quiz":
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.warning("Please log in to access the quiz.")
    else:
        # 질문 1 출력
        question_1 = "1. 다음 중 경영정보학과의 영문 명을 고르시오"
        st.write(question_1)

        # 보기
        options_1 = ["MIS", "CIA", "FBI", "MI6"]

        # 라디오 버튼 생성
        selected_option_1 = st.radio("보기", options_1, key="q1_radio")

        # 질문 2 출력
        question_2 = "2. 동아대학교 부민캠퍼스의 위치를 고르시오"
        st.write(question_2)

        # 보기
        options_2 = ["부산 사하구", "부산 서구", "부산 해운대구", "부산 진구"]

        # 라디오 버튼 생성
        selected_option_2 = st.radio("보기", options_2, key="q2_radio")

        # 질문 3 출력
        question_3 = "3. 동아대학교 승학캠퍼스의 위치를 고르시오"
        st.write(question_3)

        # 보기
        options_3 = ["부산 사하구", "부산 서구", "부산 해운대구", "부산 진구"]

        # 라디오 버튼 생성
        selected_option_3 = st.radio("보기", options_3, key="q3_radio")

        # 제출 버튼
        if st.button("Submit Quiz"):
            # 정답 확인 및 결과 저장
            results = {
                'question_1': selected_option_1,
                'question_2': selected_option_2,
                'question_3': selected_option_3
            }
            
            # 결과 저장
            save_quiz_results(st.session_state.username, results)
            
            # 정답 피드백
            correct_answers = {
                'question_1': "MIS",
                'question_2': "부산 서구",
                'question_3': "부산 사하구"
            }
            
            for q, correct_answer in correct_answers.items():
                if results[q] == correct_answer:
                    st.success(f"Question {q[-1]}: Correct!")
                else:
                    st.error(f"Question {q[-1]}: Incorrect! The correct answer is '{correct_answer}'.")

        st.markdown("---")
