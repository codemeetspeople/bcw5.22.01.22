def max_c_style():
    data = input()
    data = data.strip()
    data = data.split()

    for index, value in enumerate(data):
        data[index] = int(value)

    maximum = data[0]
    for elem in data[1:]:
        if elem > maximum:
            maximum = elem
    print(maximum)


def max_python_style():
    data = input().strip().split()
    print(max(map(int, data)))


if __name__ == '__main__':
    # max_c_style()
    max_python_style()
