def LCP(small , big):
    i = 0
    s = ""
    while i < len(small):
        if small[i] == big[i]:
            s = s + small[i]
        else:
            return s
        i = i + 1
    return s




def sol(list):
    if len(list) == 0:
        return ""
    if len(list) == 1:
        return list[0]
    for i in range(len(list)):
        if list[i] == "":
            return ""



    if len(list[0]) < len(list[1]):
        prefix = LCP(list[0], list[1])

    else:
        prefix = LCP(list[1], list[0])

    if len(list) == 2:
        return prefix
    for i in list:
        if prefix == "":
            return ""
        if len(i) < len(prefix):
            prefix = LCP(i, prefix)
        else:
            prefix = LCP(prefix, i)

    return prefix
