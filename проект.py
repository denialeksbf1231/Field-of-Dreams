import random
qw = 1
qr = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
print("Здравствуйте.Данная игра работает по правилам телевизионной программы:поле чудес,детской игры:виселица или популярной браузерной игры:wordle.Смысл заключается в том что вам загадывается русское слово на тематику море,вода.Ваша задача вводить либо буквы слова либо слово полностью.Если вы полногстью ввели слово и не угадали,", end="")
print("вы сразу проигрываете.Все слова начинаются с маленькой буквы,они только в единственном числе,в них нет тире и других знаков.Если вы вводите букву,которой нет в слове, звездочки в слове не меняются.Если вы вводите букву,которая есть в слове,звездочки,на местах которых расположены буквы,превращаются в эти буквы.Команды:")
print("1: !letter - показывает какие буквы вы уже вводили")
print("2: !mystery - показывает сколько букв вам еще надо отгадать")
print("3: !help - показать другие комманды")
print("4: !giveup - сдаться")
while True:
    gt = "1"
    giveup = 0
    if qw == "2":
        break
    game = 1
    op = ["якорь", "океан", "вода", "корабль", "ракушка", "акваланг", "аквариум", "рыба", "судно", "подлодка", "коралл", "пирс", "посейдон", "русалка", "волна", "бриз", "лодка", "акула", "палуба", "юнга", "моряк", "море", "озеро", "река", "пляж", "остров", "прилив", "отлив", "осьминог", "моллюск", "раковина"]
    op2 = ["рак", "омар", "дельфин", "косатка", "тюлень", "скат", "угорь"]
    op.extend(op2)
    a = random.choice(op)
    f = op.index(a)
    del op[f]
    qt = len(a)
    z = list(a)
    print("В слове -", len(a), "букв")
    w = len(a)
    s = w * "*"
    s = list(s)
    d = list(a)
    h = list()
    c = len(a)
    k = ["1", "2"]
    x = [2, 3, 4]
    y = [5, 6, 7, 8, 9]
    x.append(1)
    while game == 1:
        if game == 2:
            break
        while True:
            print("Вы желаете ввести букву или слово?(1 - букву, 2 - слово)")
            q = input()
            y = ("1", "2")
            if q in y:
                break
        if q == "1":
            while True:
                print("Введите букву")
                qe = input()
                qe = qe.lower()
                if qe == "!letter":
                    if len(h) == 0:
                        print("Вы еще не использовали буквы")
                    else:
                        print("Вы использовали буквы:",* h)
                elif qe == "!mystery":
                    print("Вам осталось отгадать:", qt, "букв")
                elif qe == "!help":
                    print("Данная игра работает по правилам телевизионной программы:поле чудес,детской игры:виселица или популярной браузерной игры:wordle.Смысл заключается в том что вам загадывается русское слово на тематику море,вода.Ваша задача вводить либо буквы слова либо слово полностью.Если вы полногстью ввели слово и не угадали,", end="")
                    print("вы сразу проигрываете.Все слова начинаются с маленькой буквы,они только в единственном числе,в них нет тире и других знаков.Если вы вводите букву,которой нет в слове, звездочки в слове не меняются.Если вы вводите букву,которая есть в слове,звездочки,на местах которых расположены буквы,превращаются в эти буквы.Команды:")
                    print("1: !letter - показывает какие буквы вы уже вводили")
                    print("2: !mystery - показывает сколько букв вам еще надо отгадать")
                    print("3: !giveup - сдаться")
                elif qe == "!giveup":
                    print("Вы сдались.У вас оставалось:",c, "жизней,слово было:", a)
                    while True:
                        print("Желаете продолжить?Если да,то введите 1, если нет,то 2.")
                        qw = input()
                        if qw in k:
                            game = 2
                            break
                    giveup = 1
                    game = 2
                    break
                elif qe not in h and qe in qr:
                    break
                elif qe in h:
                    print("Вы уже вводили эту букву")
                elif qe not in qr:
                    print("Пожалуйста,введите букву из русского алфавита")
                elif len(qe) != 1:
                    print("Пожалуйста,введите одну букву")
            if giveup == 1:
                break
            h.append(qe)
            for i in d:
                f = d.index(i)
                if i == qe:
                    s[f] = d[f]
                    d[f] = "*"
                    qt = qt - 1
            c = c - 1
            print(*s)
            if c in x:
                print("У вас осталось", c, "жизни")
            elif c == 1:
                print("У вас осталось", c, "жизнь")
            elif c in y:
                print("У вас осталось", c, "жизней")
            if c == 0:
                print("У вас закончились жизни.слово - ", a)
                while True:
                    print("Желаете продолжить?Если да,то введите 1, если нет,то 2.")
                    qw = input()
                    if qw in k:
                        game = 2
                        break
        if q == "2":
            while game != 2:
                if game == 2:
                    break
                f = 0
                print("Введите слово")
                qe = input()
                qe = qe.lower()
                if qe == "!letter":
                    f = 1
                    if len(h) == 0:
                        print("Вы еще не использовали буквы")
                    else:
                        print("Вы использовали буквы:",* h)
                elif qe == "!mystery":
                    f = 1
                    print("Вам осталось отгадать:", qt, "букв")
                elif qe == "!help":
                    print("Данная игра работает по правилам телевизионной программы:поле чудес,детской игры:виселица или популярной браузерной игры:wordle.Смысл заключается в том что вам загадывается русское слово на тематику море,вода.Ваша задача вводить либо буквы слова либо слово полностью.Если вы полногстью ввели слово и не угадали,", end="")
                    print("вы сразу проигрываете.Все слова начинаются с маленькой буквы,они только в единственном числе,в них нет тире и других знаков.Если вы вводите букву,которой нет в слове, звездочки в слове не меняются.Если вы вводите букву,которая есть в слове,звездочки,на местах которых расположены буквы,превращаются в эти буквы.Команды:")
                    print("1: !letter - показывает какие буквы вы уже вводили")
                    print("2: !mystery - показывает сколько букв вам еще надо отгадать")
                    print("3: !giveup - сдаться")
                    f = 1
                elif qe == "!giveup":
                    f = 1
                    print("Вы сдались.У вас оставалось:",c, "жизней,слово было:", a)
                    while True:
                        print("Желаете продолжить?Если да,то введите 1, если нет,то 2.")
                        qw = input()
                        if qw in k:
                            game = 2
                            break
                        giveup = 1
                        game = 2
                        break
                if qe == a:
                    while True:
                        print("Вы выиграли!У вас осталось:", c, "Жизней,желаете продолжить?Если да,то введите 1, если нет,то 2.")
                        qw = input()
                        if qw in k:
                            game = 2
                            break
                elif qe != a and f == 0:
                    print("Вы проиграли.слово - ", a)
                    while True:
                        print("Желаете продолжить?Если да,то введите 1, если нет,то 2.")
                        qw = input()
                        if qw in k:
                            game = 2
                        break

    

