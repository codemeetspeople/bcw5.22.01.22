def hello():
    print("Hello, world!")


def multiply(x, y):
    return x * y


def coffee_fabric(coffee_type):
    def coffee_maker():
        print(f'This machine makes {coffee_type}')

    return coffee_maker


def function(x, y, *args, color='black', **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':  # pragma: no cover
    function(1, 2, 3, 4, 5, color='black', user='root', value=42)
