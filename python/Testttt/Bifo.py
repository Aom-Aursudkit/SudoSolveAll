def Bifo(x,y,member):
    summ = x + y
    if summ >= 3000:
        summ = summ - 500
    elif member == 1:
        if summ >= 1000:
            summ = summ - 80
        elif summ >= 500:
            summ = summ - 30
    return summ

if __name__ == '__main__':
    print (Bifo(100,3000,0))

