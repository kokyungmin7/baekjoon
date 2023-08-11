import sys

N, M, T = map(int, sys.stdin.readline().rstrip().split())

clipboard = list()

for i in range(N):
    clipboard.append(list(sys.stdin.readline().rstrip()))

R, G, B = 0, 0, 0
mini = N if N < M else M
minimini = mini if mini < T else T
prev_mini_canvas = [['.' for __ in range(M)] for __ in range(N)]
curr_mini_canvas = [['.' for __ in range(M)] for __ in range(N)]

for t in range(minimini):
    if t+1 < minimini:
        for i in range(N):
            for j in range(M):
                if clipboard[i][j] != '.':
                    curr_mini_canvas[i][j] = clipboard[i][j]
                elif clipboard[i][j] == '.':
                    if i < N-1 and j < M-1:
                        curr_mini_canvas[i][j] = prev_mini_canvas[i + 1][j + 1]
                    elif i >= N and j >= M:
                        curr_mini_canvas[i][j] = '.'
                if i == 0 and j > 0:
                    if curr_mini_canvas[i][j] == 'R':
                        R += 1
                    elif curr_mini_canvas[i][j] == 'G':
                        G += 1
                    elif curr_mini_canvas[i][j] == 'B':
                        B += 1
                elif j == 0:
                    if curr_mini_canvas[i][j] == 'R':
                        R += 1
                    elif curr_mini_canvas[i][j] == 'G':
                        G += 1
                    elif curr_mini_canvas[i][j] == 'B':
                        B += 1
    elif t+1 == minimini:
        for i in range(N):
            for j in range(M):
                if clipboard[i][j] != '.':
                    curr_mini_canvas[i][j] = clipboard[i][j]
                elif clipboard[i][j] == '.':
                    if i < N-1 and j < M-1:
                        curr_mini_canvas[i][j] = prev_mini_canvas[i + 1][j + 1]
                    elif i >= N and j >= M:
                        curr_mini_canvas[i][j] = '.'
                if curr_mini_canvas[i][j] == 'R':
                    R += 1
                elif curr_mini_canvas[i][j] == 'G':
                    G += 1
                elif curr_mini_canvas[i][j] == 'B':
                    B += 1

    prev_mini_canvas = curr_mini_canvas

if T > mini:
    add_row_R = curr_mini_canvas[0][1:].count('R')
    add_row_G = curr_mini_canvas[0][1:].count('G')
    add_row_B = curr_mini_canvas[0][1:].count('B')
    add_col_R = [i[0] for i in curr_mini_canvas].count('R')
    add_col_G = [i[0] for i in curr_mini_canvas].count('G')
    add_col_B = [i[0] for i in curr_mini_canvas].count('B')
    R += add_row_R * (T - mini)
    G += add_row_G * (T - mini)
    B += add_row_B * (T - mini)
    R += add_col_R * (T - mini)
    G += add_col_G * (T - mini)
    B += add_col_B * (T - mini)
print(R, G, B, sep='\n')
