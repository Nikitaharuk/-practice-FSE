import string
password = input()
isValid = True
allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
errors = ""


if len(password) != 8:
    errors = errors + '�������� ����� ������ \n'
    isValid = False
if password.lower() == password:
    errors = errors + '����������� ��������� ����� \n'
    isValid = False
if password.upper() == password:
    errors = errors + '����������� �������� ����� \n'
    isValid = False
if not any(map(str.isdigit, password)):
    errors = errors + '����������� ����� \n'
    isValid = False
if ('*' not in password) and ('-' not in password) and ('#' not in password):
    errors = errors + '����������� ����������� ������� \n'
    isValid = False
if (set(password) - set(allowed_sym)) != set():
    errors = errors + '������������ ������������ ������� \n'
    isValid = False
if isValid == True:
    print("�������� ������")
else:
    print("������ �� �������� \n")
    print(errors)