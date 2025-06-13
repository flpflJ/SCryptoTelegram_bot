import base64
import re
import math
import random
import io
import matplotlib.pyplot as plt
def atbashcrypt(message):
    rusalph = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    rusalphdict = dict(zip(rusalph, list(range(len(rusalph)))))
    engalph = list('abcdefghijklmnopqrstuvwxyz')
    engalphdict = dict(zip(engalph, list(range(len(engalph)))))
    numbers = list('0123456789')
    txt = message
    upper = [i for i in range(len(txt)) if txt[i].isupper()]
    txt = txt.lower()
    result = ""
    for s in txt:
        if s in rusalph:
            result = "".join([result, rusalph[len(rusalph) - 1 - rusalphdict[s]]])
        elif s in engalph:
            result = "".join([result, engalph[len(engalph) - 1 - engalphdict[s]]])
        elif s in numbers:
            result = "".join([result, numbers[len(numbers) - 1 - int(numbers[int(s)])]])
        else:
            result = "".join([result, s])
    resultlist = list(result)
    for l in upper:
        resultlist[l] = resultlist[l].upper()
    result = ''.join(resultlist)
    return result

def caesarcrypt(message, key: int, flag):
    ruslaphupper = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    ruslaphupperd = dict(zip(ruslaphupper, list(range(len(ruslaphupper)))))
    rusalphlower = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    ruslaphlowerd = dict(zip(rusalphlower, list(range(len(rusalphlower)))))
    engalphlower = list("abcdefghijklmnopqrstuvwxyz")
    engalphlowerd = dict(zip(engalphlower, list(range(len(engalphlower)))))
    engalphupper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    engalphupperd = dict(zip(engalphupper, list(range(len(engalphupper)))))
    numbers = list("0123456789")
    result = []
    try:
        key = int(key)
        if flag == 1:
            key = -key
        for i in range(len(message)):
            if message[i] in ruslaphupper:
                result.append(ruslaphupper[(ruslaphupperd[message[i]] + key)%(len(ruslaphupper))])
            elif message[i] in rusalphlower:
                result.append(rusalphlower[(ruslaphlowerd[message[i]] + key) % (len(rusalphlower))])
                #print((ruslaphlowerd[message[i]] + key))
            elif message[i] in engalphlower:
                result.append(engalphlower[(engalphlowerd[message[i]] + key) % (len(engalphlower) )])
            elif message[i] in engalphupper:
                result.append(engalphupper[(engalphupperd[message[i]] + key) % (len(engalphupper))])
            elif message[i] in numbers:
                result.append(numbers[(int(numbers[int(message[i])]) + key) % (len(numbers))])
            else:
                result.append(message[i])
        return ''.join(result)
    except (ValueError, TypeError):
        return 'Введено неккоректное смещение либо некорректное сообщение. Введите число в смещение, либо текст.'

def richelieu(message,key,flag):
    try:
        validation_pattern = r'^(\(\d+(?:,\d+)*\))+$'
        if not re.match(validation_pattern, key):
            return "Ошибка: Строка не соответствует формату (x,y,z,...)(x,y,z,...)..." #idk
        f = ''
        group_pattern = r'\((\d+(?:,\d+)*)\)'
        groups = re.findall(group_pattern, key)
        result = [group.split(',') for group in groups]
        lenof = 0
        for r in result:
            testr = [str(i) for i in range(1,len(r)+1)]
            if not(set(r) == set(testr)):
                return 'Некорректный ключ!'
            lenof += len(r)
        if lenof > len(message):
            return 'Некорректный ключ!'

        d = 0
        if flag == 0:
            for r in result:
                for i in range(len(r)):
                    f += f.join(message[d+int(r[i])-1])
                d+=len(r)
        else:
            f = list(message)
            for r in result:
                for i in range(len(r)):
                    #f = list(message)
                    f[d+int(r[i])-1] = message[d+i]
                d += len(r)
            f = ''.join(f)
        if(d != len(message)):
            f += "".join(message[d:])
        return f
    except TypeError:
        return 'Некорректный ключ, либо нет сообщения.'

