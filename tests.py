import random

from main import binary_search

test_sample_size = 10000
test_rand_size = 100


def test_binary_search_case_1():
    test_random_values = tuple(random.randint(0, test_rand_size - 1) for _ in range(test_sample_size))
    test_target_array = tuple(range(test_rand_size))

    for value in test_random_values:
        response = binary_search(test_target_array, value)

        assert response.found_value == value
        assert response.count_attempts < 20
