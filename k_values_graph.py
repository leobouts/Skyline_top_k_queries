from a_top_k import *
from b_top_k import *
import time


def main():

    # test the generator for the top-k input
    # starting time

    values_k = [1, 2, 5, 10, 20, 50, 100]
    times_topk_join_a = []
    times_topk_join_b = []
    number_of_valid_lines_a = []
    number_of_valid_lines_b = []

    for k in values_k:

        number_of_valid_lines = []
        top_k_a_generator = generate_top_join_a(number_of_valid_lines)
        start_time_a = time.time()

        for i in range(k):
            next(top_k_a_generator)

        number_of_valid_lines_a.append(len(number_of_valid_lines))
        top_k_time_a = time.time() - start_time_a
        times_topk_join_a.append(top_k_time_a)

        number_of_valid_lines = []
        top_k_b_generator = generate_top_join_b(number_of_valid_lines)
        start_time_b = time.time()

        for i in range(k):
            next(top_k_b_generator)

        number_of_valid_lines_b.append(len(number_of_valid_lines))
        top_k_time_b = time.time() - start_time_b
        times_topk_join_b.append(top_k_time_b)

    print(times_topk_join_a)
    print(times_topk_join_b)
    print(number_of_valid_lines_a)
    print(number_of_valid_lines_b)


if __name__ == "__main__":
    main()

