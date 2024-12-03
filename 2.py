def is_valid_move(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def knights_tour(N, startX, startY):
    # 定義騎士的8個移動方向
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    # 初始化棋盤
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[startX][startY] = 0  # 起始位置標記為0
    
    def dfs(x, y, step):
        if step == N * N - 1:  # 如果已經訪問所有位置
            return True
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            
            if is_valid_move(nx, ny, board, N):
                board[nx][ny] = step + 1
                if dfs(nx, ny, step+1):
                    return True
                board[nx][ny] = -1  # 回溯
        return False
    return dfs(startX, startY, 0)

# 輸入
N = 5
startX = 0
startY = 1

# 輸出
print(knights_tour(N, startX, startY))