def SortProMax(x):
    if type(x) is list:
        ku = []
        ke = []
        charr = []
        waa= []
        for i in range (len(x)):
            if type(x[i]) == int:
                if x[i]%2 == 0:
                    ku += [x[i]]
                else:
                    ke += [x[i]]
            else:
                if x[i].isalpha() == True:
                    charr += [x[i]]
                else:
                    waa += [x[i]]
        ku.sort(reverse=True)
        ke.sort()
        charr.sort()
        ans = []
        o = 0
        oo = 0
        ooo = 0
        oooo = 0
        for ii in range(len(x)):
            if type(x[ii]) == int:
                if x[ii]%2 == 0:
                    ans += [ku[o]]
                    o += 1
                else:
                    ans += [ke[oo]]
                    oo += 1
            else:
                if x[ii].isalpha() == True:
                    ans += [charr[ooo]]
                    ooo += 1
                else:
                    ans += [waa[oooo]]
                    oooo += 1
        return ans
    else:
        return "Error"


if __name__ == "__main__":
    print(SortProMax([3, 4, "b", "H", "#", 6, 5, 9, "a", 1, 4]))
