ALL_CYCLES = []
def parse():
    # Open the input file and read the contents
    with open('10\input.txt') as f:
        input = [line.split() for line in f.read().splitlines()]
    return input
    #return [["noop"], ["addx", "3"], ["addx", "-5"]]


def calculate_signal_strengths(instructions:list) -> int:
    global ALL_CYCLES

    for instruction in instructions:
        if instruction[0] == "noop":
            ALL_CYCLES.append(0)
        else:
            ALL_CYCLES.extend([0, int(instruction[1])])

    cycle_counter = 20
    sums = []

    for _ in ALL_CYCLES[20::40]:
        total = 1
        total += sum(ALL_CYCLES[:cycle_counter-1])
        sums.append(total * cycle_counter)
        cycle_counter += 40
    
    print(sums)
    return(sum(sums))

def render_image(all_cycles:list) -> None:
    monitor = [["░"] * 40 for _ in range(6)]
    i = 0
    current_index = 40

    for cycle in range(len(all_cycles)):
        pixel = sum(all_cycles[:cycle]) + 1
        if cycle % 40 in range(pixel-1, pixel+2):
            monitor[i][cycle%40] = "▓"

        if cycle > current_index-2:
            i += 1
            current_index += 40
    
    for line in monitor:
        print("".join([pixel for pixel in line]))

if __name__ == '__main__':
    instructions = parse()
    """Solve part 1."""
    print(f"Part 1: {calculate_signal_strengths(instructions=instructions)}")
    """Solve part 2."""
    print("Part 2: Rendered image is")
    render_image(ALL_CYCLES)