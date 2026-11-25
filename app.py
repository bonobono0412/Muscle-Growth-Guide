
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="근성장 가이드",
    page_icon="💪",
    layout="centered"
)

# 부위별 운동 리스트
luten = ['이두컬', '해머컬', '트라이셉스 푸시다운']
chest = ['벤치프레스', '덤벨프레스', '푸쉬업']
back = ['랫풀다운', '시티드로우', '데드리프트']
abs = ['크런치', '레그레이즈', '플랭크']
legs = ['스쿼트', '레그프레스', '런지']


# 근성장 부위를 매개변수로 받는 함수
def workout(part):

    if part == '팔':
        routine = luten

    elif part == '가슴':
        routine = chest

    elif part == '등':
        routine = back

    elif part == '복근':
        routine = abs

    elif part == '다리':
        routine = legs

    else:
        return [], '잘못된 부위입니다.'

    recommendation = routine[0]

    return routine, recommendation


# 웹사이트 제목
st.title("💪 근성장 가이드")
st.subheader("나만의 운동 루틴 만들기")

st.write("원하는 근성장 부위와 주간 운동 횟수를 선택하세요!")

st.divider()

# 근성장 부위 선택
st.header("1. 근성장 부위 선택")

part = st.selectbox(
    "운동할 부위를 선택하세요.",
    ['팔', '가슴', '등', '복근', '다리']
)

# 주간 운동 횟수 선택
st.header("2. 주간 운동 횟수 선택")

age = st.selectbox(
    "일주일에 몇 번 운동할까요?",
    [1, 2, 3, 4, 5, 6, 7],
    index=2,
    format_func=lambda x: f"주 {x}회"
)

st.divider()

# 루틴 생성 버튼
if st.button("🔥 나의 운동 루틴 생성하기", use_container_width=True):

    routine, recommendation = workout(part)

    st.success("운동 루틴이 생성되었습니다!")

    # 선택 정보 출력
    st.header("📋 나의 운동 정보")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("선택 부위", part)

    with col2:
        st.metric("주간 운동 횟수", f"{age}회")

    # 운동 횟수가 적을 경우
    if age <= 2:
        st.warning(
            "운동 횟수가 적어 근성장에 시간이 오래 걸릴 수 있습니다."
        )

    # 운동 루틴 출력
    st.header("🏋️ 추천 운동 루틴")

    for exercise in routine:
        st.write(f"✅ {exercise}")

    # 주간 운동 데이터 생성
    st.header("📅 주간 운동 계획")

    for day in range(1, age + 1):

        st.subheader(f"Day {day}")

        for exercise in routine:
            st.write(f"- {exercise}")

    # 추천 운동 출력
    st.divider()

    st.header("⭐ 가장 추천하는 운동")

    st.success(f"오늘의 추천 운동은 **{recommendation}** 입니다!")

    st.balloons()

st.divider()

st.caption("근성장 가이드 | 나만의 운동 루틴 만들기")

