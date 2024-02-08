def find_match(x,y):
    count9 = ""
    count1 = "1"
    for i in range(y):
        count9 += "9"
    for i in range(y-1):
        count1 += "0"
    count9 = int(count9)
    count1 = int(count1)
    num = []
    for i in range(count1,count9+1):
        check = str(i)
        checkk = 0
        order = 1
        for i2 in range(1,len(check)):
            if int(check[i2]) < int(check[i2-1]):
                order = 0
        if order == 1:
            for i1 in range(len(check)):
                checkk += int(check[i1])
            if checkk == x:
                num.append(i)
    print(num)
    if num == []:
        return num
    ans = [len(num),num[0],num[len(num)-1]]
    return ans

print(find_match(10,3))
print(find_match(27, 3))