
def calculate(list):
    if list is not list:
        return False

    sum = 0
    
    for elem in list:
        if type(elem) is str:
            try:
                sum += int(elem)
            except ValueError:
                pass
    return sum