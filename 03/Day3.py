def main():
    # Part 1
    items_to_reorganize = []
    total = 0

    with open("03\input.txt") as file:
        rucksaks = file.readlines()

    for sack in rucksaks:
        first_compartment, second_compartment = sack[:len(sack)//2], sack[len(sack)//2:]
        #items_to_reorganize = [item for item in first_compartment if item in second_compartment]
        for item in first_compartment:
            if item in second_compartment:
                items_to_reorganize.append(item)
                break

    for item in items_to_reorganize:
        if item.isupper():
            total += (ord(item) - 64 + 26)
        else:
            total += (ord(item) - 96)
    
    print(total)

    # Part 2
    badge_priorities = 0
    # Divide rucksacks into groups of 3
    groups = list(divide_chunks(rucksaks, 3))
    for group in groups:
        # Strip line ending from lists
        group = [elf.strip("\n") for elf in group]
        group_items = []
        # Find all common items for 2 elves
        for item in group[0]:
            if item in group[1]:
                group_items.append(item)
        # Find the first common item with 3rd elf
        for item in group_items:
            if item in group[2]:
                if item.isupper():
                    badge_priorities += (ord(item) - 64 + 26)
                else:
                    badge_priorities += (ord(item) - 96)
                break
            
    print(badge_priorities)

def divide_chunks(l, n): # https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    for i in range(0, len(l), n):
        yield l[i:i + n]

if __name__ == '__main__':
    main()