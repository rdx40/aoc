def count_houses(instructions):
    position = (0, 0)  
    visited_houses = set()
    visited_houses.add(position)
    moves = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}

    for move in instructions:
        position = (position[0] + moves[move][0], position[1] + moves[move][1])
        visited_houses.add(position)

    return len(visited_houses)

def count_houses_with_robot(instructions):
    santa_position = (0, 0)  
    robot_position = (0, 0)  
    visited_houses = set()
    visited_houses.add(santa_position)

    moves = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}


    for i, move in enumerate(instructions):
        if i % 2 == 0:
            santa_position = (santa_position[0] + moves[move][0], santa_position[1] + moves[move][1])
            visited_houses.add(santa_position)
        else:
            robot_position = (robot_position[0] + moves[move][0], robot_position[1] + moves[move][1])
            visited_houses.add(robot_position)

    return len(visited_houses)

try:
    with open('input.txt', 'r') as f:
        instructions = f.read().strip()

    
    houses_visited = count_houses(instructions)
    print("Part 1: Houses visited by Santa:", houses_visited)

    
    houses_visited_with_robot = count_houses_with_robot(instructions)
    print("Part 2: Houses visited by Santa and Robot:", houses_visited_with_robot)

except FileNotFoundError:
    print("Error: 'input.txt' not found.")
