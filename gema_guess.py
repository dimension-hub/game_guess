import json
from random import randrange


def record_the_results(name, password, border, total):
    point = 0
    for _ in range(1, int(border) + 1, 5): point += 1
    if int(total) >= 10: point += 5
    result_user = {
        "name":name,
        "password":password,
        "point":point
    }
    try:
        date = json.load(open("db_result_users.json"))
    except:
        date = []
        date.append(result_user)
        with open("db_result_users.json", "w") as file:
            json.dump(date, file, indent=2, ensure_ascii=False)
        return print(f"Ваш результат {point} очков, продолжайте в том же духе!")
    with open("db_result_users.json", "r") as file:
        date_file = json.loads(file.read())
    if name in [date_user.get("name") for date_user in date_file if name == date_user.get("name")]:
        point_max = max([date_user.get("point") for date_user in date_file if name == date_user.get("name")])
        if point > point_max:
            date.append(result_user)
            with open("db_result_users.json", "w") as file:
                json.dump(date, file, indent=2, ensure_ascii=False)
                if point > max([date_user.get("point") for date_user in date_file]):
                    return print(f"Вы показали лучший результат в игре и набрали {point} очков, поздравляем!")
                else:
                    return print(f"Вы улучшили свой рекорд, который сейчас составляет {point} очков!")
        else:
            return print(f"Ваш лучший результат в игре{point_max}")
    date.append(result_user)
    with open("db_result_users.json", "w") as file:
        json.dump(date, file, indent=2, ensure_ascii=False)
    if point > max([date_user.get("point") for date_user in date_file]):
        return print(f"Вы показали лучший результат в игре и набрали {point} очков, поздравляем!")
    else:
        return print(f"Ваш результат {point} очков, продолжайте в том же духе!")



def is_valid_user(name_user):
    try:
        json.load(open("db_result_users.json"))
    except:
        return True
    with open("db_result_users.json", "r") as file:
        date_file = json.loads(file.read())
    return name_user not in [date_user.get("name") for date_user in date_file]



def login_user():
    while True:
        validation = input(r"Если вы уже уже зарегистрированы в игре введите 'y\n': ")
        if validation == "y":
            name, password = input("Ваше имя: ").title(), input("Ваш пароль: ")
            try:
                json.load(open("db_result_users.json"))
            except:
                print("Вы еще не прошли регистрацию!")
                return registration_user()
            with open("db_result_users.json") as file:
                date_file = json.loads(file.read())
            if [key for key in date_file if key["name"] == name] and [key for key in date_file if key["password"] == password]:
                date_person = {
                    "name":name,
                    "password":password
                }
                return gen_random(date_person)
            else:
                print("Некорректные данные пользователя!")
        elif validation == "n":
            return registration_user()
        else:
            print("Некорректные данные!")



def registration_user():
    print("Ваше имя не должно содержать цифры!")
    while True:
        name_user = input("Ваше имя: ").title()
        if name_user.isalpha():
            if is_valid_user(name_user):
                print("Пароль должен быть не менее 8 символов и содержать в себе цифру, большую букву и маленькую!")
                password_user = input("Ваш пароль: ")
                if len(password_user) >= 8 and [i for i in password_user if i.isdigit()]:
                    if [i for i in password_user if i.isupper()] and [i for i in password_user if i.islower()]:
                        paremetr = {
                            "name": name_user,
                            "password":password_user
                        }
                        return gen_random(paremetr)
                    else:
                        print("Некорректный пароль, попробуйте еще раз!")
                else:
                    print("Некорректный пароль, попробуйте еще раз!")
            else:
                print("Такое имя уже существует, придумайте новое!")
        else:
            print("Некорректне имя, попробуйте еще раз!")



def is_valid_border(num):
    return num.isdigit() and 5 <= int(num) <= 100


def gen_random(person_dict):
    name, password = person_dict.get("name"), person_dict.get("password")
    print(f"Добро пожаловать в числовую угадайку {name}")
    while True:
        num_border_user = input("задайте границу числа, не менее 5 и не более 100: ")
        if is_valid_border(num_border_user):
            num_border_user = int(num_border_user)
            number_random = randrange(1, num_border_user + 1)
            return gema_guess(name, password, number_random, num_border_user)
        else:
            print("А может быть все-таки введем целое число от 5 до 100?")


def gema_guess(*args):
    name, password, num_random, num_border_user = args
    total = 0
    while True:
        num_user = input("Введите число: ")
        if num_user.isdigit() and 1 <= int(num_user) <= num_border_user:
            num_user = int(num_user)
            if num_user == num_random:
                total += 1
                print(f"{name}, хорошая игра! Ваш результат: {num_random} количество попыток № {total}")
                return record_the_results(name, password, num_border_user, total)
            elif num_user > num_random:
                total += 1
                print("Ваше число больше загаданного")
            else:
                total += 1
                print("Ваше число меньше загаданного")
        else:
            print("Введите корректное число! Не забывайте ваше число должны входить ваш диапазон.")
    



def main():
    login_user()




if __name__ == "__main__":
    main()