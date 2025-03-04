game_running = True
while game_running:        
    print('Naughts and Crosses')
    # board with nums
    board = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    # show board
    for row in board:
        print(row)
    # decide player
    xo = input("Are you playing as x or as o?: ")
    if xo == 'x':
        user1 = 'x'
        user2 = 'o'
        counter = 0
    else:
        user1 = 'o'
        user2 = 'x'
        counter = 1

    opts = ["x", "o"]

    while True:
        prompt = 'Where do you want to put your ' + str(opts[counter%2]) + ": "
        move = int(input(prompt))
        error = False
        if move in range(1,10):
            if move == 1:
                if type(board[0][0]) is int:
                    board[0][0] = opts[counter%2]
                else:
                    error = True
            elif move == 2:
                if type(board[0][1]) is int:
                    board[0][1] = opts[counter%2]
                else:
                    error = True
            elif move == 3:
                if type(board[0][2]) is int:
                    board[0][2] = opts[counter%2]
                else:
                    error = True
            elif move == 4:
                if type(board[1][0]) is int:
                    board[1][0] = opts[counter%2]
                else:
                    error = True
            elif move == 5:
                if type(board[1][1]) is int:
                    board[1][1] = opts[counter%2]
                else:
                    error = True
            elif move == 6:
                if type(board[1][2]) is int:
                    board[1][2] = opts[counter%2]
                else:
                    error = True
            elif move == 7:
                if type(board[2][0]) is int:
                    board[2][0] = opts[counter%2]
                else:
                    error = True
            elif move == 8:
                if type(board[2][1]) is int:
                    board[2][1] = opts[counter%2]
                else:
                    error = True
            elif move == 9:
                if type(board[2][2]) is int:
                    board[2][2] = opts[counter%2]
                else:
                    error = True
            # check if player tried to take a spot taken
            if not error:
                counter += 1
            else:
                print("Must be a vacant space!")
            # show board
            for row in board:
                # could check if all bits of row match here 
                print(row)
        else:
            print("Must be 1-9")
        play_again = False
        if board[0][0] == board[0][1] == board[0][2]:
            print("You win!")
            play_again = True
        elif board[1][0] == board[1][1] == board[1][2]:
            print("You win!")
            play_again = True
        elif board[2][0] == board[2][1] == board[2][2]:
            print("You win!")
            play_again = True
        elif board[0][0] == board[1][0] == board[2][0]:
            print("You win!")
            play_again = True
        elif board[0][1] == board[1][1] == board[2][1]:
            print("You win!")
            play_again = True
        elif board[0][2] == board[1][2] == board[2][2]:
            print("You win!")
            play_again = True
        elif board[0][0] == board[1][1] == board[2][2]:
            print("You win!")
            play_again = True
        elif board[2][0] == board[1][1] == board[0][2]:
            print("You win!")
            play_again = True
        if play_again:
            again = input("Do you want to play again: ")
            if again == True:
                game_running = True
            elif again == False:
                game_running = False