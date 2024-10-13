import random

def build_grid(game_state):
    for i in range(len(game_state)):
        print(" _", end="")
    print("\n")
    
    for i in range(len(game_state)):
        for j in range(len(game_state)):
            print("|", end="")
            print(game_state[i][j], end="")
        print("|")
        for j in range(len(game_state)):
            print(" _", end="")
        print("\n")

def generate_random():
    return random.randint(0, 1)

def check(a, b, x, game_state):
    # Check for win conditions
    if (game_state[a][0] == x and game_state[a][1] == x and game_state[a][2] == x) or \
       (game_state[0][b] == x and game_state[1][b] == x and game_state[2][b] == x) or \
       (game_state[0][0] == x and game_state[1][1] == x and game_state[2][2] == x) or \
       (game_state[0][2] == x and game_state[1][1] == x and game_state[2][0] == x):
        return True
    return False

def initialise(size):
    game_state = {}
    for i in range(size):
        game_state[i] = {j: " " for j in range(size)}
    return game_state

game_state = initialise(3)
build_grid(game_state)

size = 0
visited = [[False, False, False] for _ in range(3)]
chance = generate_random()

while size < len(game_state) * len(game_state):
    if chance == 0:
        print("Your mark is 0. Give two indices (row and column):")
    else:
        print("Your mark is X. Give two indices (row and column):")

    a = int(input())
    b = int(input())
    
    # Input validation
    while a < 0 or a > 2 or b < 0 or b > 2 or visited[a][b]:
        print("Your input index is invalid. Give another valid input.")
        a = int(input())
        b = int(input())
    
    # Update game state
    mark = '0' if chance == 0 else 'X'
    game_state[a][b] = mark
    visited[a][b] = True
    size += 1
    
    build_grid(game_state)

    # Check for a win
    if check(a, b, mark, game_state):
        print(f"Player {'1' if chance == 0 else '2'} wins!")
        exit(0)
    
    chance = 1 - chance  # Switch turns

print("Match got tie!")
