from typing import Tuple

from exceptions import TaskException


def task1(x: [float, int], y: [float, int]) -> int:
    """
    Даны действительные числа x и y.
    Вернуть (|x| − |y|) / (1+ |xy|)
    """
    return (x - y) / (1 + (x * y))


def task2(a: [float, int]) -> tuple[int, int]:
    """
    Дана длина ребра куба.
    Вернуть кортеж с объемом куба и площадью его боковой поверхности.
    """
    v = a ** 3
    s = (4 * a ** 2)/4
    return (v, s)


def task3(a: [float, int], b: [float, int]) -> int:
    """
    Даны два катета прямоугольного треугольника.
    Вернуть длину гипотенузы.
    """
    return (a ** 2 + b ** 2) ** 0.5


def task4(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную предпоследнему символу введенной строки.
    """
    return string[-2]


def task5(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную первым пяти символам введенной строки.
    """
    return string[:5]


def task6(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную введенной строку без последних двух символов.
    """
    return string[:-2]


def task7(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную всем элементам введенной строки с четными индексами.
    """
    return string[::2]


def task8(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную третьему символу введенной строки.
    """
    return string[2]


def task9(string: str) -> str:
    """
    Дана строка. Если длина строки больше 10 символов, то вернуть новую строку
    с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
    Если меньше 10, то вывести на экран второй символ строки
    """
    if len(string) > 10:
        print("!!!")
        return f"{string}!!!"
    else:
        return string[1]


def task10(string: str) -> tuple[str, str | None]:
    """
    Дана строка. Вернуть букву, которая находится в середине этой строки.
    Также, если эта центральная буква равна первой букве в строке, то вернуть часть строки между первым и
    последним символами исходной строки.
    (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
    Для создания результирующий строки используйте срез)
    """
    meridian = int(len(string) / 2)
    srez = None
    if string[0] == string[meridian]:
        srez = string[1:-1]
    return tuple(string[meridian], srez)


def task11(string: str) -> bool:
    """
    Напишите функцию которая проверяет является ли строка палиндромом.
    Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
    """
    if string == string[::-1]:
        return True
    else:
        return False


def task12(string: str, symbol: str) -> int:
    """
    Напишите функцию которая возвращает сколько раз символ встречается в строке
    """
    count = 0
    for i in string:
        if i == symbol:
            count += 1
    return count


def task13(number: int) -> bool:
    """
    Дано число. Если это число делится на 1000 без остатка, то верните True иначе False
    """
    if number % 1000 == 0:
        return True
    else:
        return False


def task14(guests_count: int) -> str:
    """
    В семье N свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от количества гостей.
    Если их будет больше 50 - закажут ресторан, если от 20 до 50 - кафе, а если меньше 20 - отпразднуют дома.
    Вернуть "ресторан", "кафе", "дом" в зависимости от количества гостей.
    """
    if guests_count > 50:
        return "ресторан"
    elif 20 <= guests_count <= 50:
        return "кафе"
    elif guests_count < 20:
        return "дом"


def micro_calc(a: [float, int], b: [float, int], sign: str) -> [float, int, str]:
    """
    Даны 2 действительных числа и строка с арифметическим знаком ('+', '-', ':', '*', '^')
    Необходимо вернуть результат арифметической операции
    В случае ошибки вычислений или неизвестного знака вернуть строку "error"
    """
    try:
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == ':':
            return a / b
        elif sign == '*':
            return a * b
        elif sign == '^':
            return a ** b
    except ZeroDivisionError:
        return 'error'


def big_letters(phrase: str) -> str:
    """
    Напишите функцию, которая принимает строку, состоящую только из букв ASCII и пробелов, и возвращает
    эту строку печатными буквами шириной 5 символов и высотой 7 символов с одним пробелом между символами.
     - Заглавные буквы должны состоять из соответствующих заглавных букв.
     - Не имеет значения, состоит ли ввод из строчных или прописных букв.
     - Любые начальные и/или конечные пробелы во входных данных следует игнорировать.
     - Пустые строки или подобные строки, содержащие только пробелы, должны возвращать пустую строку.
     - Остальные пробелы (между буквами и/или словами) должны рассматриваться как любые другие символы.
       Это означает, что на входной пробел будет шесть пробелов в выводе или кратно шести,
       если пробелов было больше - плюс один от предыдущего символа!
     - Конечные пробелы должны быть удалены в результирующей строке.
     - Строка должна быть отформатирована таким образом, чтобы при передаче функции Python print()
       отображался желаемый результат (см., например, ниже)

      AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M N   N  OOO  PPPP   QQQ  RRRR   SSS
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM NN  N O   O P   P Q   Q R   R S   S
     A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M N   N O   O P   P Q   Q R   R S
     AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M N N N O   O PPPP  Q   Q RRRR   SSS
     A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M N   N O   O P     Q Q Q R R       S
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M N  NN O   O P     Q  QQ R  R  S   S
     A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M N   N  OOO  P      QQQQ R   R  SSS

    TTTTT U   U V   V W   W X   X Y   Y ZZZZZ
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W  X X   Y Y     Z
      T   U   U V   V W W W   X     Y     Z
      T   U   U V   V W W W  X X    Y    Z
      T   U   U  V V  W W W X   X   Y   Z
      T    UUU    V    W W  X   X   Y   ZZZZZ
    """

    alphabet = [
        [[' AAA '], ['A   A'], ['A   A'], ['AAAAA'], ['A   A'], ['A   A'], ['A   A']],
        [['BBBB '], ['B   B'], ['B   B'], ['BBBB '], ['B   B'], ['B   B'], ['BBBB ']],
        [[' CCC '], ['C   C'], ['C    '], ['C    '], ['C    '], ['C   C'], [' CCC ']],
        [['DDDD '], ['D   D'], ['D   D'], ['D   D'], ['D   D'], ['D   D'], ['DDDD ']],
        [['EEEEE'], ['E    '], ['E    '], ['EEEEE'], ['E    '], ['E    '], ['EEEEE']],
        [['FFFFF'], ['F    '], ['F    '], ['FFFFF'], ['F    '], ['F    '], ['F    ']],
        [[' GGG '], ['G   G'], ['G    '], ['G GGG'], ['G   G'], ['G   G'], [' GGG ']],
        [['H   H'], ['H   H'], ['H   H'], ['HHHHH'], ['H   H'], ['H   H'], ['H   H']],
        [['IIIII'], ['  I  '], ['  I  '], ['  I  '], ['  I  '], ['  I  '], ['IIIII']],
        [['JJJJJ'], ['    J'], ['    J'], ['    J'], ['    J'], ['    J'], ['JJJJ ']],
        [['K   K'], ['K  K '], ['K K  '], ['KK   '], ['K K  '], ['K  K '], ['K   K']],
        [['L    '], ['L    '], ['L    '], ['L    '], ['L    '], ['L    '], ['LLLLL']],
        [['M   M'], ['MM MM'], ['M M M'], ['M   M'], ['M   M'], ['M   M'], ['M   M']],
        [['N   N'], ['NN  N'], ['N   N'], ['N N N'], ['N   N'], ['N  NN'], ['N   N']],
        [[' OOO '], ['O   O'], ['O   O'], ['O   O'], ['O   O'], ['O   O'], [' OOO ']],
        [['PPPP '], ['P   P'], ['P   P'], ['PPPP '], ['P    '], ['P    '], ['P    ']],
        [[' QQQ '], ['Q   Q'], ['Q   Q'], ['Q   Q'], ['Q Q Q'], ['Q  QQ'], [' QQQQ']],
        [['RRRR '], ['R   R'], ['R   R'], ['RRRR '], ['R R  '], ['R  R '], ['R   R']],
        [[' SSS '], ['S   S'], ['S    '], [' SSS '], ['    S'], ['S   S'], [' SSS ']],
        [['TTTTT'], ['  T  '], ['  T  '], ['  T  '], ['  T  '], ['  T  '], ['  T  ']],
        [['U   U'], ['U   U'], ['U   U'], ['U   U'], ['U   U'], ['U   U'], [' UUU ']],
        [['V   V'], ['V   V'], ['V   V'], ['V   V'], ['V   V'], [' V V '], ['  V  ']],
        [['W   W'], ['W   W'], ['W   W'], ['W W W'], ['W W W'], ['W W W'], [' W W ']],
        [['X   X'], ['X   X'], [' X X '], ['  X  '], [' X X '], ['X   X'], ['X   X']],
        [['Y   Y'], ['Y   Y'], [' Y Y '], ['  Y  '], ['  Y  '], ['  Y  '], ['  Y  ']],
        [['ZZZZZ'], ['    Z'], ['   Z '], ['  Z  '], [' Z   '], ['Z    '], ['ZZZZZ']]
    ]

    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    q = 0
    res = ''
    s = 0
    while s != 7:
        if len(phrase.strip().upper()) != 0:
            for i in phrase.strip().upper():
                if i == ' ':
                    res += '      '
                else:
                    w = az.index(i)
                    res += alphabet[w][q][0]
                    res += ' '
        else:
            res += ''
            break
        q += 1
        res = res.rstrip()
        if s != 6:
            res += '\n'
        s += 1

    return res


def perfect_square(square: str) -> bool:
    """
    Напишите функцию, которая проверяет входную строку. Если строка представляет собой идеальный квадрат,
    верните true, в противном случае — false.
     - Символ '.' — правильный квадрат (1x1)
     - Правильные квадраты могут содержать только '.' и необязательно '\n' (перевод строки).
     - Идеальные квадраты должны иметь одинаковую ширину и высоту.
    """
    included = ['.', '\n']
    included2 = ['.']
    unique = list(set(square))
    included.sort()
    unique.sort()

    if included == unique or included2 == unique:
        if list(square) == list(square)[::-1]:
            return True
    else:
        return False

