def rotor(symbol, n, shift, reverse=False):
    """Функция шифрования символа с помощью ротора, где:
        1) symbol - символ, поступающий для шифрования
        2) n - номер ротора
        3) reverse - признак обратного направления, если находится в значении True,
    символ шифруется в обратном направлении (по умолчанию False)."""
    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
              }
    if reverse:
        symbol = ROTORS[0][(ROTORS[0].index(symbol) + shift) % 26]
        ind = (ROTORS[n].index(symbol) - shift) % 26
        return ROTORS[0][ind]
    else:
        ind = (ROTORS[0].index(symbol) + shift) % 26
        symb = ROTORS[n][ind]
        return ROTORS[0][(ROTORS[0].index(symb) - shift) % 26]


def reflector(symbol, n, shift):
    """Функция шифрования символа с помощью отражателя (имеет только одно направление)."""
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',  # reflector B
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',  # reflector C
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',  # reflector B Dünn
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',  # reflector C Dünn
                  }
    ind = (REFLECTORS[0].index(symbol) - shift) % 26
    return REFLECTORS[n][(ind + shift) % 26]


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    """Функция реализует энигму, где:
        1) text - исходный текст, который необходимо зашифровать
        2) ref - номер отражателя
        3) rot1, rot2, rot3 - номера роторов
        4) shift1, shift2, shift3 - сдвиги роторов (1, 2 и 3, соответственно)
        5) строка замен символов
    Сигнал распространяется по машине справа налево (и после отражения обратно)."""
    plugboard = {}  # словарь замены символов с помощью коммутационной панели
    if pairs:
        for f, s in pairs.upper().split():
            if f in plugboard and (plugboard.get(f) != s and plugboard.get(s) != f) or \
                    s in plugboard and (plugboard.get(s) != f and plugboard.get(f) != s):
                return 'Извините, невозможно произвести коммутацию'
            else:
                plugboard[f] = s
                plugboard[s] = f

    def rotor_shift(shift1, rot2, shift2, rot3, shift3):
        """Функция пересчитывает сдвиг роторов после каждого нажатия символа."""
        shifts = {1: (16,), 2: (4,), 3: (21,), 4: (9,), 5: (25,), 6: (25, 12), 7: (25, 12), 8: (25, 12)}
        if shift2 in shifts[rot2]:
            shift2 = (shift2 + 1) % 26
            shift1 = (shift1 + 1) % 26
        elif shift3 in shifts[rot3]:
            shift2 = (shift2 + 1) % 26
        shift3 = (shift3 + 1) % 26
        return shift1, shift2, shift3

    res = ''
    for symb in text.upper():
        if symb not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            continue
        if symb in plugboard:
            symb = plugboard[symb]
        shift1, shift2, shift3 = rotor_shift(shift1, rot2, shift2, rot3, shift3)
        symb = rotor(symb, rot3, shift3, False)
        symb = rotor(symb, rot2, shift2, False)
        symb = rotor(symb, rot1, shift1, False)
        symb = reflector(symb, ref, shift1)
        symb = rotor(symb, rot1, shift1, True)
        symb = rotor(symb, rot2, shift2, True)
        symb = rotor(symb, rot3, shift3, True)
        if symb in plugboard:
            symb = plugboard[symb]
        res += symb
    return res


print(enigma('A', 1, 1, 0, 2, 0, 3, 0, ''))  # B
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'))  # Q
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'))  # D
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'))  # Извините, невозможно произвести коммутацию
print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'))  # Извините, невозможно произвести коммутацию
print(enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0))  # BDZGOWC
