import random


# Guess Game
def guess_game():
    cnt = 0
    guess_number = random.randint(1, 100)
    while True:
        user_guess = int(input("추측: "))
        cnt += 1
        if user_guess > guess_number:
            print("숫자가 너무 큽니다.")
        elif user_guess < guess_number:
            print("숫자가 너무 작습니다.")
        else:
            print(f"정답입니다. {cnt}번만에 맞췄습니다.")
            break


# Gugu
def gugu():
    while True:
        user_input = int(input("구구단 몇 단을 계산할까요?(1~9): "))
        if not 1 <= user_input <= 9:
            break
        print(f"구구단 {user_input}단을 계산합니다.")
        for i in range(1, 9):
            print(f"{user_input} * {i} = {user_input * i}")
    print("구구단 게임을 종료합니다.")


# 2차원 리스트
def average():
    kor_score = [49, 79, 20, 100, 80]
    math_score = [43, 59, 85, 30, 90]
    eng_score = [49, 79, 48, 60, 100]
    midterm_score = [kor_score, math_score, eng_score]
    avg = [0, 0, 0, 0, 0]
    for subject in midterm_score:
        for stu, score in enumerate(subject):
            avg[stu] += score
    else:
        for i in range(len(avg)):
            avg[i] /= len(midterm_score)
        print(avg)


# 딕셔너리
def dictionary():
    l = [{'id': 1, 'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-2343-9870'},
    {'id': 2, 'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'},
    {'id': 3, 'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-7777-1234'},
    {'id': 4, 'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-4567-0987'}]
    for person in l:
        for k, v in person.items():
            print(f"{k}:{v}")
        print('---')


choice = input("실행할 코드\n1:guess, 2:gugu, 3:2차원리스트\n, 4:딕셔너리\n")
if choice == '1':
    guess_game()
elif choice == '2':
    gugu()
elif choice == '3':
    average()
elif choice == '4':
    dictionary()
