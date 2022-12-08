def main():
    # Open the input file and read the contents
    with open('06\input.txt') as f:
        input = f.read()

    startOfPacket = findIndex(input, 0, 4)
    startOfMessage = findIndex(input, 0, 14)
    
    print(startOfPacket)
    # 1625
    print(startOfMessage)
    # 2250

def findIndex(input, start, stop):
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