# parse the input
with open("4-input.txt") as f:
    calls = [int(n) for n in f.readline().split(",")]
    boards = []
    while f.readline():
        board = []
        for line in range(5):
            board.append([int(n) for n in f.readline().split()])
        boards.append(board)


def update(board, call):
    for r in range(5):
        for c in range(5):
            if board[r][c] == call:
                board[r][c] = 0


def winning(board):
    for r in range(5):
        if sum(board[r]) == 0:
            return True
    for c in range(5):
        if sum([row[c] for row in board]) == 0:
            return True
    return False


def score(board):
    score = 0
    for r in range(5):
        for c in range(5):
            score += board[r][c]
    return score


def puzzle1(calls, boards):
    for call in calls:
        for board in boards:
            update(board, call)
            if winning(board):
                print(
                    "Puzzle 1: board {} won, score {}, last call {}, answer {}".format(
                        board, score(board), call, score(board) * call
                    )
                )
                return


def puzzle2(calls, boards):
    winners = []
    for call in calls:
        losers = []
        for board in boards:
            update(board, call)
            if winning(board):
                winners.append((call, board))
            else:
                losers.append(board)
        boards = losers
    (call, winner) = winners[-1]
    print(
        "Puzzle 2: board {} won, score {}, answer {}".format(
            winner, score(winner), call * score(winner)
        )
    )
    return


puzzle1(calls, boards.copy())
puzzle2(calls, boards.copy())
