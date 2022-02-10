# [1, 4.7, ‘hi’, False, None]
# Необходимо создать из него словарь с ключами “int”, “float”, “str”, “bool”, “none” и соответствующим значением из списка.
# Вместо этих значений в списке и их порядок могут быть и другие, напишите код, который будет работать с любыми значениями, то есть он должен быть универсальным
# Например из списка
# [True, 2.3, None, “brook”, 5]
# Надо получить:
# {
# “float”: 2.3,
# “bool”: True,
# “none”: None,
# “int”: 5,
# “str”: “brook”
# }


def func(list):

    dict = {}

    for i in list:

        if isinstance(i, float):
            dict.update({'float': i})
        elif isinstance(i, str):
            dict.update({'str': i})
        elif isinstance(i, bool):
            dict.update({'bool': i})
        elif isinstance(i, int):
            dict.update({'int': i})
        else:
            dict.update({'none': i})
    return dict

list = [1, 4.7, 'hi', False, None]

print(func(list))
