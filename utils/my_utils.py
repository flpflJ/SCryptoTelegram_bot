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

#def caesarcrypt(message):
#