
# 근성장 가이드 프로그램

# 부위별 운동 목록
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

    # 추천 운동 반환
    recommendation = routine[0]

    return routine, recommendation


# 프로그램 시작
print("================================")
print("       근성장 가이드 프로그램")
print("================================")

# 근성장 부위 선택
print("\n근성장 부위를 선택하세요.")
print("1. 팔")
print("2. 가슴")
print("3. 등")
print("4. 복근")
print("5. 다리")

choice = input("선택: ")

parts = {
    '1': '팔',
    '2': '가슴',
    '3': '등',
    '4': '복근',
    '5': '다리'
}

if choice not in parts:
    print("잘못된 선택입니다.")

else:
    part = parts[choice]

    # 주 운동 횟수 선택
    age = int(input("\n주 운동 횟수를 선택하세요 (1~7): "))

    if age < 1 or age > 7:
        print("운동 횟수는 1~7 사이로 입력하세요.")

    else:
        # 함수 호출
        routine, recommendation = workout(part)

        print("\n========== 운동 결과 ==========")
        print("선택한 근성장 부위:", part)
        print("주 운동 횟수:", age, "회")

        # 운동 횟수가 적을 경우
        if age <= 2:
            print("운동 횟수가 적어 근성장에 시간이 오래 걸릴 수 있습니다.")

        # 운동 루틴 출력
        print("\n[추천 운동 루틴]")

        for exercise in routine:
            print("-", exercise)

        # 주간 루틴 데이터 생성
        print("\n[주간 운동 루틴 데이터]")

        for day in range(1, age + 1):
            for exercise in routine:
                print(f"Day {day}: {exercise}")

        # 추천 운동 출력
        print("\n가장 추천하는 운동:", recommendation)

        print("\n근성장 가이드를 이용해 주셔서 감사합니다!")
