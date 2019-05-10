numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Угадайте число или введите X для выхода. ")
    if answer == "X":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("пожалуйста, введите число или X для выхода.")
    if answer in numbers:
        print("Вы угадали!")
    else:
        print("Неправильно!")

    
