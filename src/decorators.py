def run_n_times(times):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        inner_wrapper.__name__ = func.__name__
        return inner_wrapper
    return outer_wrapper


@run_n_times(5)
def hello(user):
    print(f'hello, {user}')


@run_n_times(5)
def hello_to_two(user1, user2):
    print(f'hello, {user1} and {user2}')


if __name__ == '__main__':  # pragma: no cover
    hello('caiman')
    hello_to_two('saruman', 'zurbagan')

