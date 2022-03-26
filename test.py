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

