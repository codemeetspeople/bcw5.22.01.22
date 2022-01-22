if __name__ == '__main__':
    # for loop
    # for i in range(0, 10, 2):
    #     print(i)

    # while loop
    # i = 0
    # while i < 10:
    #     print(i)
    #     i += 1

    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    # for elem in array:
    #     print(elem)

    params = {
        'login': 'caiman',
        'password': 'qwerty',
        'id': 12345
    }

    for key, value in params.items():
        print(key, value)
