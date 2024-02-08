def Palindrome(x):
    if type(x) is str:
        x = x.lower()
        xx = ""
        cc = len(x)
        for i2 in range(cc):
            if x[i2] == " ":
                pass
            else:
                xx = xx + x[i2]
        cx = len(xx)
        if cx <= 7:
            return 0
        cx = cx - 7
        ans = 0
        for i in range(cx):
            palin = ""
            for i1 in range(4):
                palin = palin + xx[i+3-i1]
            if palin[0] == palin[1] and palin[1] == palin[2] and palin[2] == palin[3]:
                pass
            elif xx.find(palin,i+1) >= 0:
                ans = ans + 1
        return ans

    else:
        return "Error"

if __name__ == "__main__":
    print(Palindrome("eeeeeeee"))