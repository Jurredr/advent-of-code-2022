class Day2():
    def part1(self):
        rounds = [round.replace('A', 'X').replace('B', 'Y').replace(
            'C', 'Z').split(' ') for round in open("input.txt").read().split("\n")]
        total = 0
        for round in rounds:
            total += ord(round[1]) - 87
            if round[0] == round[1]:
                total += 3
            elif (round[1] == 'X' and round[0] == 'Z') or (round[1] == 'Y' and round[0] == 'X') or (round[1] == 'Z' and round[0] == 'Y'):
                total += 6
        print(total)

    def part2(self):
        rounds = open("input.txt").read().split("\n")
        total = 0
        for round in rounds:
            total += {'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6,
                      'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
                      'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6}.get(round)
        print(total)


if __name__ == "__main__":
    day = Day2()
    day.part1()
    day.part2()
