def main():
    statestr = ''

    current_player = 0

    board = [[1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0], [
        1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0]]
    for i in range(8):
        for j in range(8):
            statestr += str(board[i][j])

    if(current_player == 0):
        statestr += str(0)
    elif(current_player == 1):
        statestr += str(1)

    bytes = bytearray(statestr.encode('ascii'))


if __name__ == "__main__":
    main()
