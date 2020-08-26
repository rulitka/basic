def ConquestCampaign(N, M, L, battalion):
    board = [[0]*M for i in range(N)]
    day = 1
    count = N*M
    
    for i in range(0, 2*L, 2): 
        x = battalion[i] - 1 
        y = battalion[i+1] - 1 
        if board[x][y] == 0:
            board[x][y] = 1
            count -= 1
            
    while count != 0:
        new_board = [[board[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                        if 0 <= x < N and 0 <= y < M and new_board[x][y] == 0:
                            new_board[x][y] = 1
                            count -= 1
        board = new_board
        day += 1
    return day
