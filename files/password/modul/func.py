import files.password.data.users as u
import files.password.modul.decorator as d


def registration(name, psw, lst=u.users):
    if len(name) < 6:
        print("Имя должно быть не менее 6 символов.")
        return False
    if '#' not in psw or '&' not in psw or '*' not in psw or '%' not in psw or len(psw) < 6:
        print("Пароль должен быть не менее из 6 символов и содержать %, #, *, &.")
        return False
    if name in [list(i.items())[0][0] for i in lst]:
        print("Пользователь с таким именем уже существует.")
        return False
    else:
        data_append({name: psw}, lst)
        print("Регистрация прошла успешно!")
        print(lst)
        return True


@d.pass_decorator
def data_append(dct, lst=u.users):
    lst.append(dct)
