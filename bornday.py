# bornday.py

# Спросить у пользователя год рождения А.С. Пушкина
год_рождения = input("Введите год рождения А.С. Пушкина: ")

if год_рождения == "1799":
    день_рождения = input("Введите день рождения А.С. Пушкина (дд): ")
    if день_рождения == "06":
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")