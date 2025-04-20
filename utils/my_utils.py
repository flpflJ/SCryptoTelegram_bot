import base64
import re

import numpy as np
from ascii_graph import Pyasciigraph
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
    max_ic = -1
    best_key_en = 0
    best_key_ru = 0
    rd,ed,smbcnt=symbol_count(text)
    edd = dict()
    kd = dict()
    ra = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    char_to_ind = {char: i for i, char in enumerate(ra)}
    for k in range(len(ra)):
        cur_ic = 0.0
        for char, freq in rd.items():
            if char not in char_to_ind:
                continue
            cipher_idx = char_to_ind[char]
            original_idx = (cipher_idx - k) % len(ra)
            original_char = ra[original_idx]

            cur_ic += freq * reference_prob_ru.get(original_char)
        if cur_ic > max_ic:
            max_ic = cur_ic
            best_key_ru = k
    for i in ra:
        kd[i]=ra[char_to_ind[i]-best_key_ru % len(ra)]
    rae = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_ic = -1
    char_to_ind = {char: i for i, char in enumerate(rae)}
    for k in range(len(rae)):
        cur_ic = 0.0
        for char, freq in ed.items():
            if char not in char_to_ind:
                continue
            cipher_idx = char_to_ind[char]
            original_idx = (cipher_idx - k) % len(rae)
            original_char = rae[original_idx]

            cur_ic += freq * reference_prob_en.get(original_char)
        if cur_ic > max_ic:
            max_ic = cur_ic
            best_key_en = k
    for i in rae:
        edd[i]=rae[char_to_ind[i]-best_key_en % len(rae)]
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

def rand_gen(length : int, seed : int =1,a : int = 1002378,c : int = 101393193,m : int = 22167236):
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
        res.append(Xn)
        Xn = LCG(Xn, a, c, m)
    gamma = bytearray()
    for num in res:
        if num > 4294967295:
            num = num % 4294967295
        gamma.extend(num.to_bytes(4, byteorder='little'))
    return gamma[:length]

def gamma(text,key):
    return bytes([a^b for a,b in zip(text,key)])
#def gamma(text,key):
#    return bytes(np.bitwise_xor(np.frombuffer(text), key))

