from generators import *
import heapq


def generate_top_join_a(number_of_valid_lines):

    # create the generators
    generator_for_r1 = generate_next_r1(number_of_valid_lines)
    generator_for_r2 = generate_next_r2(number_of_valid_lines)
    
    # list that hold examined items
    r1_list = []
    r2_list = []

    q = []

    # get the first tuples from the two relations Ri.
    # initialize the values
    # ri_tup[25] holds the weight
    # ri_tup[0] holds the id
    # we want the top-k pairs from summing the instance weight
    # instance weight is in index 25

    ###############
    # R1 tuple    #
    ###############

    r1_tup = next(generator_for_r1)
    p1_max = r1_tup[25]
    p1_cur = r1_tup[25]
    r1_list.append(r1_tup)



    ################
    # R2 tuple     #
    ################

    r2_tup = next(generator_for_r2)
    p2_max = r2_tup[25]
    p2_cur = r2_tup[25]
    r2_list.append(r2_tup)

    # checks that each time one tuple from each relation
    # will be selected

    turn_counter = 1
    
    while True:

        # update threshold
        f1 = float(p1_max) + float(p2_cur)
        f2 = float(p1_cur) + float(p2_max)

        threshold = max(f1, f2)

        if turn_counter % 2 == 1:

            r1_tup = next(generator_for_r1)
            p1_cur = r1_tup[25]
            r1_list.append(r1_tup)

            # create the new pairs of two (join)
            pairs_list = [(r1_tup, x) for x in r2_list]

        else:

            r2_tup = next(generator_for_r2)
            p2_cur = r2_tup[25]
            r2_list.append(r2_tup)

            # create the new pairs of two (join)
            pairs_list = [(r2_tup, x) for x in r1_list]

        turn_counter += 1

        for pair in pairs_list:

            if pair[0][1] == pair[1][1]:
                f_sum = float(pair[0][25]) + float(pair[1][25])

                heapq.heappush(q, (-f_sum, pair))

        # while we have pairs with score bigger than the threshold report them

        while len(q) > 0 and float(q[0][1][0][25])+float(q[0][1][1][25]) >= threshold:

            to_yield = heapq.heappop(q)

            yield to_yield
