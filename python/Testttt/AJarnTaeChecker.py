def AJarnTaeChecker(nano,ans,point):
    if type(nano) is list and type(ans) is list and type(point) is list:
        final = []
        match = []
        cpoint = []
        fpoint = 0
        if len(nano) != len(ans):
            return "Plagiarism"
        for i in range(len(nano)):
            if type(nano[i]) != type(ans[i]):
                return "Plagiarism"
            if type(nano[i]) == int:
                if nano[i] > 5 or nano[i] < 1:
                    return "F"
                if nano[i] == ans[i]:
                    match = match + [i+1]
                    cpoint = cpoint + [point[i]]
                    fpoint = fpoint + point[i]
            if type(nano[i]) == str:
                tempnano = nano[i]
                tempans = ans[i]
                x = 0
                if len(tempnano) == len(tempans):
                    for ii in range(len(tempans)):
                        if tempnano[ii] == tempans[ii]:
                            x += 1
                    if (x / len(tempans)) * 100 >= 80:
                        match = match + [i + 1]
                        cpoint = cpoint + [point[i]]
                        fpoint = fpoint + point[i]
        final = [match] + [cpoint] + [fpoint]
        return final
    else:
        return "Error"

if __name__ == "__main__":
    print(AJarnTaeChecker([1, 2, 1, 3, 2, 4, 1, 2, 4, 2, 3, 4, 5, 2, 4, 'abc', 'elephant', 'giraffe', 'computer', 'A'],
                          [1, 3, 2, 3, 5, 4, 4, 1, 4, 2, 3, 4, 2, 1, 4, 'abd', 'elehant', 'giraffe', 'computel', 'AB'],
                          [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
    print(AJarnTaeChecker([1, 2, 1, 3, 2, 4, 1, 2, 4, 2, 3, 4, 5, 2, 'abc', 4, 'elephant', 'giraffe', 'computer', 'A'],
                          [1, 3, 2, 3, 5, 4, 4, 1, 4, 2, 3, 4, 2, 1, 4, 'abd', 'elehant', 'giraffe', 'computel', 'AB'],
                          [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
    print(AJarnTaeChecker([1, 2, 1, 3, 2, 4, 1, 2, 4, 2, 3, 4, 5, 2, 4, 'abc', 'elephant', 'giraffe', 'computer'],
                          [1, 3, 2, 3, 5, 4, 4, 1, 4, 2, 3, 4, 2, 1, 4, 'abd', 'elehant', 'giraffe', 'computel', 'AB'],
                          [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
    print(AJarnTaeChecker([8, 2, 1, 3, 2, 4, 1, 2, 4, 2, 3, 4, 5, 2, 4, 'abc', 'elephant', 'giraffe', 'computer', 'A'],
                          [1, 3, 2, 3, 5, 4, 4, 1, 4, 2, 3, 4, 2, 1, 4, 'abd', 'elehant', 'giraffe', 'computel', 'AB'],
                          [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))