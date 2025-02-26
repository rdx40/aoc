def find_floor(instructions):
    floor = instructions.count('(')-instructions.count(')')
    return floor

def find_basement_position(instructions):
    floor = 0
    for position, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return position
    return None

with open('input.txt', 'r') as f:
    instructions = f.read().strip()

floor = find_floor(instructions)
print("Part 1: Final floor: ",floor)

basement_position = find_basement_position(instructions)
print("Part 2: First basement position: ",basement_position)


