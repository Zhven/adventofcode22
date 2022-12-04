def main():
    # Part 1
    itemsToReorganize = []
    total = 0

    with open("03\input.txt") as file:
        rucksaks = file.readlines()

    for sack in rucksaks:
        firstCompartment, secondCompartment = sack[:len(sack)//2], sack[len(sack)//2:]
        #itemsToReorganize = [item for item in firstCompartment if item in secondCompartment]
        for item in firstCompartment:
            if item in secondCompartment:
                itemsToReorganize.append(item)
                break

    for item in itemsToReorganize:
        if item.isupper():
            total += (ord(item) - 64 + 26)
        else:
            total += (ord(item) - 96)
    
    print(total)

    # Part 2
    badgePriorities = 0
    # Divide rucksacks into groups of 3
    groups = list(divide_chunks(rucksaks, 3))
    for group in groups:
        # Strip line ending from lists
        group = [elf.strip("\n") for elf in group]
        groupItems = []
        # Find all common items for 2 elves
        for item in group[0]:
            if item in group[1]:
                groupItems.append(item)
        # Find the first common item with 3rd elf
        for item in groupItems:
            if item in group[2]:
                if item.isupper():
                    badgePriorities += (ord(item) - 64 + 26)
                else:
                    badgePriorities += (ord(item) - 96)
                break
            
    print(badgePriorities)

def divide_chunks(l, n): # https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    for i in range(0, len(l), n):
        yield l[i:i + n]

if __name__ == '__main__':
    main()