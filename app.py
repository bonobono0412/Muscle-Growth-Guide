
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="근성장 가이드",
    page_icon="💪",
    layout="wide"
)

# 제목
st.title("💪 근성장 가이드")
st.subheader("나만의 맞춤형 운동 루틴 만들기")
st.write("운동 부위, 세트 수, 세트당 반복 횟수를 설정하세요!")

st.divider()


# 부위별 운동 리스트
luten = [
    '바벨컬', '덤벨컬', '해머컬', '프리처컬',
    '컨센트레이션컬', '케이블컬',
    '트라이셉스 푸시다운',
    '오버헤드 트라이셉스 익스텐션',
    '클로즈그립 벤치프레스', '딥스'
]

chest = [
    '벤치프레스', '인클라인 벤치프레스',
    '덤벨프레스', '인클라인 덤벨프레스',
    '체스트 플라이', '케이블 크로스오버',
    '푸쉬업', '딥스',
    '머신 체스트 프레스', '디클라인 프레스'
]

back = [
    '데드리프트', '랫풀다운', '풀업', '친업',
    '시티드 케이블 로우', '바벨 로우',
    '덤벨 로우', '티바 로우',
    '스트레이트 암 풀다운', '페이스 풀'
]

abs = [
    '크런치', '레그레이즈', '플랭크',
    '사이드 플랭크', '바이시클 크런치',
    '마운틴 클라이머', '케이블 크런치',
    '행잉 레그레이즈', '리버스 크런치', '데드버그'
]

legs = [
    '스쿼트', '레그프레스', '런지',
    '레그 익스텐션', '레그 컬',
    '루마니안 데드리프트', '힙 쓰러스트',
    '카프 레이즈', '불가리안 스플릿 스쿼트',
    '고블릿 스쿼트'
]


# 운동 부위 데이터
exercise_data = {
    '팔': luten,
    '가슴': chest,
    '등': back,
    '복근': abs,
    '다리': legs
}


# 근성장 부위를 매개변수로 받는 함수
def workout(parts):

    routine = {}
    recommendation = {}

    for part in parts:

        if part == '팔':
            exercise = luten

        elif part == '가슴':
            exercise = chest

        elif part == '등':
            exercise = back

        elif part == '복근':
            exercise = abs

        elif part == '다리':
            exercise = legs

        else:
            continue

        routine[part] = exercise
        recommendation[part] = exercise[0]

    return routine, recommendation


# 운동 부위 선택
st.header("1. 운동 부위 선택")

parts = st.multiselect(
    "운동할 부위를 선택하세요. 여러 개 선택 가능합니다.",
    ['팔', '가슴', '등', '복근', '다리'],
    default=['팔']
)


# 주간 운동 횟수 선택
st.header("2. 주간 운동 횟수")

age = st.selectbox(
    "일주일에 몇 번 운동할까요?",
    [1, 2, 3, 4, 5, 6, 7],
    index=2,
    format_func=lambda x: f"주 {x}회"
)


# 운동 루틴 설정
st.header("3. 운동별 세트 및 반복 횟수")

set_data = {}
rep_data = {}

if parts:

    for part in parts:

        st.subheader(f"🏋️ {part} 운동 설정")

        for exercise in exercise_data[part]:

            col1, col2, col3 = st.columns([3, 1, 1])

            with col1:
                st.write(f"**{exercise}**")

            with col2:
                sets = st.number_input(
                    "세트",
                    min_value=1,
                    max_value=10,
                    value=3,
                    key=f"set_{part}_{exercise}"
                )

            with col3:
                reps = st.number_input(
                    "횟수",
                    min_value=1,
                    max_value=50,
                    value=12,
                    key=f"rep_{part}_{exercise}"
                )

            set_data[exercise] = sets
            rep_data[exercise] = reps

        st.divider()


# 루틴 생성 버튼
if st.button("🔥 나의 운동 루틴 생성하기", use_container_width=True):

    if not parts:
        st.error("운동 부위를 하나 이상 선택해주세요.")

    else:

        routine, recommendation = workout(parts)

        st.success("운동 루틴이 생성되었습니다!")

        # 운동 정보
        st.header("📋 나의 운동 정보")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("선택 부위", ", ".join(parts))

        with col2:
            st.metric("주간 운동 횟수", f"{age}회")

        # 운동 횟수 조건문
        if age <= 2:
            st.warning(
                "운동 횟수가 적어 근성장에 시간이 오래 걸릴 수 있습니다."
            )

        # 부위별 운동 결과
        st.header("🏋️ 운동별 세트 및 반복 횟수")

        for part in parts:

            st.subheader(f"💪 {part} 운동")

            for exercise in routine[part]:

                st.write(
                    f"✅ **{exercise}** : "
                    f"{set_data[exercise]}세트 × "
                    f"{rep_data[exercise]}회"
                )

        # 주간 운동 계획
        st.header("📅 주간 운동 계획")

        for day in range(1, age + 1):

            st.subheader(f"Day {day}")

            for part in parts:

                st.write(f"**[{part}]**")

                for exercise in routine[part][:3]:

                    st.write(
                        f"- {exercise} | "
                        f"{set_data[exercise]}세트 × "
                        f"{rep_data[exercise]}회"
                    )

        # 추천 운동
        st.divider()

        st.header("⭐ 부위별 추천 운동")

        for part in parts:

            st.success(
                f"{part} 추천 운동: {recommendation[part]}"
            )

        st.balloons()

        st.success("나만의 근성장 루틴 생성 완료!")


# 하단 안내
st.divider()

st.caption(
    "💪 근성장 가이드 | 꾸준한 운동과 충분한 회복이 중요합니다."
)
