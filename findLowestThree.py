import random

def find_Lowest_Three(list_of_tuples):
    lowest = list_of_tuples[0]
    for distance, index in list_of_tuples:
        if distance < lowest[0]:
            lowest = (distance, index)

    del list_of_tuples[list_of_tuples.index(lowest)]
    lower = list_of_tuples[0]

    for distance, index in list_of_tuples:
        if distance < lower[0]:
            lower = (distance, index)

    del list_of_tuples[list_of_tuples.index(lower)]
    low = list_of_tuples[0]

    for distance, index in list_of_tuples:
        if distance < low[0]:
            low = (distance, index)

    del list_of_tuples[list_of_tuples.index(low)]

    return low, lower, lowest







if __name__ == "__main__":
    p = []
    for i in range(30):
        p.append((random.randrange(255), i+1))

    for i in p:
        print i

    print "blarrrh"
    find_Lowest_Three(p)
