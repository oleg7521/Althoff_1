while True:
    print("Введи X для выхода")
    for i in range(1, 11):
        print(i, end=' ')
    print()
    a = input("Отгадайте число из списка ")
    if a == "X":
        break
    elif int(a) == 7:
        print("Вы угадали")
        break
    else:
        print("Попробуйте ещё раз")

    
