ROMAN_VALUES = {"I": 1, "V": 5, "X": 10}


def getDecimal(rom: str) -> int:
    return ROMAN_VALUES.get(rom.upper(), -1)


def convRoman(token: str) -> int:
    clean = "".join(ch for ch in token.upper() if ch in ROMAN_VALUES)
    dec = 0
    i = 0
    
    while i < len(clean):
        d1 = getDecimal(clean[i])
        if i + 1 < len(clean):
            d2 = getDecimal(clean[i + 1])
            if d1 >= d2:
                dec += d1
                i += 1
            else:
                dec += d2 - d1
                i += 2
        else:
            dec += d1
            i += 1
    return dec