'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Approach

"Build a hash table of all positive elements in
the given array. Once the hash table is built, look in the hash table for
all positive integers, starting from 1. As soon as we find a number which is not
there in hash table, we return it. This approach may take O(n) time on average,
but it requires O(n) extra space." - Jedshady's solution, including code bellow
'''

def solution(l):
    positive_list = remove_negative(l)
    positive_list = modify_index(positive_list)
    smallest_position = find_smallest_position(positive_list)
    return smallest_position

def remove_negative(l):
    l[:] = [x for x in l if x > 0]
    # print("After removing negatives: {}".format(l))
    return l

# mark as negative the elements in the list I have seen
def modify_index(l):
    for n in l:
        # print("n: {}".format(n))s
        if abs(n) - 1 < len(l) and l[abs(n) - 1] > 0:
            l[abs(n) - 1] = - l[abs(n) - 1]
    # print("After modify index: {}".format(l))
    return l

def find_smallest_position(l):
    for i, n in enumerate(l):
        if n > 0:
            # print("{} - {}".format(i,n))
            return i + 1
    return len(l) + 1

def main():
    # test_list = [3, 4, -1, 1]
    test_list = [1, 2, 0]
    # test_list = [2, 4, -8, 10, 15, 0, 0 , -1, 1]
    # test_list = [0, 0, 0]
    print(solution(test_list))

if __name__ == "__main__":
    main()