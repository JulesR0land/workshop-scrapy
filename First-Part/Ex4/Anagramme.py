
def is_anagramme(str1, str2):
    sorted1 = list(str1)
    sorted1.sort()
    sorted2 = list(str2)
    sorted2.sort()

    if sorted1 == sorted2:
        return True
    return False

def anagramme(str, list):
    anagrammes = []

    for elem in list:
        if is_anagramme(str, elem):
            anagrammes.append(elem)
    
    return anagrammes