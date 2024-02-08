def WorldLine(x):
    xx = x[0][0][0] - x[0][1][0]
    yy = x[0][0][1] - x[0][1][1]
    for i in range(len(x)):
        if xx != x[i][0][0] - x[i][1][0] or yy != x[i][0][1] - x[i][1][1]:
            return "False"
        xx = x[i][0][0] - x[i][1][0]
        yy = x[i][0][1] - x[i][1][1]
        # print(xx,yy)
    return "True"
if __name__ == "__main__":
    print(WorldLine([ [[0,1],[2,1]],
                      [[1,2],[3,2]],
                      [[2,3],[5,3]]]))