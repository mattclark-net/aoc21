# parse the input
with open("4-input.txt") as f:
    calls = [int(n) for n in f.readline().split(",")]
    boards = []
    while f.readline():
        board = []
        for line in range(5):
            board.extend([int(n) for n in f.readline().split()])
        boards.append([board, [0] * 25])


def updatedboards(boards, call):
    for board in boards:
        updatedboard = board.copy()
        for r in range(5):
            for c in range(5):
                if updatedboard[0][r * 5 + c] == call:
                    updatedboard[1][r * 5 + c] = 1
        yield updatedboard


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


def winners_and_losers(boards, call):
    winners = []
    losers = []
    for board in updatedboards(boards, call):
        winners.append(board) if winning(board) else losers.append(board)
    return winners, losers


def puzzle1(boards, calls):
    for call in calls:
        for board in updatedboards(boards, call):
            if winning(board):
                return board, call


def puzzle2(boards, calls):
    allwinners = []
    losers = boards.copy()
    for call in calls:
        winners, losers = winners_and_losers(losers, call)
        if winners != []:
            allwinners.append([winners, call])
    return allwinners[-1]


firstwinner, call = puzzle1(boards, calls)
print(
    "Puzzle 1: board {} won, score {}, last call {}, answer {}".format(
        firstwinner, score(firstwinner), call, score(firstwinner) * call
    )
)

lastwinners, call = puzzle2(boards, calls)
lastwinner = lastwinners[-1]
print(
    "Puzzle 2: board {} won, score {}, answer {}".format(
        lastwinner, score(lastwinner), call * score(lastwinner)
    )
)
