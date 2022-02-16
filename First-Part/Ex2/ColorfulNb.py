def is_colorfull(nb):
    digits = []
    colors = []

    for digit in str(nb):
        digits.append(int(digit))
    
    for i in digits:
        if i in colors:
            return False
        else:
            colors.append(i)

    for i in range(len(digits) - 1):
        if digits[i] * digits[i + 1] in colors:
            return False
        else:
            colors.append(digits[i] * digits[i + 1])
    
    all_product = 1

    for i in digits:
        all_product *= i
    
    if all_product in colors:
        return False
    return True