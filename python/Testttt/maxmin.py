def maxmin(x):
    x = str(x)
    # print(x)
    max = int(x[0])
    min = int(x[0])
    for i in range(len(x)):
        if int(x[i]) > max:
            max = int(x[i])
        if int(x[i]) < min and int(x[i]) != 0:
            min = int(x[i])
        if int(x[i]) == 0:
            zero = 1
    # print(max,min)
    ansmax = x
    ansmin = x
    if int(x[0]) != max:
        ansmax = ansmax.replace(str(max),x[0])
        ansmax = ansmax[1:]
        ansmax = str(max)+ansmax
    if x[0] == str(min) and zero == 1:
        ansmin = ansmin.replace("0",x[1])
        ansmin = ansmin[2:]
        ansmin = str(min)+"0"+ansmin
    elif int(x[0]) != min:
        ansmin = ansmin.replace(str(min),x[0])
        ansmin = ansmin[1:]
        ansmin = str(min)+ansmin
    # ans = [int(ansmax),int(ansmin)]
    return "("+ansmax+", "+ansmin+")"
    # return ans

    



print(maxmin(9876543210))
print(maxmin(1234567890))