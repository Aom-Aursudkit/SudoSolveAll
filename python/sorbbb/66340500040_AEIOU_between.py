def AEIOU_between(x):
    if type(x) is str:
        countx =len(x)
        ans = ""
        endd = 0
        stopp = 0
        if x.count("*") > 1:
            for i1 in range(countx):
                if x[i1] == "*":
                    endd = i1
        for i in range(countx):
            if endd != 0 and endd == i:
                ans = ans + x[i]
                stopp = 0
            elif x[i] == "*" and stopp == 0:
                ans = ans + x[i]
                stopp = 1
            elif stopp == 1:
                if x[i] == "a" or x[i] == "e" or x[i] == "i" or x[i] == "o" or x[i] == "u":
                    if x[i-1] == "a" or x[i-1] == "e" or x[i-1] == "i" or x[i-1] == "o" or x[i-1] == "u" or x[i-1] == "*" or x[i-1] == " ":
                        ans = ans + x[i]
                    else:
                        ans = ans + x[i-1]
                elif x[i] == "*":
                    ans = ans + str(i)
                else:
                    ans = ans + x[i]
            else:
                ans = ans + x[i].swapcase()
        return ans
    else:
        return "Error"




if __name__ == "__main__":
    print(AEIOU_between("Fly me to the* moon Let *me p*lay among*the stars"))