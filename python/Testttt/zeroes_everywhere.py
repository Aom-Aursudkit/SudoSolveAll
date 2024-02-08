def zeroes_everywhere(n):
    # for i in range(1,n+1):
    #     ans = 1
    #     for i1 in range(i):
    #         ans = ans * (i1+1)
    #     print(i,ans)
    ######################################
    # nn = 1
    # for i in range(n):
    #     nn = nn * (i+1)
    # x = str(nn)
    # ans = 0
    # for i in range(len(x)):
    #     if x[len(x)-1-i] == "0":
    #         ans +=1
    #     else:
    #         break
    ######################################
    ans = 0
    for i in range(1, n + 1):
        if int(n / (5 ** i)) == 0:
            break
        ans = ans + int(n / (5 ** i))
    return ans


print(zeroes_everywhere(30))
