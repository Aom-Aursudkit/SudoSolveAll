def Clouds(x):
    y = x.split("not")
    tf = 0
    if y[0] == '':
        y.remove('')
        tf = 1
    # print(y)
    name = ""
    for i in range(len(y)):
        if y[i] != '':
            for i1 in range(i+1,len(y)):
                if y[i1] != '':
                    if y[i] != len(y)-1:
                        tf += 1
                    break
                else:
                    tf += 1
            # print(tf)
            if tf%2 == 0:
                name = name + str(y[i])
                tf = 0
            else:
                tf = 0
    if name == "nimbostratus" or name == "cumulonimbus":
        r = "Rain"
    else:
        r = "Not Rain"
    ans = [name,r]
    return ans

if __name__ == "__main__":
    print(Clouds('notnimbonotstratus'))
    print(Clouds('nimbonotnotnotstratus'))