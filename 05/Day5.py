import re

def main():
    # Open the input file and read the contents
    with open('05\input.txt') as f:
        lines = f.readlines()

    # Parse instructions from file
    instructions = []
    for line in lines:
        if ("move" in line):
            # https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
            instructions.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    
    # Parse starting state from file
    grid = []
    for line in lines:
        if ("1" in line):
            break
        else:
            grid.append(line.strip("\n").split(" "))
    # Transform grid into matrix
    newGrid = []
    for array in grid:
        i = 0
        n = len(array)
        ans = []
        while i<n:
            j = i+1
            while j<n and array[j]==array[i] and array[j]=='':
                j += 1
            if j-i==1:
                ans.append(array[i])
            else:
                for k in range(int((j-i)/4)):
                    ans.append("_")
            i=j
        newGrid.append(ans)

    # Transpose matrix and transform into list of lists
    # https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    crates = [[newGrid[j][i] for j in range(len(newGrid))] for i in range(len(newGrid[0]))]
    i = 0
    crates = [[i for i in row if i != "_"] for row in crates]
    crates = [[i.strip("[]") for i in row] for row in crates]
    for row in crates:
        row.reverse()
        row = [i for i in row if i != "_"]
        row = [i.strip("[]") for i in row]

    # Part 1
    # for inst in instructions:
        # move(crates, inst[0], inst[1], inst[2])

    # result = "".join([row[-1] for row in crates])
    # print(result)
    # QGTHFZBHV

    # Part 2

    for inst in instructions:
        move2(crates, inst[0], inst[1], inst[2])
    result = "".join([row[-1] for row in crates])
    print(result)
    # MGDMPSZTM

            
def move(array, iterations, fromRow, toRow):
    for i in range(iterations):
        array[toRow-1].append(array[fromRow-1].pop(-1))

def move2(array, crates, fromRow, toRow):
    movable = [array[fromRow-1].pop(-1) for i in range(crates)]
    movable.reverse()
    for e in movable:
        array[toRow-1].append(e)
        
if __name__ == '__main__':
    main()