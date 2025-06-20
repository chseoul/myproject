import streamlit as st

st.title("안녕하세요!")

st.title("Title")
st.header("Header")
st.subheader("Subheader")

st.text("이것은 일반 텍스트입니다.")

st.markdown('''
# Markdown
안녕하세요 **markdown** 형식으로 작성할 수 있는 함수입니다.
''')

st.code("print('Hello, World!')")


name = st.text_input(label="이름", placeholder="이름을 입력하세요")
st.text(name)


content = st.text_area(
	label="문의사항",
	placeholder="문의사항을 자세히 입력해주세요",
	height=200
)
st.text(content)

number = st.number_input(
	label="몇 개를 생성할까요?",
	min_value=1,
	max_value=5,
	value=3
)
st.text(f"number: {number}")

length = st.select_slider(
	label="문자열 길이",
	options=(100,200,300,400,500),
	value=200
)
st.text(f"length: {length}")

option = st.radio(
	label="카테고리를 선택하세요",
	options=["뉴스", "블로그", "기획안"],
	index=1
)
st.text(f"선택한 항목: {option}")

choice = st.selectbox(
	label="콘텐츠 유형을 선택하세요",
	options=["유튜브", "인스타그램", "블로그"],
	index=1
)
st.text(f"선택된 콘텐츠 유형: {choice}")

choices = st.multiselect(
	label="관심 있는 주제를 선택하세요",
	options=["AI", "데이터 사이언스", "웹 개발"],
	default=["AI","데이터 사이언스"]
)
st.text(f"선택한 주제: {', '.join(choices)}")

button = st.button(
	label="로그인",
	key="login_btn1"
)
if button:
	st.text("로그인 버튼이 클릭되었습니다.")
	

button = st.button(
	label="로그인",
	type="primary",
	key="login_btn2"
)
if button:
	st.text("로그인 버튼이 클릭되었습니다.")
	

import streamlit as st

button = st.button(
	label="로그인",
	use_container_width=True,
	key="login_btn3"
)
if button:
	st.text("로그인 버튼이 클릭되었습니다.")
	
# 텍스트파일 업로드(sample.txt)
uploaded_file = st.file_uploader("텍스트 파일을 업로드하세요", type=["txt"])
if uploaded_file is not None:
	content = uploaded_file.read().decode("utf-8")
	st.text(content)

# 이미지파일 업로드(sample.jpeg)
uploaded_file = st.file_uploader(
	"이미지 파일을 업로드하세요",
	type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
	st.image(uploaded_file)
	

count = 0
if st.button("클릭"):
	count += 1
st.text(f"버튼 누른 횟수: {count}")


if "count" not in st.session_state:
	st.session_state["count"] = 0

if st.button("Click"):
	st.session_state["count"] += 1
st.text(f"버튼 누른 횟수: {st.session_state['count']}")
