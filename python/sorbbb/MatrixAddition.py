def MatrixAddition(x,y):
    if type(x) is list and type(y) is list:
        ans = x + y
        return ans
    else:
        return "Error"

if __name__ == "__main__":
    print(MatrixAddition([1,2,3],[1,2,3]))