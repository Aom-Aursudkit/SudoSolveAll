def PaoYingChoob(x, y):
    if x == y:
        if x == 1:
            return "Player:scissor X Computer:scissor --> It is a draw"
        if x == 2:
            return "Player:rock X Computer:rock --> It is a draw"
        if x == 3:
            return "Player:paper X Computer:paper --> It is a draw"
    elif x + y == 3:
        if x > y:
            return "Player:rock X Computer:scissor --> User won"
        else:
            return "Player:scissor X Computer:rock --> User lost"
    elif x + y == 4:
        if x < y:
            return "Player:scissor X Computer:paper --> User won"
        else:
            return "Player:paper X Computer:scissor --> User lost"
    elif x + y == 5:
        if x > y:
            return "Player:paper X Computer:rock --> User won"
        else:
            return "Player:rock X Computer:paper --> User lost"

# def PaoYingChoob(player, computer):
#     scissor = 1
#     hammer = 2
#     paper = 3
#     if player == 1 and computer == 2:
#         return 'Player:scissor X Computer:rock --> User lost'
#     if player == 2 and computer == 3:
#         return 'Player:rock X Computer:paper --> User lost'
#     if player == 1 and computer == 3:
#         return 'Player:scissor X Computer:paper --> User won'
#     if player == 2 and computer == 1:
#         return 'Player:rock X Computer:scissor --> User won'
#     if player == 3 and computer == 2:
#         return 'Player:paper X Computer:rock --> User won'
#     if player == 3 and computer ==1:
#         return 'Player:paper x Computer:scissor --> User lost'
#     if player == 1 and computer ==1:
#         return 'Player:scissor X Computer:scissor --> It is a draw'
#     if player == 2 and computer ==2:
#         return 'Player:rock X Computer:rock --> It is a draw'
#     if player == 3 and computer ==3:
#         return 'Player:paper X Computer:paper --> It is a draw'


if __name__ == '__main__':
    print(PaoYingChoob(1,3))