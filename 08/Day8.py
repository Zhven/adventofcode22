ROWS = None
COLUMNS = None

def parse():
    global ROWS, COLUMNS
    # Open the input file and read the contents
    with open('08\input.txt') as f:
        input = f.read().splitlines()

    test = ['30373',
            '25512',
            '65332',
            '33549',
            '35390'
            ]

    forest = [[int(item) for item in line] for line in input]
    ROWS = len(forest)
    COLUMNS = len(forest[0])

    return forest

def find_trees(forest):
    # Add edges as visible trees
    edges = (ROWS*2) + ((COLUMNS-2)*2) 
    total = edges


    for row in range(1, ROWS-1):
        for col in range(1, COLUMNS-1):           
            tree = forest[row][col]
            
            # Get the full row and column of the current tree
            left = [forest[row][col-i] for i in range(1, col+1)]
            right = [forest[row][col+i] for i in range(1, COLUMNS-col)]
            up = [forest[row-i][col] for i in range(1, row+1)]
            down = [forest[row+i][col] for i in range(1, ROWS-row)]

            # Check each direction for higher trees
            if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
                total += 1
    
    return total


def find_highest_scenic_score(forest):
    scores = []
    for row in range(1, ROWS-1):
        for col in range(1, COLUMNS-1):           
            tree = forest[row][col]
            
            # Get the full row and column of the current tree
            left = [forest[row][col-i] for i in range(1, col+1)]
            right = [forest[row][col+i] for i in range(1, COLUMNS-col)]
            up = [forest[row-i][col] for i in range(1, row+1)]
            down = [forest[row+i][col] for i in range(1, ROWS-row)]

            # Find scenic score
            score = 1
            for lst in (left, right, up, down):
                tracker = 0
                for i in range(len(lst)):
                    if lst[i] < tree:
                        tracker += 1
                    elif lst[i] >= tree:
                        tracker += 1
                        break
                score *= tracker
            scores.append(score)
    
    return max(scores)

if __name__ == '__main__':
    """Solve part 1."""
    forest = parse()
    visible_trees = find_trees(forest)
    print(f"Part 1: {visible_trees}")
    """Solve part 2."""
    highest_score = find_highest_scenic_score(forest)
    print(f"Part 2: {highest_score}")

