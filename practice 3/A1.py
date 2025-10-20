password = input()
if len(password) != 8:
    print("Длина пароля не равна 8")
else :
    if not any(char.isupper() for char in password):
       print ("В пароле отсутствуют заглавные буквы")
    else:
        if not any(char.islower() for char in password):
            print ("В пароле отсутствуют строчные буквы")
        else:
            if not any(char.isdigit() for char in password):
                print("В пароле отсутствуют цифры")
            else:
                special_chars = {'!', '#', '$', '%', '&', '*', '+', '-', ':', ';', '<', '=', '>', '?', '@', '^', '_'}
                if not any(char in special_chars for char in password):
                    print("В пароле отсутствуют специальные символы")
                else:
                    print("Надежный пароль")