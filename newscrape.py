from newsearch import University


def searchFull(name):
    UA = University(957)
    full = UA.searching(name)
    if "Error" in full:
        return "error"
    listU = []
    for values in full.values():
        listU.append(values)

    return listU

def nss(name):
    names = []
    Ualbany = University(957)
    names = Ualbany.searching(name)
    if("error" in names):
        return "error"
    one = combo(names)
    return one

def combo(names):
    total = ""
    for i in range(len(names)):
        total += names[i] +"\n"
    return total

#print(nss("Morgan"))