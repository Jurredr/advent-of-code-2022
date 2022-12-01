class Day1():
    def part1(self):
        print(self.top_calories(1))

    def part2(self):
        print(self.top_calories(3))

    def top_calories(self, n: int) -> int:
        all_elves = open("input.txt").read().split("\n\n")
        calories = [sum(map(int, elf.split())) for elf in all_elves]
        return sum(sorted(calories)[-n:])


if __name__ == "__main__":
    day = Day1()
    day.part1()
    day.part2()
