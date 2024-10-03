# [if~elif~else 2] 점수를 입력받아 그 점수에 해당되는 등급(A,B,C,D,F)을 판정하는 프로그램을 작성하시오.
# 형식
# 점수를 입력해주세요 : 88
# 성적 : 88
# 등급 : B

#Solution
def calculate_grade(score):
    # 점수 범위별 등급을 매핑
    grade_ranges = [
        (range(90, 101), 'A'),
        (range(80, 90), 'B'),
        (range(70, 80), 'C'),
        (range(60, 70), 'D'),
        (range(0, 60), 'F')
    ]
    
    # 입력 점수에 따라 등급을 찾아 반환
    for score_range, grade in grade_ranges:
        if score in score_range:
            return f"성적 : {score}\n등급 : {grade}"
    return "잘못된 입력입니다."

# 사용자로부터 점수 입력받기
user_score = int(input("점수를 입력해주세요 : "))
# 등급 계산 후 결과 출력
print(calculate_grade(user_score))

