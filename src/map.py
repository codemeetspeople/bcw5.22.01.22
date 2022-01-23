def handler(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


if __name__ == '__main__':  # pragma: no cover
    array = [1, 2, 3, 4, 5]

    # incremented = handler(lambda x: x + 1, array)
    # powered = handler(lambda x: x ** 2, array)

    incremented = list(map(lambda x: x + 1, array))
    powered = list(map(lambda x: x ** 2, array))

    print(array)
    print(incremented)
    print(powered)
