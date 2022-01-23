def hello():
    print("Hello, world!")


def multiply(x, y):
    return x * y


# def say_hello(name='caiman'):
#     print()


def coffee_fabric(coffee_type):
    def coffee_maker():
        print(f'This machine makes {coffee_type}')

    return coffee_maker


if __name__ == '__main__':  # pragma: no cover
    m1 = coffee_fabric('espresso')
    m2 = coffee_fabric('americano')
    m3 = coffee_fabric('latte')

    m1()
    m2()
    m3()
