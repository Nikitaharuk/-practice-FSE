password = input()
if len(password) != 8:
    print("����� ������ �� ����� 8")
else :
    if not any(char.isupper() for char in password):
       print ("� ������ ����������� ��������� �����")
    else:
        if not any(char.islower() for char in password):
            print ("� ������ ����������� �������� �����")
        else:
            if not any(char.isdigit() for char in password):
                print("� ������ ����������� �����")
            else:
                special_chars = {'!', '#', '$', '%', '&', '*', '+', '-', ':', ';', '<', '=', '>', '?', '@', '^', '_'}
                if not any(char in special_chars for char in password):
                    print("� ������ ����������� ����������� �������")
                else:
                    print("�������� ������")