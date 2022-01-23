def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step


if __name__ == '__main__':  # pragma: no cover
    # for i in my_range(5):  # 0, 1, 2, 3, 4
    #     print(i)

    # for i in my_range(7, 10):  # 7, 8, 9
    #     print(i)

    for i in my_range(0, 10, 2):  # 0, 2, 4, 6, 8
        print(i)
