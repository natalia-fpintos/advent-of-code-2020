def two_sum(values) -> int:
    sums = {}
    for v in values:
        if v in sums:
            return v * sums[v]
        sums[2020 - v] = v


if __name__ == '__main__':
    file_contents = open('input/input.txt', 'r').read().splitlines()
    expenses = [int(v) for v in file_contents]

    result = two_sum(expenses)
    print(result)
