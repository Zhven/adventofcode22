def get_answer():
    with open("01\input.txt") as file:
        elfs = [s.split("\n") for s in file.read().split("\n\n")]
        elfs = [sum(int(j) for j in i if j!='') for i in elfs]
        elfs.sort(reverse=True)
        
        most_calories = elfs[0]

        top_3_calories = sum(elfs[0:3])

    print(elfs)
    print(most_calories)
    print(elfs)
    print(top_3_calories)

if __name__ == '__main__':
    get_answer()