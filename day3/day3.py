class Day3():
    def part1(self, rucksacks):
        priorities = sum([(ord(duplicate_char) - 38 if duplicate_char.isupper() else ord(duplicate_char) - 96)
                          for duplicate_char in [(set(rucksack[0]) & set(rucksack[1])).pop() for rucksack in rucksacks]])
        print(priorities)

    def part2(self, rucksacks):
        groups = (rucksacks[i:i+3] for i in range(0, len(rucksacks), 3))
        badges = ((set(group[0]) & set(group[1]) & set(
            group[2])).pop() for group in groups)
        print(sum([(ord(char) - 38 if char.isupper() else ord(char) - 96)
              for char in badges]))


if __name__ == "__main__":
    day = Day3()
    day.part1([(rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):])
               for rucksack in open("input.txt").read().split("\n")])
    day.part2(open("input.txt").read().split("\n"))
