import operator

PART = 0

class Monkey:
    def __init__(self, number:int, items:list, operation:list, test_nr:int, true_throw:int, false_throw:int):
        self.number = number
        self.items = items
        self.operation = operation
        self.test_nr = test_nr
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspected = 0

    # Monkey inspects item and worry level is calculated based on the monkey's operation
    def inspect(self, item):
        global PART
        allowed_operators={
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv}
        # Map monkey's operation to calculate result
        operation = [item if op == "old" else op for op in self.operation]
        # Inspects -> worry level goes up
        result = allowed_operators[operation[1]](operation[0],operation[2])
        # Iterate inspected items count
        self.inspected += 1
        # print(f"Monkey {self.number} inspects an item with a worry level of {item}")
        # print(f"Worry level is calculated {operation} to {result}")
        if PART == 1:
            # then gets bored -> worry level / 3
            result = result // 3
            # print(f"Monkey gets bored with item. Worry level is divided by 3 to {result}.")
        else:
            # then gets bored -> worry level / 3
            result = result % PART
            # print(f"Monkey gets bored with item. Worry level is divided by 3 to {result}.")
        return result

    def decide(self, item):
        if item % self.test_nr == 0:
            # print(f"Current worry level is divisible by {self.test_nr}.")
            # print(f"Item with worry level {item} is thrown to monkey {self.false_throw}")
            return self.true_throw
        else:
            # print(f"Current worry level is not divisible by {self.test_nr}.")
            # print(f"Item with worry level {item} is thrown to monkey {self.false_throw}")
            return self.false_throw

    def __str__(self):
        return f"Monkey number: {self.number}, items: {self.items}, inspected: {self.inspected}"

    def __repr__(self):
        return f"Monkey number: {self.number}, items: {self.items}, inspected: {self.inspected}"

def parse():
    # Open the input file and read the contents
    with open('11\input.txt') as f:
        input = [obj.split("\n") for obj in f.read().split("\n\n")]
    
    monkeys = []
    for obj in input:
        number = obj[0].strip(":").split(" ")[1]
        items = [int(e.strip(", ")) for e in obj[1].strip(",").split(" ")[4:]]
        operation = [int(e) if e.isnumeric() else e for e in obj[2].split(" ")[-3:]]
        test_nr = int(obj[3].split(" ")[-1])
        true_throw = int(obj[4].split(" ")[-1])
        false_throw = int(obj[5].split(" ")[-1])
        monkeys.append(Monkey(number, items, operation, test_nr, true_throw, false_throw))
    return monkeys

def play(monkeys:list, rounds:int):
    for round in range(rounds):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items[0]
                monkey.items.pop(0)
                new_worry_level = monkey.inspect(item)
                throw_to = monkey.decide(new_worry_level)
                new_monkey = monkeys[throw_to]
                # print(new_monkey)
                new_monkey.items.append(new_worry_level)
        # print(f"After round {round + 1}")
        # print_inspections(monkeys)

def monkeys_sorted_by_inspections(monkeys:list):
   newlist = sorted(monkeys, key=lambda x: x.inspected, reverse=True)
   return newlist[0].inspected * newlist[1].inspected

def print_inspections(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkey.number}: is holding {[e for e in monkey.items]}")

def calculate_modulus(monkeys):
    mod_all = 1
    for div_by in [m.test_nr for m in monkeys]:
        mod_all *= div_by
    return mod_all

if __name__ == '__main__':
    """Solve part 1."""
    PART = 1
    monkeys = parse()
    play(monkeys=monkeys, rounds=20)
    print(monkeys_sorted_by_inspections(monkeys=monkeys))
    """Solve part 2."""
    monkeys = parse()
    PART = calculate_modulus(monkeys=monkeys)
    play(monkeys=monkeys, rounds=10000)
    print(monkeys_sorted_by_inspections(monkeys=monkeys))