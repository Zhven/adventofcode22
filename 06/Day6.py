def main():
    # Open the input file and read the contents
    with open('06\input.txt') as f:
        input = f.read()

    start_of_packet = find_index(input, 0, 4)
    start_of_message = find_index(input, 0, 14)
    
    print(start_of_packet)
    # 1625
    print(start_of_message)
    # 2250

def find_index(input, start, stop):
    size = stop
    while True:
        chunk = input[start:stop:1]
        start += 1
        stop += 1
        chunk_list = list(chunk)

        for letter in chunk:
            if chunk.count(letter) > 1:
                chunk_list.remove(letter)

        if len(chunk_list) == size:
                return stop - 1

if __name__ == '__main__':
    main()