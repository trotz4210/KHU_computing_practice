# [if~else] 아르바이트 주간 또는 야간 근무와 시간을 입력 받아 급여를 계산하는 프로그램을 작성하시오.
#형식
#아르바이트 급여 계산 프로그램
#※ 시급
#- 주간 근무 : 9,500원
#- 야간 근무 : 주간 시급 * 1.5
#
#1(주간 근무) 또는 2(야간 근무)를 입력해주세요 : 2
#근무 시간을 입력해주세요 : 5
#5시간 동안 일한 야간 급여는 71,250원 이다.

#Solution
print("아르바이트 급여 계산기\n"
      "※ 시급\n"
      "- 주간 근무 : 9,500원\n"
      "- 야간 근무 : 주간 시급 * 1.5")

wage_per_hour = 9500

types_of_work = int(input("1(주간 근무) 또는 2(야간 근무)를 입력해주세요 : "))
time_of_work = int(input("근무 시간을 입력해주세요 : "))

if types_of_work == 1:
    total_day_wage = wage_per_hour * time_of_work
    print(f"{time_of_work}시간 동안 일한 주간 급여는 {total_day_wage}원 이다.")
elif types_of_work == 2:
    round(total_night_wage,0) = wage_per_hour * time_of_work * 1.5
    print(f"{time_of_work}시간 동안 일한 야간 급여는 {total_night_wage}원 이다.")
else:
    print("잘못된 입력입니다.")
