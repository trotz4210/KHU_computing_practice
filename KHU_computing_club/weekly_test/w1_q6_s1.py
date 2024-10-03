# [if~elif~else 2] 점수를 입력받아 그 점수에 해당되는 등급(A,B,C,D,F)을 판정하는 프로그램을 작성하시오.
# 형식
# 점수를 입력해주세요 : 88
# 성적 : 88
# 등급 : B

#Solution
score = int(input("점수를 입력해주세요 : "))

if 90 <= score <= 100:
    print(f"성적 : {score}\n등급 : A")
elif 80 <= score <= 89:
    print(f"성적 : {score}\n등급 : B")
elif 70 <= score <= 79:
    print(f"성적 : {score}\n등급 : C")
elif 60 <= score <= 69:
    print(f"성적 : {score}\n등급 : D")
elif 0 <= score <= 59:
    print(f"성적 : {score}\n등급 : F")
else:
    print("잘못된 입력입니다.")
