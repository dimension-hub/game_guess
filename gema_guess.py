import json
from random import randrange


def login_user():
    validation = input(r"Если вы уже уже зарегистрированы в игре введите 'y\n':" )
    if validation.isdigit() and validation == "y":
        gema_guess()
    elif validation.isdigit() and validation == "n":
        pass
    else:
        pass


def registration_user():
    print("Ваше имя не должно содержать цифры!")
    while True:
        name_user = input("Ваше имя: ").title()
        if name_user.isalpha():
            if is_valid_user(name_user):
                print("Пароль должен быть не менее 8 символов и содержать в себе цифру, большую букву и маленькую!")
                while True:
                    password_user = input("Ваш пароль: ")
                    if len(password_user) >= 8 and [i for i in password_user if i.isdigit()]:
                        if [i for i in password_user if i.isupper()] and [i for i in password_user if i.islower()]:
                            person = {
                                "name":name_user,
                                "password":password_user
                            }
                            return person
                        else:
                            print("Некорректный пароль, попробуйте еще раз!")
                    else:
                        print("Некорректный пароль, попробуйте еще раз!")
            else:
                print("Такое имя уже существует, придумайте новое!")
        else:
            print("Некорректный имя, попробуйте еще раз!")


def is_valid_user(name_user):
    try:
        json.load(open("db_result_users.json"))
    except:
        return True
    with open("db_result_users.json", "r") as file:
        date_file = json.loads(file.read())
        return [key for key in date_file if name_user not in key["name"]]


def is_valid_border(num):
    return num.isdigit() and 5 <= int(num) <= 100


def gen_random(person_dict):
    global is_valid_border
    name = person_dict.get("name")
    print(f"Добро пожаловать в числовую угадайку {name}")
    while True:
        num_border_user = input("задайте границу числа, не менее 5 и не более 100: ")
        if is_valid_border(num_border_user):
            num_border_user = int(num_border_user)
            number_random = randrange(1, num_border_user + 1)
            return number_random, num_border_user
        else:
            print("А может быть все-таки введем целое число от 5 до 100?")


def result_write_json(result_dict):
    try:
        date_result = json.load(open("db_result_users.json"))
    except:
        date_result = []
    date_result.append(result_dict)
    with open("db_result_users.json", "w") as file:
        json.dump(date_result, file, indent=2, ensure_ascii=False)


def gema_guess(*args):
    date_result_user, date_person_user = args
    num_random, border_user = date_result_user
    name_user, password_user = date_person_user.get("name"), date_person_user.get("password")
    print(num_random)
    total = 0
    while True:
        num_user = input("Введите число: ")
        if num_user.isdigit() and 1 <= int(num_user) <= border_user:
            num_user = int(num_user)
            if num_user == num_random:
                total += 1
                print(f"{name_user}, хорошая игра! Ваш результат: {num_random} количество попыток № {total}")
                result_parametr_user = {
                    "name":name_user,
                    "password":password_user,
                    "border":border_user,
                    "total":total
                }
                return result_parametr_user
            elif num_user > num_random:
                total += 1
                print("Ваше число больше")
            else:
                total += 1
                print("Ваше число меньше")
        else:
            print("Введите корректное число! Не забывайте ваше число должны входить ваш диапазон.")
    



def main():
    person = registration_user()
    numbers_user = gen_random(person)
    result = gema_guess(numbers_user, person)
    result_write_json(result)



if __name__ == "__main__":
    main()