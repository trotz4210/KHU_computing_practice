#[if 1] 키보드로 월을 입력 받아 월에 해당되는 계절을 표시하는 프로그램을 작성하시오.
#형식
#월을 입력하세요 : n월
#n월은 여름입니다.

#Solution
봄 = [3, 4, 5]
여름 = [6, 7, 8]
가을 = [9, 10 ,11]
겨울 = [1, 2, 12]

month = int(input("월을 입력하세요 : "))

if month in 봄:
    print(f"{month}월은 봄입니다.")
elif month in 여름:
    print(f"{month}월은 여름입니다.")
elif month in 가을:
    print(f"{month}월은 가을입니다.")
elif month in 겨울:
    print(f"{month}월은 겨울입니다.")
else:
    print("잘못된 입력 값입니다.")
