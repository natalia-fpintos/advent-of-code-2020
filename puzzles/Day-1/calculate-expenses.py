def two_sum(values) -> int:
    sums = {}
    for v in values:
        if v in sums:
            return v * sums[v]
        sums[2020 - v] = v


def three_sum(values) -> int:
    for i in values:
        sums = {}
        for j in values:
            if j in sums:
                return j * sums[j][0] * sums[j][1]
            sums[2020 - j - i] = (j, i)


if __name__ == '__main__':
    file_contents = open('input/input.txt', 'r').read().splitlines()
    expenses = [int(v) for v in file_contents]

    result = two_sum(expenses)
    result2 = three_sum(expenses)
    print(result)
    print(result2)
