def Mountain(x):
    if type(x) is int:
        ans = ""
        if x <= 0:
            return "Error"
        if x == 1:
            return "2"
        for i3 in range(x-1):
            for i in range(1,(x-i3)+1): #ขาขึ้น
                ans = ans + str(i*2)
            for i1 in range((x-i3)-1): #ข้างบน
                ans = ans + str((x-i3)*2)
            for i2 in range((x-i3)): #ขาลง
                ans = ans + str(((x-i3)-i2)*2)
        return ans
    else:
        return "Error"

if __name__ == "__main__":
    print(Mountain(4))
