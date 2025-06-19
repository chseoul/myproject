import streamlit as st
# 웹 페이지 설정
st.set_page_config(
    page_title="뉴콘텐츠아카데미",
    layout="wide"
)

# 네비게이션 바 코드 작성
pages = [
    st.Page(
        page="pages/01_basic.py",
        title="Basic",
        default=True
    ),
    st.Page(
        page="pages/02_copywriterbot.py",
        title="CopywriterBot"
    ),
    st.Page(
        page="pages/03_chatbot.py",
        title="ChatBot"
    ),
    st.Page(
        page="pages/04_worldchatbot.py",
        title="WorldChatBot"
    ),
     st.Page(
        page="pages/05_writingBot.py",
        title="WritingBot"
    ),
         st.Page(
        page="pages/06_youtubeChatBot.py",
        title="YoutubeChatBot"
    )
    ]

nav = st.navigation(pages)
nav.run()