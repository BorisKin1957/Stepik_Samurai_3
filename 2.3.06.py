def f_1() -> callable:
    result, key = {}, 1

    def f_2(value: str) -> dict:
        nonlocal key
        result[key] = value
        key += 1
        return result

    return f_2


x = f_1()
print(x('один'))
print(x('два'))
print(x('три'))
