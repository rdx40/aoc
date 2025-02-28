def cnt_houses(moves):
    visited = set()
    x,y = 0,0
    visited.add((x,y))

    for move in moves:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        visited.add((x,y))
    return len(visited)


def cnt_houses_two(moves):
    visited = set()
    a,b = 0,0
    c,d = 0,0
    visited.add((a,b))

    for i,move in enumerate(moves):
        if i%2 == 0:
            if move == '^':
                b += 1
            elif move == 'v':
                b -= 1
            elif move == '>':
                a += 1
            elif move == '<':
                a -= 1
            visited.add((a,b))
        else:
            if move == '^':
                d += 1
            elif move == 'v':
                d -= 1
            elif move == '>':
                c += 1
            elif move == '<':
                c -= 1
            visited.add((c,d))
    return len(visited)


            


with open('input.txt', "r") as file:
    moves = file.read().strip()

print("Part 1: ", cnt_houses(moves))
print("Part 2: ", cnt_houses_two(moves))
