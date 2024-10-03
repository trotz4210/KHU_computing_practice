# [if~elif~else 1] 입력 받은 세 수 중 가장 큰 수를 찾는 프로그램을 작성하시오.
# 형식
# 첫 번째 정수를 입력하세요 : 3
# 두 번째 정수를 입력하세요 : 6
# 세 번째 정수를 입력하세요 : 7
# 입력된 세 수 3, 6, 7 중에서 가장 큰 수는 7입니다.

#Solution
first = int(input("첫 번째 정수를 입력하세요 : "))
second = int(input("두 번째 정수를 입력하세요 : "))
third = int(input("세 번째 정수를 입력하세요 : "))

if first == second and second == third:
    print(f"세 수는 모두 같으므로, 가장 큰 수는 {first} 입니다.")
elif first >= second:
    if first > third:
        print(f"입력된 세 수 {first}, {second}, {third} 중에서 가장 큰 수는 {first}입니다.")
    else:
        print(f"입력된 세 수 {first}, {second}, {third} 중에서 가장 큰 수는 {third}입니다.")
else:
    if second > third:
        print(f"입력된 세 수 {first}, {second}, {third} 중에서 가장 큰 수는 {second}입니다.")
    else:
        print(f"입력된 세 수 {first}, {second}, {third} 중에서 가장 큰 수는 {third}입니다.")
