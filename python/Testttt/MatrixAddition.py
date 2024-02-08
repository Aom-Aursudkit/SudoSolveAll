def MatrixAddition(x, y):
    if type(x) is list and type(y) is list:
        ans = [[0 for i in range(len(y[0]))] for ii in range(len(y))]
        for ii in range(len(x)):
            for jj in range(len(x[0])):
                temp = x[ii][jj]
                if type(temp) != int:
                    return "Error"
                if type(temp) == float:
                    return "Error"
        for ii in range(len(y)):
            for jj in range(len(y[0])):
                temp = y[ii][jj]
                if type(temp) != int:
                    return "Error"
                if type(temp) == float:
                    return "Error"
        if len(x) == len(y) and len(x[0]) == len(y[0]):
            for i in range(len(x)):
                for j in range(len(x[0])):
                    ans[i][j] = x[i][j] + y[i][j]
            return ans
        else:
            xx = [[x[a][b] for a in range(len(x))] for b in range(len(x[0]))]
            if len(xx) != len(y):
                return "Error"
            for i in range(len(xx)):
                if len(xx[i]) != len(y[i]):
                    return "Error"
            for i1 in range(len(y)):
                for j1 in range(len(y[0])):
                    ans[i1][j1] = xx[i1][j1] + y[i1][j1]
            return ans

    else:
        return "Error"


if __name__ == "__main__":
    print(MatrixAddition([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(MatrixAddition([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]))
# m = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for row in m:
# 	print(row)
# print(m)
# rez = [[m[x][y] for x in range(len(m))] for y in range(len(m[0]))]
# print("\n")
# for row in rez:
# 	print(row)
# print(rez)
