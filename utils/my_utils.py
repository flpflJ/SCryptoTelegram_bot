import re
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

def gronsfield_cipher(message,key: str,flag):
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
            message_formatted[i] = (int(message_formatted[i]) - int(len_key[i])) % len(alph)
            res += alph[message_formatted[i]]
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
    for k in text:
        if len(strk) == 0:
            strk += k
            if k == text[-1]:
                mas.append(k + '~')
        else:
            if(strk[0] == k):
                strk += '~'
                mas.append(strk)
                strk = k
            else:
                strk+= k
                mas.append(strk)
                strk = ""
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
    bigrams = split_bigrams(message)
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
        return res.replace('~','')