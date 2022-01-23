if __name__ == '__main__':  # pragma: no cover
    x, y = 10, 20

    if x > y:
        print(x)
    else:
        print(y)

    if x % 3 == 0:
        print('alpha')
    elif x % 4 == 0:
        print('bravo')
    else:
        print('delta')
