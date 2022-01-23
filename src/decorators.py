def run_5_times(func):
    def wrapper():
        for i in range(5):
            func()
    return wrapper


@run_5_times
def hello():
    print("Hello, world!")

# def hello():
#     print("Hello, world!")
# hello = run_5_times(hello)


@run_5_times
def hello2():
    print("Hello, world2!")


if __name__ == '__main__':  # pragma: no cover
    hello2()
