if __name__ == '__main__':
    with open("01\input.txt") as file:
        elfs = [s.split("\n") for s in file.read().split("\n\n")]
        elfs = [sum(int(j) for j in i if j!='') for i in elfs]
        elfs.sort(reverse=True)
        
        mostCalories = elfs[0]

        top3Calories = sum(elfs[0:3])

    print(elfs)
    print(mostCalories)
    print(elfs)
    print(top3Calories)