import string


def ReadResearch(x,first,last,key):
    global iii
    if x == str(x) and first == str(first) and last == str(last) and key == str(key):
        countx = len(x)
        countkey = len(key)
        xx = x.lower()
        first = first.lower()
        last = last.lower()
        key = key.lower()
        endd = 0
        ans = ""
        lastt = 0
        for iiii in range (countx):
            if x[iiii] == last or xx[iiii] == last:
                lastt = iiii
        if last == "":
            lastt = countx-1
        if first == "":
            return "Error"
        if key == "":
            return "Error"
        for i in range (countx):
            if endd == 1:
                break
            if x[i] == first or xx[i] == first:
                for ii in range (i,countx):
                    if lastt != 0 and lastt == ii:
                        endd = 1
                        break
                    # elif x[ii] == key or xx[ii] == key:
                    #     ans = ans + str(ii)
                    else:
                        for iii in range (countkey):
                            if x[ii] == key[iii] or xx[ii] == key[iii]:
                                ans = ans + str(ii)
                            else:
                                pass
        for iii in range(countkey):
            if x[lastt] == key[iii] or xx[lastt] == key[iii]:
                ans = ans + str(lastt)
            else:
                pass
        if lastt == countx-1:
            for iii in range(countkey):
                if x[countx-1] == key[iii] or xx[countx-1] == key[iii]:
                    ans = ans + str(countx-1)
                else:
                    pass
        return ans
    else:
        return "Error"



if __name__ == "__main__":
    print(ReadResearch("Pree tae tum jod kor nee kub","e", "k", "oaer"))