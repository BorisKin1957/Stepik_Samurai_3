def pass_decorator(func):
    def wrapper(*args, **kwargs):
        for name, pasw in args[0].items():
            new_pasw = ''
            for symbol in pasw:
                if symbol not in '%#*&':
                    symbol = chr(ord(symbol) + 2)
                new_pasw += symbol
            args[0][name] = new_pasw
        result = func(*args, **kwargs)

        return result
    return wrapper