def gronsfeld_cipher(message,key: str,flag):
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    pattern = r'^\d+$'
    if not re.fullmatch(pattern, key):
        return 'Некорректный ключ. Это может быть только число.'
    message_formatted = []
    for i in range(len(message)):
        if message[i] in alph:
            message_formatted.append(alph.find(message[i]))
    len_key = (len(message_formatted) // len(key)) * key + key[:(
                len(message_formatted) % len(key))]
    res = ''
    if flag == 0:
        for i in range(len(message_formatted)):
            message_formatted[i] = (int(message_formatted[i]) + int(len_key[i])) % len(alph)
            res += alph[message_formatted[i]]
    else:
        for i in range(len(message_formatted)):
            message_formatted[i] = (int(message_formatted[i]) + int(len_key[i]) * -1) % len(alph)
            res += alph[message_formatted[i]]
    for i in range(len(message)):
        if message[i] not in alph:
            res = res[:i] + message[i] + res[i:]
    return res

def vigenere_cipher(message,key,flag):
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    message_formatted = []
    k = []
    key_formatted = ''
    for i in range(len(message)):
        if message[i] in alph:
            message_formatted.append(alph.find(message[i]))
    for i in range(len(key)):
        if key[i] in alph:
            key_formatted+=key[i]
    len_key = (len(message_formatted) // len(key_formatted)) * key_formatted + key_formatted[:(len(message_formatted)%len(key_formatted))]
    for i in range(len(len_key)):
        if len_key[i] in alph:
            k.append(alph.find(len_key[i]))
    result = []
    if flag == 0:
        for i in range(len(k)):
            result.append((message_formatted[i]+k[i])%len(alph))
    else:
        for i in range(len(k)):
            result.append((message_formatted[i]-k[i])%len(alph))
    res = ''
    for _ in result:
        res += alph[_]
    for i in range(len(message)):
        if message[i] not in alph:
            res = res[:i] + message[i] + res[i:]
    return res

def split_bigrams(text):
    mas = []
    strk = ""
    for ind, k in enumerate(text):
        if len(strk) == 0:
            strk += k
        else:
            if strk[0] == k and k == '~':
                strk += '#'
                mas.append(strk)
                strk = k
            elif strk[0] == k:
                strk += '~'
                mas.append(strk)
                strk = k
            else:
                strk+= k
                mas.append(strk)
                strk = ""
    if strk and strk != '~':
        mas.append(strk + '~')
    elif strk and strk == '~':
        mas.append(strk + '#')
    return mas

def form_matrix(alph, text):
    unique_chars = set()
    for alphab in alph.values():
        unique_chars.update(alphab)
    unique_chars = sorted(unique_chars)
    pattern = f"^[{''.join(re.escape(c) for c in unique_chars)}]+$"
    if not re.fullmatch(pattern, text):
        return 'Использован недопустимый алфавит в сообщении или ключе'
    for char in "".join(dict.fromkeys(text)):
        unique_chars.remove(char)
    return unique_chars

def playfair_cipher(message,key,flag):
    if flag == 1 and len(message) % 2 != 0:
        return 'Неверная длина сообщения'
    alphabets = {
        "ru": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "RU": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "en": "abcdefghijklmnopqrstuvwxyz",
        "EN": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "digits": "0123456789",
        "specs": " ,.!@#$%^&*()-=_+<>?/~"
    }
    matrix = list("".join(dict.fromkeys(key))) + form_matrix(alphabets, key)
    key_list = []
    if flag == 0:
        bigrams = split_bigrams(message)
    else:
        bigrams = [message[i:i + 2] for i in range(0, len(message), 2)]
    res = ''
    for i in range(15):
        tmp = []
        for j in range(10):
            tmp.append(matrix[i*10+j])
        key_list.append(tmp)
    matrix = key_list
    for bigram in bigrams:
        tmp_b = ''
        x0,y0,x1,y1,f0,f1 = (0,)*6
        for i in range(15):
            for j in range(10):
                if bigram[0] == matrix[i][j]:
                    x0,y0=i,j
                    f0 = 1
                if bigram[1] == matrix[i][j]:
                    x1,y1=i,j
                    f1=1
                if f0 and f1:
                    break
            if f0 and f1:
                break
        if x0 == x1:
            if(flag == 0):
                tmp_b += matrix[x0][(y0+1)%10]
                tmp_b += matrix[x1][(y1+1)%10]
            else:
                tmp_b += matrix[x0][(y0-1)%10]
                tmp_b += matrix[x1][(y1-1)%10]
        elif y0 == y1:
            if flag == 0:
                tmp_b += matrix[(x0+1)%15][y0]
                tmp_b += matrix[(x1+1)%15][y1]
            else:
                tmp_b += matrix[(x0-1)%15][y0]
                tmp_b += matrix[(x1-1)%15][y1]
        else:
            tmp_b += matrix[x0][y1]
            tmp_b += matrix[x1][y0]
        res += tmp_b
    if flag == 0:
        return res
    else:
        return res.replace('~', '')
#lab7
def replace_symbol(text,result_dict):
    result=[]
    for ch in text:
        original_case_char = ch
        check_char = ch.upper()

        replacement = result_dict.get(check_char, None)

        if replacement is not None:
            if original_case_char.islower():
                replacement = replacement.lower()
            else:
                replacement = replacement.upper()
            result.append(replacement)
        else:
            result.append(original_case_char)

    final_string = "".join(result)

    return final_string


def symbol_count(text):
    try:
        ra = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        ea = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rd = dict.fromkeys(ra,0)
        ed = dict.fromkeys(ea, 0)
        smbcnt = 0
        text = text.upper()
        for _ in text:
            if _ in ra or _ in ea:
                smbcnt+=1
        for key in rd:
            rd[key] = round(text.count(key)/smbcnt,3)
        for key in ed:
            ed[key] = round(text.count(key)/smbcnt,3)
        return rd, ed, smbcnt
    except ZeroDivisionError:
        print('Текст не может быть пустой.')

def generate_hist(rd, flag):
    keys = list(rd.keys())
    values = list(rd.values())
    plt.figure(figsize=(8, 5))
    plt.bar(keys, values, color='skyblue')
    if flag == 0:
        plt.title("Гистограмма букв русского алфавита")
    else:
        plt.title("Гистограмма букв английского алфавита")
    plt.xlabel("Буква")
    plt.ylabel("Частота появления")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    stringbytes = io.BytesIO()
    plt.savefig(stringbytes, format='jpg')
    stringbytes.seek(0)
    return base64.b64encode(stringbytes.read()).decode()

def ind_of_c(text):
    reference_prob_ru = {
        "Р": 0.040, "Я": 0.018, "Х": 0.009, "О": 0.090, "В": 0.038, "Ы": 0.018, "Ж": 0.007, "Е": 0.072, "Ё": 0.072, "Л": 0.035, "З": 0.016, "Ю": 0.006, "А": 0.062,
        "К": 0.028, "Ъ": 0.014, "Ь": 0.014, "Ш": 0.006, "И": 0.062, "М": 0.026, "Б": 0.014, "Ц": 0.004, "Н": 0.053, "Д": 0.025, "Г": 0.013, "Щ": 0.003, "Т": 0.053,
        "П": 0.023, "Ч": 0.012, "Э": 0.003, "С": 0.045, "У": 0.021, "Й": 0.010, "Ф": 0.002
    }
    reference_prob_en = {
        "E": 0.123, "L": 0.040, "B": 0.016, "T": 0.096, "D": 0.036, "G": 0.016, "A": 0.081, "C": 0.032, "V": 0.009, "O": 0.079, "U": 0.031, "K": 0.005, "N": 0.072,
        "P": 0.023, "Q": 0.002, "I": 0.071, "F": 0.023, "X": 0.002, "S": 0.066, "M": 0.022, "J": 0.001, "R": 0.060, "W": 0.020, "Z": 0.001, "H": 0.051, "Y": 0.019
    }
    rd,ed,smbcnt=symbol_count(text)
    sorted_ru = dict(sorted(reference_prob_ru.items(), key=lambda item: item[1]))
    sorted_en = dict(sorted(reference_prob_en.items(), key=lambda item: item[1]))
    rd_sorted = dict(sorted(rd.items(), key=lambda item: item[1]))
    ed_sorted = dict(sorted(ed.items(), key=lambda item: item[1]))
    edd = dict(sorted(dict(zip(ed_sorted.keys(),sorted_en.keys())).items(), key=lambda item: item))
    kd = dict(sorted(dict(zip(rd_sorted.keys(),sorted_ru.keys())).items(), key=lambda item: item))
    return kd,edd

def parse_validate_pairs(str):
    pattern = (
        r'^\s*'
        r'([A-ZА-ЯЁa-zа-яё]\s*-\s*[A-ZА-ЯЁa-zа-яё])'
        r'(?:\s*,\s*([A-ZА-ЯЁa-zа-яё]\s*-\s*[A-ZА-ЯЁa-zа-яё]))*'
        r'\s*$'
    )
    if not re.fullmatch(pattern,str.upper(),flags=re.IGNORECASE):
        return None, 'Невалидный ввод. Формат должен быть вида: А - Б (пробелы значения не имеют, как и регистр)'
    pairs = re.findall(
        r'\s*([A-ZА-ЯЁa-zа-яё])\s*-\s*([A-ZА-ЯЁa-zа-яё])\s*',
        str.upper(),
        flags=re.IGNORECASE
    )
    EN_LETTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    RU_LETTERS = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    for pair in pairs:
        first, second = pair[0].upper(), pair[1].upper()

        lang_first = 0 if first in EN_LETTERS else 1 if first in RU_LETTERS else None
        lang_second = 0 if second in EN_LETTERS else 1 if second in RU_LETTERS else None
        if lang_first != lang_second:
            return 'Невалидный ввод. Алфавиты не совпадают.'
    left = [pair[0].upper() for pair in pairs]
    right = [pair[1].upper() for pair in pairs]

    return left, right

def swap_symbol(left,right, res_dict):
    for i in range(len(left)):
        for k, v in res_dict.items():
            if v == right[i]:
                res_dict[k] = res_dict[left[i]]
        res_dict[left[i]] = right[i]

def check_alphabets(msg):
    ra = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ea = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    euf,ruf = 0,0
    for i in msg.upper():
        if i in ra:
            ruf = 1
            break
    for i in msg.upper():
        if i in ea:
            euf = 1
            break
    return euf,ruf
#lab8
def LCG(Xn,a,c,m):
    return (a * Xn + c) % m

def rand_gen(length : int, seed : int = 1,a : int = 1002378,c : int = 101393193,m : int = 22167236):
    if m is None:
        m = 22167236
    if c is None:
        c = 101393193
    if a is None:
        a = 1002378
    if seed is None:
        seed = 1
    res = []
    Xn = seed
    for _ in range(length):
        Xn = LCG(Xn, a, c, m)
        res.append(Xn)
    gamma = bytearray()
    for num in res:
        if num >= 4294967295:
            num = num % 4294967295
        gamma.extend(num.to_bytes(4, byteorder='little'))
    return gamma[:length]

def gamma(text,key):
    return bytes([a^b for a,b in zip(text,key)])
#def gamma(text,key):
#    return bytes(np.bitwise_xor(np.frombuffer(text), key))

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35,
    27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def str_to_bits(s):
    return [int(b) for byte in s.encode('utf-8') for b in format(byte, '08b')]

def bits_to_str(b):
    return bytes(int(''.join(map(str, b[i:i+8])), 2) for i in range(0, len(b), 8)).decode('utf-8', errors='ignore')

def permute(block, table):
    return [block[i - 1] for i in table]

def split_in_half(block):
    mid = len(block) // 2
    return block[:mid], block[mid:]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def pad_bits(bits):
    pad_len = 64 - (len(bits) % 64)
    pad_byte = [int(b) for b in format(pad_len // 8, '08b')]
    return bits + pad_byte * (pad_len // 8)

def unpad_bits(bits):
    if len(bits) % 8 != 0:
        return bits
    last_byte = bits[-8:]
    pad_len = int(''.join(map(str, last_byte)), 2)
    return bits[:-pad_len * 8]

def bits_to_bytes(bits):
    return bytes(int(''.join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8))

def bytes_to_bits(byte_data):
    return [int(b) for byte in byte_data for b in format(byte, '08b')]

def encode_base64(bits):
    return base64.b64encode(bits_to_bytes(bits)).decode('ascii')

def decode_base64(b64_string):
    return bytes_to_bits(base64.b64decode(b64_string))

def key_schedule(key_64):
    key = permute(key_64, PC1)
    C, D = split_in_half(key)
    round_keys = []
    for shift in SHIFT:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        round_keys.append(permute(C + D, PC2))
    return round_keys

def s_box_substitution(bits48):
    output = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = (block[0] << 1) + block[5]
        col = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
        val = S[i][row][col]
        output.extend([int(b) for b in format(val, '04b')])
    return output


def feistel(R, K):
    R_expanded = permute(R, E)
    xored = xor(R_expanded, K)
    sbox_output = s_box_substitution(xored)
    return permute(sbox_output, P)


def des_encrypt_block(block64, key64):
    block = permute(block64, IP)
    L, R = split_in_half(block)
    keys = key_schedule(key64)
    for i in range(16):
        L, R = R, xor(L, feistel(R, keys[i]))
    return permute(R + L, FP)

def des_decrypt_block(block64, key64):
    block = permute(block64, IP)
    L, R = split_in_half(block)
    keys = key_schedule(key64)[::-1]
    for i in range(16):
        L, R = R, xor(L, feistel(R, keys[i]))
    return permute(R + L, FP)

def normalize_key(key):
    key_bytes = key.encode('utf-8')[:8].ljust(8, b'\x00')
    return bytes_to_bits(key_bytes)

def des_encrypt_message(message, key):
    bits = pad_bits(str_to_bits(message))
    key_bits = normalize_key(key)
    encrypted = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        encrypted += des_encrypt_block(block, key_bits)
    return encrypted

def des_decrypt_message(bits, key):
    key_bits = normalize_key(key)
    decrypted = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        decrypted += des_decrypt_block(block, key_bits)
    decrypted = unpad_bits(decrypted)
    return bits_to_str(decrypted)

def des_encrypt_bytes(data: bytes, key: str) -> bytes:
    bits = pad_bits(bytes_to_bits(data))
    key_bits = normalize_key(key)
    encrypted = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        encrypted += des_encrypt_block(block, key_bits)
    return bits_to_bytes(encrypted)

def des_decrypt_bytes(data: bytes, key: str) -> bytes:
    bits = bytes_to_bits(data)
    key_bits = normalize_key(key)
    decrypted = []
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        decrypted += des_decrypt_block(block, key_bits)
    decrypted = unpad_bits(decrypted)
    return bits_to_bytes(decrypted)

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            sieve[num * num: limit + 1: num] = [False] * len(sieve[num * num: limit + 1: num])
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def generate_500_digit_odd():

    first_digit = str(random.choice(range(1, 10)))

    middle_digits = ''.join(str(random.choice(range(10))) for _ in range(random.choice(range(100,300))))

    last_digit = str(random.choice([1, 3, 5, 7, 9]))

    number_str = first_digit + middle_digits + last_digit
    return int(number_str)


def check_small_primes(n, small_primes):
    for p in small_primes:
        if n % p == 0:
            return False
    return True


def miller_rabin_test(n, k=20):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(1,n-1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_large_prime():
    small_primes = sieve_of_eratosthenes(1000)

    while True:
        candidate = generate_500_digit_odd()

        if not check_small_primes(candidate, small_primes):
            continue

        if miller_rabin_test(candidate):
            return candidate

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modinv(a, m):
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        raise Exception('Обратного элемента не существует, видимо, модуль - не простое число.')
    return x % m

def generate_rsa_keys(p, q, e):
    #p = generate_large_prime()
    #q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    #e = 65537
    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt_rsa(message, pubkey):
    e, n = pubkey
    m = int.from_bytes(message.encode('utf-8'), 'big')
    c = pow(m, e, n)
    return c

def choose_optimal_e(phi_n, preferred_e=[65537, 257, 17, 5, 3]):
    for e in preferred_e:
        if math.gcd(e, phi_n) == 1:
            return e
    while True:
        e_candidate = random.randint(3, phi_n - 1)
        if math.gcd(e_candidate, phi_n) == 1:
            return e_candidate

def decrypt_rsa(ciphertext, privkey):
    d, n = privkey
    m = pow(ciphertext, d, n)
    length = (m.bit_length() + 7) // 8
    return m.to_bytes(length, 'big').decode('utf-8')

def diffie_hellman(g, p):
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    A = pow(g,a,p)
    B = pow(g,b,p)
    s_alice = pow (B, a, p)
    return A, B, a, b, s_alice

def sign(message, d, n, f):
    dd = message
    if f == 0:
        dd = message.encode()
    hash_msg = int.from_bytes(dd, byteorder='big') % n
    signature = pow(hash_msg, d, n)
    return signature

def verify(message, signature, e, n, f):
    dd = message
    if f == 0:
        dd = message.encode()
    hash_msg = int.from_bytes(dd, byteorder='big') % n
    decrypted_hash = pow(signature, e, n)
    return decrypted_hash == hash_msg