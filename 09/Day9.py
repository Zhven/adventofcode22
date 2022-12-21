class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Return absolute distance to another point
    def dist(self, point):
        return abs(self.x - point.x), abs(self.y - point.y)

def parse():
    # Open the input file and read the contents
    with open('09\input.txt') as f:
        input = [line.split() for line in f.read().splitlines()]
    return input

def solve(length, input):
    tail_points = [Point(), ]
    points = [Point() for _ in range(length)]

    for direction, i in input:
        if direction in ['R', 'L', ]:
            move, steps = ('x', 1) if direction == 'R' else ('x', -1)
        if direction in ['U', 'D', ]:
            move, steps = ('y', 1) if direction == 'U' else ('y', -1)

        for j in range(int(i)):
            head = points[0]
            setattr(head, move, getattr(head, move) + 1*steps)
            for k in range(1, length):
                point = points[k]
                point_before = points[k-1]
                xd, yd = point_before.dist(point)
                if xd > 1 or yd > 1:
                    if point.x < point_before.x:
                        point.x += 1
                    elif point.x > point_before.x:
                        point.x -= 1
                    if point.y < point_before.y:
                        point.y += 1
                    elif point.y > point_before.y:
                        point.y -= 1
                    if k == len(points) - 1:
                        tail_points.append(Point(point.x, point.y))

    return len(set([(point.x, point.y) for point in tail_points]))

if __name__ == '__main__':
    instructions = parse()
    """Solve part 1."""
    print(f"Part 1: {solve(2, instructions)}")
    """Solve part 2."""
    print(f"Part 2: {solve(10, instructions)}")

"""The solve function takes a length and a list of input instructions as arguments. It initializes two lists of Point objects: tail_points and points. tail_points starts with a single point at the origin (0, 0), while points is a list of length points, also starting at the origin.

The function then iterates over the input instructions and moves each point in the points list according to the instructions. For each instruction, the function determines the direction of the move (either right, left, up, or down) and the number of steps to take. It then updates the x or y coordinate of the first point in the points list according to the direction and number of steps.

For each of the remaining points in the points list, the function calculates the distance between that point and the point before it. If the distance in either the x or y direction is greater than 1, the function moves the point closer to the point before it by one unit in the appropriate direction. If the point is the last point in the list, it is appended to the tail_points list.

Finally, the function returns the number of unique points in the tail_points list by creating a set of tuples representing the x and y coordinates of each point and taking the length of this set."""
