class Node():

    def __init__(self):
        self.parent = None
        self.children = []
        self.size = 0
        self.name = None

def parse():
    # Open the input file and read the contents
    with open('07\input.txt') as f:
        input = f.readlines()
        curr_node = None
        head = None

    for line in input:
        curr_node, head = switch(line.strip("\n").split(" "), curr_node, head)

    calculate_folder_sizes(head, head.size)

    return head

def switch(case, curr_node, head):
    if all(('$' in case, 'cd' in case)):
        directory = case[-1]
        if directory == '..':
            curr_node = curr_node.parent
        elif directory == '/':
            head = Node()
            head.name = directory
            curr_node = head
        else:
            next_node = [child for child in curr_node.children if child.name == directory]
            curr_node = next_node[0]
    elif all(('$' in case, 'ls' in case)):
        pass
    elif 'dir' in case:
        directory = case[-1]
        new_node = Node()
        new_node.name = directory
        new_node.parent = curr_node
        curr_node.children.append(new_node)
    else:
        size = case[0]
        file = case[-1]
        new_node = Node()
        new_node.children = None
        new_node.name = file
        new_node.size = int(size)
        new_node.parent = curr_node
        curr_node.children.append(new_node)
    return curr_node, head
                
def calculate_folder_sizes(head, size):
    if head.children is None:
        return head, head.size
    else:
        size_sum = sum([calculate_folder_sizes(child, size)[1] for child in head.children])
        head.size += size_sum
        return head, head.size

def sum_directories_less_than_100000(head, total):
    if head.children is None:
        return head, total
    else:
        total += head.size if head.size <= 100000 else 0
        for child in head.children:
            total = sum_directories_less_than_100000(child, total)[1]

        return head, total

def smallest_dir_for_deletion(head, size, required):
    if head.children is None:
        return head, size, required
    else:
        if size == 0:
            size = max(size, head.size if head.size >= required else size)
        else:
            size = min(size, head.size if head.size >= required else size)
        for child in head.children:
            size = smallest_dir_for_deletion(child, size, required)[1]

        return head, size, required


if __name__ == '__main__':
    data = parse()
    """Solve part 1."""
    print(f"Part 1: {sum_directories_less_than_100000(data, 0)[1]}")
    """Solve part 2."""
    total_used = data.size
    available = 70000000
    target_unused = 30000000
    current_unused = available - total_used
    required = target_unused - current_unused
    print(f"Part 2: {smallest_dir_for_deletion(data, 0, required)[1]}")

