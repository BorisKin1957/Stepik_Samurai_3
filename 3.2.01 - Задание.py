import password.modul.func as f
import password.data.users as u

flag = True
while flag:
    name = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    print('------------------------------------------------------------------------')
    result = f.registration(name, password, u.users)
    print('------------------------------------------------------------------------')
    if result:
        flag = False
