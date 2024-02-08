def Example(x):
    if x == str(x):
        return "Error"
    elif x > 0:
        lastd = pow(x, 2)
        front = str()
        for i in range(1, int(x)):
            front = front + str(i)
        alll = front + str(lastd)
        return alll
    else:
        return "Error"


if __name__ == "__main__":
    print(Example(4))
