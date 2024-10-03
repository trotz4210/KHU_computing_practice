# [리스트7] 리스트에 저장된 성적에 대해 성적 등급에 따라 해당 인원을 세는 프로그램을 작성하시오. 

# Solution
s = [
    64, 89, 100, 85, 77, 58, 79, 67, 96, 87,
    87, 36, 82, 98, 84, 76, 63, 69, 53, 22
    ]

count_su = 0
count_wu = 0
count_mi = 0
count_yang = 0
count_ga = 0

i = 0

while i < len(s):
    if 100 >= s[i] >= 90:
        count_su += 1
    if 90 > s[i] >= 80:
        count_wu += 1
    if 80 > s[i] >= 70:
        count_mi += 1
    if 70 > s[i] >= 60:
        count_yang += 1
    if 60 > s[i]:
        count_ga += 1
    i = i + 1

print(
    f"수 : {count_su}명\n"
    f"우 : {count_wu}명\n"
    f"미 : {count_mi}명\n"
    f"양 : {count_yang}명\n"
    f"가 : {count_ga}명"
)