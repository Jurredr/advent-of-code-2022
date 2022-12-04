class Day4():
    def part1(self):
        pairs = [pair for pair in [[list(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)), list(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1))]
                                   for pair in [pair.split(',') for pair in open("input.txt").read().split("\n")]] if set(pair[0]).issubset(set(pair[1])) or set(pair[1]).issubset(set(pair[0]))]
        print(len(pairs))

    def part2(self):
        pairs = [pair for pair in [[list(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)), list(range(int(pair[1].split('-')[0]),
                                                                                                                        int(pair[1].split('-')[1]) + 1))] for pair in [pair.split(',') for pair in open("input.txt").read().split("\n")]] if set(pair[0]).intersection(set(pair[1]))]
        print(len(pairs))


if __name__ == "__main__":
    day = Day4()
    day.part1()
    day.part2()
