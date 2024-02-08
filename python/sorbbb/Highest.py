def Highest(l):
    if type(l) is list:
        ans = []
        for y in range(len(l)):
            for x in range(len(l[y])):
                yy = len(l) - 1 - y
                if type(l[y][x]) != int:
                    return "Error"
                if y == 0:
                    if x == 0:
                        if l[yy][x] > l[yy][x + 1] and l[yy][x] > l[yy - 1][x]:
                            ans += [[0, 0]]
                    elif len(l[y]) - 1 - x == 0:
                        if l[yy][x] > l[yy][x - 1] and l[yy][x] > l[yy - 1][x]:
                            ans += [[0, x]]
                    else:
                        if l[yy][x] > l[yy][x + 1] and l[yy][x] > l[yy][x - 1] and l[yy][x] > l[yy - 1][x]:
                            ans += [[0, x]]
                if yy == 0:
                    if x == 0:
                        if l[yy][x] > l[yy][x + 1] and l[yy][x] > l[yy + 1][x]:
                            ans += [[y, 0]]
                    elif len(l[y]) - 1 - x == 0:
                        if l[yy][x] > l[yy][x - 1] and l[yy][x] > l[yy + 1][x]:
                            ans += [[y, x]]
                    else:
                        if l[yy][x] > l[yy][x + 1] and l[yy][x] > l[yy][x - 1] and l[yy][x] > l[yy + 1][x]:
                            ans += [[y, x]]
                elif x == 0and yy != 0:
                    if l[yy][x] > l[yy][x + 1]  and l[yy][x] > l[yy - 1][x]:
                        ans += [[y, 0]]
                elif len(l[y]) - 1 - x == 0and yy != 0:
                    if l[yy][x] > l[yy][x - 1]  and l[yy][x] > l[yy - 1][x]:
                        ans += [[y, x]]
                else:
                    if l[yy][x] > l[yy][x + 1] and l[yy][x] > l[yy][x - 1]  and l[yy][x] > l[yy - 1][x]:
                        ans += [[y, x]]
        if ans == []:
            return "Not found"
        return ans
    else:
        return "Error"


if __name__ == "__main__":
    print(Highest([[0, 6, 3, 11, 12],
                   [9, 5, 12, 9, 3],
                   [4, 6, 8, 10, 0]]))
    print(Highest([[1, 2, 1],
                   [1, 2, 1],
                   [1, 2, 1]]))
    print(Highest([[0, 6, 3, 11, 12],
                   [9, 5, 12, "M", 3],
                   [4, 6, 8, 10, 0],
                   [1, 2, 3, 4, 5]]))
