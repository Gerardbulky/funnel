
'''

        case 1: head is two steps away from Tail horizontally
        or vertically. Tail moves one step in that direction

        case 2: The tail moves one step diagonaly to keep up
'''


def get_number_of_positions(row_string):
    head = (0, 0)
    tail = (0, 0)
    positions = {(0, 0)}
    for line in row_string.splitlines():
        direction = line.split()[0]
        steps = int(line.split()[1])
        while steps >= 1:
            if(direction == "R"):
                head = (head[0], head[1]+1)
            if(direction == "U"):
                head = (head[0]+1, head[1])
            if(direction == "L"):
                head = (head[0], head[1]-1)
            if(direction == "D"):
                head = (head[0]-1, head[1])
            steps -= 1
            tail = update(tail, head)
            positions.add(tail)
    return len(positions)


def update(tail, head):
    # at same location
    if(tail[0] == head[0] and tail[1] == head[1]):
        return tail
        # head is 2 steps up
    if(head[0] == tail[0]+2 and head[1] == tail[1]):
        tail = (tail[0]+1, tail[1])
        return tail
        # head is 2 steps down
    if(tail[0] == head[0]+2 and head[1] == tail[1]):
        tail = (tail[0]-1, tail[1])
        return tail
        # head is 2 steps left
    if(head[1] == tail[1]-2 and head[0] == tail[0]):
        tail = (tail[0], tail[1]-1)
        return tail
        # head is 2 steps right
    if(head[1] == tail[1]+2 and head[0] == tail[0]):
        tail = (tail[0], tail[1]+1)
        return tail

    # top right
    if(head[0] == tail[0]+2 and head[1] == tail[1]+1):
        tail = (tail[0]+1, tail[1]+1)
        return tail

    # bottom left
    if(head[0] == tail[0]-2 and head[1] == tail[1]-1):
        tail = (tail[0]-1, tail[1]-1)
        return tail
    # bottom right
    if(head[0] == tail[0]-2 and head[1] == tail[1]+1):
        tail = (tail[0]-1, tail[1]+1)
        return tail
    # top left
    if(head[0] == tail[0]+1 and head[1] == tail[1]-1):
        tail = (tail[0]+1, tail[1]-1)
        return tail
    if(head[0] == tail[0]+1 and head[1] == tail[1]-2):
        tail = (tail[0]+1, tail[0]-1)
        return tail
    if(head[0] == tail[0]+1 and head[1] == tail[1]+2):
        tail = (tail[0]+1, tail[1]+1)
        return tail
    if(head[0] == tail[0]-1 and head[1] == tail[1]-2):
        tail = (tail[0]-1, tail[1]-1)
        return tail
    if(head[0] == tail[0]-1 and head[1] == tail[1]+2):
        tail = (tail[0]-1, tail[1]+1)
        return tail
    return tail


EXAMPLE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()

print(get_number_of_positions(EXAMPLE))
