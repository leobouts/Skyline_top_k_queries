from a_top_k import *
from b_top_k import *
import sys
import time


def main():

    # top-k input given from terminal argument
    k = sys.argv[1]

    number_of_valid_lines = []

    # generator that yields every k for the a-join algorithm (HRJN) and b-join
    top_k_a_generator = generate_top_join_a(number_of_valid_lines)
    top_k_b_generator = generate_top_join_b(number_of_valid_lines)

    # test the generator for the top-k input
    # starting time

    start_time = time.time()

    for i in range(int(k)):

        top_k = next(top_k_a_generator)

        print(str(i+1)+'. pair: '+str(top_k[1][0][0])+','+str(top_k[1][1][0])+' score:'+str(-top_k[0]))

    top_k_time = time.time() - start_time

    print('time in seconds:', top_k_time)

    print('===================')

    start_time = time.time()

    for i in range(int(k)):
        top_k = next(top_k_b_generator)
        print(str(i + 1) + '. pair: ' + str(top_k[1][0][0]) + ',' + str(top_k[1][1][0]) + ' score:' + str(-top_k[0]))

    top_k_time = time.time() - start_time

    print('time in seconds:', top_k_time)


if __name__ == "__main__":
    main()
