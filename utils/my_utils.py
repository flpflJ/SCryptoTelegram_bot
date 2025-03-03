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