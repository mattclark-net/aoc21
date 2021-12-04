# parse the input
with open("4-input.txt") as f:
    calls = [int(n) for n in f.readline().split(",")]
    boards = []
    while f.readline():
        board = []
        for line in range(5):
            board.extend([int(n) for n in f.readline().split()])
        boards.append([board, [0] * 25])


def update(board, call):
    for r in range(5):
        for c in range(5):
            if board[0][r * 5 + c] == call:
                board[1][r * 5 + c] = 1


def winning(board):
    for r in range(5):
        if sum(board[1][r * 5 : (r + 1) * 5]) == 5:
            return True
    for c in range(5):
        if sum([board[1][r * 5 + c] for r in range(5)]) == 5:
            return True
    return False


def score(board):
    score = 0
    for r in range(5):
        for c in range(5):
            if board[1][r * 5 + c] == 0:
                score += board[0][r * 5 + c]
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
                winners.append((board, call))
            else:
                losers.append(board)
        boards = losers
    (winner, call) = winners[-1]
    print(
        "Puzzle 2: board {} won, score {}, answer {}".format(
            winner, score(winner), call * score(winner)
        )
    )
    return


puzzle1(calls, boards.copy())
puzzle2(calls, boards.copy())
