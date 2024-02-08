def findRemoveAdd1(l1, l2):
    if type(l1) is list and type(l2) is list:
        if l1 == [] or l2 ==[]:
            return "Error"
        ans = l1
        count = 0
        for i in range(len(l2)):
            index = 0
            if len(l2[i]) < 2:
                return "Error"
            for ii in range(len(l2[i])):
                index = index + int(l2[i][ii])
            index1 = l2[i][0]
            index2 = l2[i][1]
            if len(l1) < index1:
                return "Error"
            if len(l1[index1]) < index2:
                return "Error"
            text = l1[index1][index2]
            if len(text) > index:
                ans[index1 + count].remove(ans[index1 + count][index2])
                ans = [text.upper()] + ans
                count += 1
            else:
                ans[index1 + count].remove(ans[index1 + count][index2])
                ans = ans + [text]
        return ans
    else:
        return "Error"


if __name__ == "__main__":
    print(findRemoveAdd1([['a'], ['bb', 'ccc'], ['dd', 'e']],
                         [[1, 1], [2, 0]]))
    print(findRemoveAdd1([['easy', 'list'], ['for', 'every', 'one']],
                         [[0,0],[0,1]]))
