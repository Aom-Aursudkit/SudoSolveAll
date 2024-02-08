def Chayen(e, s):
    if type(e) is list and type(s) is list:
        count = 0
        cc = 0
        while 1:
            eans = e[1][count]
            ebi = e[0][cc]
            if eans[0] == ebi[0]:
                e[0] += [ebi]
                count += 1
                cc += 1
            else:
                e[1] += [eans]
                e[0] += [ebi]
                count += 1
            print(eans, ebi)
            if count + 1 >= len(e[1]):
                break


        count2 = 0
        cc2 = 0
        while 1:
            sans = s[1][count2]
            sbi = s[0][cc2]
            if sans[0] == sbi[0]:
                s[0] += [sbi]
                count2 += 1
                cc2 += 1
            else:
                s[1] += [sans]
                s[0] += [sbi]
                count2 += 1
            if count2 + 1 >= len(s[1]):
                break

        person = ""
        turn = 0
        if count == count2:
            return "Error"
        if count < count2:
            person = "Eve"
            turn = count + 1
        if count > count2:
            person = "Sun"
            turn = count2 + 1
        ans = person + " win with " + str(turn) + " turn"
        return ans

    else:
        return "Error"


if __name__ == "__main__":
    print(Chayen([['Travel', 'Food'], ['Temple', 'French Fried', 'Theater']],
                 [['Animal', 'Food'], ['Ant', 'French Fried', 'Fudge', 'Alpaca']]))
    print(Chayen([['Animal', 'Travel', 'Food'], ['Ant', 'Temple', 'French Fried', 'Theater']],
                 [['Animal', 'Food', 'Travel'], ['Ant', 'Temple', 'French Fried', 'Theater']]))
