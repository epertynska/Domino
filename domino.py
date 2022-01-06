import random

dominoes = []
computer = []
player = []
start = []
domsnake = []
moves = []

# generating basic domino deck (stock)
i = 0
j = 0
for i in range(7):
    for j in range(7):
        dominoes.append([i, j])

for d in dominoes:
    dr = d[::-1]
    if d[0] == dr[1] and d[1] == dr[0] and d[0] != d[1]:
        dominoes.remove(dr)

# shuffling dominoes
random.shuffle(dominoes)
computer = random.sample(dominoes, 7)
for i in computer:
    if i in dominoes:
        dominoes.remove(i)
player = random.sample(dominoes, 7)
for i in player:
    if i in dominoes:
        dominoes.remove(i)

# checking if there is any "even" domino and if so, finding the highest
for x in player:
    if x[0] == x[1]:
        start.append(x)
for y in computer:
    if y[0] == y[1]:
        start.append(y)
if len(start) == 1:
    for s in start:
        if s in computer:
            computer.remove(s)
            domsnake.append(s)
            who = "player"
        elif s in player:
            player.remove(s)
            domsnake.append(s)
            who = "computer"
elif len(start) == 0:
    random.shuffle(dominoes)
    computer = random.sample(dominoes, 7)
    for i in computer:
        if i in dominoes:
            dominoes.remove(i)
    player = random.sample(dominoes, 7)
    for i in player:
        if i in dominoes:
            dominoes.remove(i)
else:
    control = [sum(s) for s in start]
    highest_index = control.index(max(control))
    x = start[highest_index]
    if x in computer:
        computer.remove(x)
        domsnake.append(x)
        who = "player"
    elif x in player:
        player.remove(x)
        domsnake.append(x)
        who = "computer"

def educated():
    global domsnake
    global computer
    global moves
    count_list = []
    for c in computer:
        for i in c:
            count_list.append(i)
    for s in domsnake:
        for i in s:
            count_list.append(i)
    c_0 = count_list.count(0)
    c_1 = count_list.count(1)
    c_2 = count_list.count(2)
    c_3 = count_list.count(3)
    c_4 = count_list.count(4)
    c_5 = count_list.count(5)
    c_6 = count_list.count(6)
    num_vals = {0: c_0, 1: c_1, 2: c_2, 3: c_3, 4: c_4, 5: c_5, 6: c_6}
    value_check = []
    val = []
    for _ in computer:
        for i in _:
            if i in num_vals:
                a = num_vals[i]
                value_check.append(a)
    j = 0
    k = 1
    while k < len(value_check):
        v = value_check[j] + value_check[k]
        val.append(v)
        j += 2
        k += 2
    moves = []
    for v in val:
        best = val.index(max(val))
        move = best + 1
        moves.append(move)
        moves.append(-move)
        val[best] = -1
    moves.append(0)

while True:
    print("=" * 70)
    print("Stock pieces: {}".format(len(dominoes)))
    print("Computer pieces: {}".format(len(computer)))
    print()
    snake = ""
    for s in domsnake:
        s = str(s)
        if len(domsnake) > 6:
            domsnake[3:-3] = "..."
            snake += s
        else:
            snake += s
    print(snake)
    print()
    print("Your pieces:")
    i = 1
    while i <= len(player):
        print("{}:{}".format(i, player[i - 1]))
        i += 1
    print()
    if len(player) == 0 and len(computer) != 0:
        print("Status: The game is over. You won!")
        break
    elif len(player) != 0 and len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(player) != 0 and len(computer) != 0:
        if who == "player":
            print("Status: It's your turn to make a move. Enter your command.")
            length = len(player)
            double_l = length * 2
            minus_length = length - double_l
            while True:
                move = input()
                try:
                    move = int(move)
                except:
                    print("Invalid input. Please try again.")
                else:
                    if minus_length <= move <= length:
                        if move > 0:
                            # check if it is legal move
                            domino = player[move - 1]
                            if domino[0] == domsnake[-1][1]:
                                player.remove(domino)
                                domsnake.append(domino)
                                who = "computer"
                                break
                            elif domino[1] == domsnake[-1][1]:
                                player.remove(domino)
                                domino = domino[::-1]
                                domsnake.append(domino)
                                who = "computer"
                                break
                            elif domino[0] != domsnake[-1][1] or domino[1] !=domsnake[-1][1]:
                                print("Illegal move. Please try again.")
                        elif minus_length <= move < 0:
                            move = abs(move)
                            domino = player[move - 1]
                            if domino[1] == domsnake[0][0]:
                                player.remove(domino)
                                domsnake.insert(0, domino)
                                who = "computer"
                                break
                            elif domino[0] == domsnake[0][0]:
                                player.remove(domino)
                                domino = domino[::-1]
                                domsnake.insert(0, domino)
                                who = "computer"
                                break
                            elif domino[0] != domsnake[0][0] or domino[1] !=domsnake[0][0]:
                                print("Illegal move. Please try again.")
                        elif move == 0:
                            if len(dominoes) > 0:
                                added = random.choice(dominoes)
                                player.append(added)
                                dominoes.remove(added)
                                who = "computer"
                                break
                            elif len(dominoes) == 0:
                                computer = []
                                who = "computer"
                                break
                    elif minus_length > move or move > length:
                        print("Invalid input. Please try again.")
                continue
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            length = len(computer)
            double_l = length * 2
            minus_length = length - double_l
            educated()
            i = 0
            while True:
                move = moves[i]
                if minus_length <= move <= length:
                    if move > 0:
                        # check if it is legal move
                        domino = computer[move - 1]
                        if domino[0] == domsnake[-1][1]:
                            computer.remove(domino)
                            domsnake.append(domino)
                            who = "player"
                            input()
                            break
                        elif domino[1] == domsnake[-1][1]:
                            computer.remove(domino)
                            domino = domino[::-1]
                            domsnake.append(domino)
                            who = "player"
                            input()
                            break
                        i += 1
                    elif minus_length <= move < 0:
                        move = abs(move)
                        domino = computer[move - 1]
                        if domino[1] == domsnake[0][0]:
                            computer.remove(domino)
                            domsnake.insert(0, domino)
                            who = "player"
                            input()
                            break
                        elif domino[0] == domsnake[0][0]:
                            computer.remove(domino)
                            domino = domino[::-1]
                            domsnake.insert(0, domino)
                            who = "player"
                            input()
                            break
                        i += 1
                    elif move == 0:
                        if len(dominoes) > 0:
                            added = random.choice(dominoes)
                            computer.append(added)
                            dominoes.remove(added)
                            who = "player"
                            input()
                            break
                        elif len(dominoes) == 0:
                            player = []
                            who = "player"
                            input()
                            break
                continue
    elif len(player) != 0 and len(computer) != 0 and len(dominoes) == 0:
        print("Status: The game is over. It's a draw!")
        break
    continue
