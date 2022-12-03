from enum import Enum

class PlayerOne(Enum):
    A = 1
    B = 2
    C = 3

class PlayerTwo(Enum):
    X = 1
    Y = 2
    Z = 3

def get_points_for_round(p1_move: PlayerOne, p2_move: PlayerTwo) -> int:
    if p1_move.value == p2_move.value:
        return 3 + p2_move.value
    elif (p2_move.value - p1_move.value) % 3 == 1:
        return 6 + p2_move.value
    else:
        return p2_move.value

def get_points_for_round_v2(p1_move: PlayerOne, outcome: PlayerTwo) -> int:
    # Lose
    if outcome == PlayerTwo.X:
        return [3, 1, 2][(p1_move.value - 1) % 3]
    # Draw
    elif outcome == PlayerTwo.Y:
        return 3 + p1_move.value
    # Win
    else:
        return 6 + [3, 1, 2][(p1_move.value + 1) % 3]

if __name__ == '__main__':
    with open('./input.txt') as f:
        total_points_1 = 0
        total_points_2 = 0
        games = f.readlines()
        for game in games:
            p1, p2 = game.strip().split(' ')
            p1_move, p2_move = PlayerOne[p1], PlayerTwo[p2]
            total_points_1 += get_points_for_round(p1_move, p2_move)
            total_points_2 += get_points_for_round_v2(p1_move, p2_move)
        print(total_points_1)
        print(total_points_2)




