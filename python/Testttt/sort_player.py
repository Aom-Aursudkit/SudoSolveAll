def sort_player(x):
    ans = []
    price = []
    for i in range(len(x)):
        price.append(x[i][2])
    price.sort()
    # for i in range(len(x)):
    #     for i in range(len(x)):


print(sort_player([["Onayna",21 , 200,3],["Prannado",20 , 500,4],["Gotjita",15 , 99999,4],["RonaldoR9",50 ,1,0],["Toonez",1 , 20,2],["Pi vanDijk",99 , 100,4]]))