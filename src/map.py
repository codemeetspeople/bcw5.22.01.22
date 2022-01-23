def increment(x):
    return x + 1


def pow2(x):
    return x ** 2


def handler(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


if __name__ == '__main__':  # pragma: no cover
    array = [1, 2, 3, 4, 5]

    # incremented = handler(increment, array)
    # powered = handler(pow2, array)

    incremented = list(map(increment, array))
    powered = list(map(pow2, array))

    print(array)
    print(incremented)
    print(powered)
