#[if 1] 키보드로 월을 입력 받아 월에 해당되는 계절을 표시하는 프로그램을 작성하시오.
#형식
#월을 입력하세요 : n월
#n월은 여름입니다.

#Solution
month = int(input("월을 입력하세요 : "))

if 3 <= month <= 5:
    print(f"{month}월은 봄입니다.")
elif 6 <= month <= 8:
    print(f"{month}월은 여름입니다.")
elif 9 <= month <= 11:
    print(f"{month}월은 가을입니다.")
elif month == 12 or 1 <= month <= 2:
    print(f"{month}월은 겨울입니다.")
else:
    print("유효하지 않은 값입니다.")
