import pytest
from generator import my_range


def _test_gen(gen_params, expected_values):
    gen = my_range(*gen_params)

    for expected in expected_values:
        assert next(gen) == expected

    with pytest.raises(StopIteration):
        next(gen)


def test_generator_one_arg():
    _test_gen((5,), (0, 1, 2, 3, 4))


def test_generator_start_end():
    _test_gen((4, 7), (4, 5, 6))


def test_generator_start_end_step():
    _test_gen((0, 10, 2), (0, 2, 4, 6, 8))
