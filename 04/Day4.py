def main():
    # Part 1
    total = 0

    with open("04\input.txt") as file:
        pairs = file.readlines()

    for pair in pairs:
        first,second = pair.strip("\n").split(',', 1)
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]

        if (first[0] <= second[0] and first[1] >= second[1] # Second contained in first
            or second[0] <= first[0] and second[1] >= first[1]): # First contained in second
            total += 1

    print(total)
    # 536

    # Part 2
    total = 0
    
    for pair in pairs:
        first,second = pair.strip("\n").split(',', 1)
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]
        first = range(first[0], first[1])
        second = range(second[0], second[1])

        if (first.start <= second.stop and second.start <= first.stop):
            total += 1

    print(total)
    # 845

if __name__ == '__main__':
    main()