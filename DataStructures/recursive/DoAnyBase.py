def do_any_base(num: int, base: int):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    if base > num:
        return digits[num]
    else:
        return str(do_any_base(num//base, base)) + str(digits[num % base])

print(do_any_base(15*16**3 + 15*16**2 + 15 * 16 + 15,8))