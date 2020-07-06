from generators import *
import heapq


def generate_top_join_b(number_of_valid_lines):

    # create the generators
    generator_for_r1 = generate_next_r1(number_of_valid_lines)
    generator_for_r2 = generate_next_r2(number_of_valid_lines)

    r1_list = []
    r2_list = {}

    q = []

    # read the males sorted file

    try:
        while True:

            r2_tup = next(generator_for_r2)
            age = r2_tup[1].replace(' ', '')
            new_hash_list = []

            # create a hash table with age as the key and a list of tuples as a value

            if age in r2_list:
                # if exists just add the new tuple
                current_hash_list = r2_list[age]
                current_hash_list.append(r2_tup)
                new_hash_list = current_hash_list

            else:

                # else create the tuple list
                new_hash_list.append(r2_tup)

            # update the hash table
            r2_list.update({age: new_hash_list})

    except StopIteration:
        pass

    try:
        while True:

            r1_tup = next(generator_for_r1)
            r1_list.append(r1_tup)

            age = r1_tup[1].replace(' ', '')

            # check if an age number does not exist in the file
            if age not in r2_list:
                continue

            for tup in r2_list[age]:

                f_sum = float(r1_tup[25]) + float(tup[25])

                heapq.heappush(q, (-f_sum, (r1_tup, tup)))

    except StopIteration:
        pass

    while True:
        to_yield = heapq.heappop(q)
        yield to_yield
