def fizz_buzz(a, b):
    sum = 0
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    return sum

print('0-30:', fizz_buzz(15, 15))



def plural_form(int, *args):
    for i in args:
        if 5 <= int % 100 <= 20:
            i = args[2]
        elif 1 < int % 10 < 5:
            i = args[1]
        elif int % 10 == 1 and int != 11:
            i = args[0]
    return str(int) + ' ' + i


print(plural_form(5, 'яблоко', 'яблока', 'яблок'))



def html(*args, **kwargs):
    def decorator(dec_func):
        def wrapper(input_att):
            result_wrapper = dec_func(input_att)
            if kwargs:
                result_wrapper = f'>{result_wrapper}'
                attributes = ''
                for k, v in kwargs.items():
                    attributes += f'{k}="{v}"'
                for i in args:
                    result_wrapper = f'<{i} {attributes}{result_wrapper}</{i}>'
            else:
                for i in args:
                    result_wrapper = f'<{i}>{result_wrapper}</{i}>'
                
            return result_wrapper
        return wrapper
    return decorator

    
@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))
