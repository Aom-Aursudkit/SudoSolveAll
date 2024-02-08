def Onepiece(x):
    if type(x) is str:
        countx = len(x)
        xx = x.lower()
        search = 0
        ans = ""
        space = 0
        for i in range(countx):
            if xx[i] == "l" and search == 0:
                for i1 in range(i, countx):
                    if xx[i1] == " ":
                        space = 1
                        break
                    if xx[i1] != "l" and xx[i1] != "u" and xx[i1] != "f" and xx[i1] != "y":
                        noo = 1
                        break
                    else:
                        noo = 0
                if space == 1:
                    ans = ans + " "
                    space = 0
                if noo == 0:
                    ans = ans + "Lufy"
                i = i1
        return ans

    else:
        return "Error"


if __name__ == "__main__":
    print(Onepiece("lufffffy lufyyy"))
