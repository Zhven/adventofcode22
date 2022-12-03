def solverProblem1(measurements):
    increase = 0

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increase += 1

    print("Problem 1 answer: " + increase)


def solverProblem2(measurements):
    increase = 0

    for i in range(2, len(measurements) - 1):
        if (measurements[i - 2] + measurements[i - 1] + measurements[i]) < (
                measurements[i - 1] + measurements[i] + measurements[i + 1]):
            increase += 1

    print("Problem 2 answer: " + increase)


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