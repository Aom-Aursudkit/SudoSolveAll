def AEIOUFront(x):
    if x == str(x):
        cx = len(x)
        ans = ""
        cc = 0
        zero = 0
        zeroc = 0
        for ii in range(cx):
            if x[ii] == "0":
               zero = ii
        if x[cx-1] == "0":
            zero = cx
        for i in range(cx):
            if x[cx - 1] == "0" and i == len(x) - 1:
                ans = ans + str(cx - 1)
            elif i == len(x) - 1 or x[i] == " ":
                ans = ans + x[i]
            elif x[i] == "0" and zeroc == 0:
                ans = ans + str(i)
                zeroc = 1
            elif zero == i and zero != 0:
                ans = ans + str(i)
                zeroc = 0
            elif zeroc == 0:
                if i == len(x) - 1 or x[i] == " ":
                    ans = ans + x[i]
                elif cc == 1:
                    cc = 0
                    pass
                elif x[i + 1] == "a":
                    ans = ans + x[i] + x[i]
                    cc = 1
                elif x[i + 1] == "e":
                    ans = ans + x[i] + x[i]
                    cc = 1
                elif x[i + 1] == "i":
                    ans = ans + x[i] + x[i]
                    cc = 1
                elif x[i + 1] == "o":
                    ans = ans + x[i] + x[i]
                    cc = 1
                elif x[i + 1] == "u" and x[i] != "o":
                    ans = ans + x[i] + x[i]
                    cc = 1
                else:
                    ans = ans + x[i]
            else:
                ans = ans + x[i]
        return ans
    else:
        return "Error"


if __name__ == "__main__":
    print(AEIOUFront("It's out there if you look hard0eenough,0enough,0enough0"))
