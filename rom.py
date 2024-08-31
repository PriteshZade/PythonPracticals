rom_dict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def rom(text, text_base):
    k = int(text, text_base)  
    roman_ans = []

    for value in rom_dict.keys():
        while k >= value:
            roman_ans.append(rom_dict[value])
            k -= value
    
    return ''.join(roman_ans)


print(rom("198", 10))  
