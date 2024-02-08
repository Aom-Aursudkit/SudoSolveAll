def weird_series(x):
    ans = []
    if x <= 11:
        for i in range(x):
            ans.append(i)
    else:
        for i in range(11):
            ans.append(i)
        for ii in range(11,x):
            count = 0
            while(True):
                same = 0
                before = str(ans[ii-1])
                countt = str(count)
                for i1 in range(len(ans)):
                    if count == ans[i1]:
                        same = 1
                if same == 0:
                    for i2 in range(len(countt)):
                        for i3 in range(len(before)):
                            if countt[i2] == before[i3]:
                                same = 1
                if same == 0:
                    ans.append(count)
                    break
                count += 1
    return ans

print(weird_series(12))