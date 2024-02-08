def AJarnTaeChecker(nano, ans, point):
    if len(nano) != len(ans):
        return "Plagiarism"
    count = 0
    x = []
    y = []
    for i in range(len(nano)):
        if type(nano[i]) != type(ans[i]):
            return "Plagiarism"
        if type(nano[i]) is int:
            if nano[i] > 5 or nano[i] < 1:
                return "F"
            if nano[i] == ans[i]:
                count = count + point[i]
                x = x + [i]
                y = y + [point[i]]
        if type(nano[i]) is str:
            if nano[i] == ans[i]:
                count = count + point[i]
                x = x + [i]
                y = y + [point[i]]
    kanan = x,y,count
    return kanan

if __name__ == "__main__":
    print(AJarnTaeChecker([1, 2, 1, 3, 2, 4, 1, 2, 4, 2, 3, 4, 5, 2, 4, 'abc', 'elephant', 'giraffe', 'computer', 'A'],
                          [1, 3, 2, 3, 5, 4, 4, 1, 4, 2, 3, 4, 2, 1, 4, 'abd', 'elehant', 'giraffe', 'computel', 'AB'],
                          [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
