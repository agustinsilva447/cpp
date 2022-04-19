def isLongPressedName(name, typed):
    i = 0
    j = 0
    if name[0] != typed[0]:
        return False
    while j<len(typed):
        print(i, len(name), j, len(typed))
        if i<len(name):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        else:
            if typed[j-1] == typed[j]:
                j += 1
            else:
                return False                    
    return True

a = isLongPressedName("ale", "alexd")
print(a)
