
import streamlit as st

st.title("💪 근성장 가이드")
st.write("나만의 운동 루틴을 만들어 보세요!")

# 1. 부위별 운동 리스트
luten = ['바벨컬', '덤벨컬', '해머컬']
chest = ['벤치프레스', '덤벨프레스', '푸쉬업']
back = ['랫풀다운', '풀업', '데드리프트']
abs = ['크런치', '레그레이즈', '플랭크']
legs = ['스쿼트', '런지', '레그프레스']


# 2. 운동 부위를 매개변수로 받는 함수
def workout(part):

    if part == '팔':
        routine = luten
        sets = 3
        reps = 12

    elif part == '가슴':
        routine = chest
        sets = 3
        reps = 10

    elif part == '등':
        routine = back
        sets = 3
        reps = 10

    elif part == '복근':
        routine = abs
        sets = 3
        reps = 15

    else:
        routine = legs
        sets = 3
        reps = 12

    return routine, sets, reps


# 3. 운동 부위 선택
parts = st.multiselect(
    "운동 부위를 선택하세요.",
    ['팔', '가슴', '등', '복근', '다리']
)

# 4. 주간 운동 횟수 선택
age = st.selectbox(
    "주간 운동 횟수",
    [1, 2, 3, 4, 5, 6, 7]
)


# 5. 운동 일정표 생성
if st.button("운동 루틴 만들기"):

    if len(parts) == 0:
        st.warning("운동 부위를 선택해주세요.")

    else:
        st.header("📅 나의 주간 운동 일정표")

        days = [
            '월요일', '화요일', '수요일',
            '목요일', '금요일', '토요일', '일요일'
        ]

        # 선택한 횟수만큼 반복
        for i in range(age):

            st.subheader(days[i])

            # 선택한 운동 부위 순회
            part = parts[i % len(parts)]

            routine, sets, reps = workout(part)

            st.write("운동 부위:", part)

            # 운동 목록 출력
            for exercise in routine:
                st.write(
                    f"✅ {exercise} | "
                    f"{sets}세트 × {reps}회"
                )

        # 운동 횟수 조건문
        if age <= 2:
            st.warning(
                "운동 횟수가 적어 근성장에 시간이 오래 걸릴 수 있습니다."
            )

        st.success("운동 일정표 생성 완료!")
