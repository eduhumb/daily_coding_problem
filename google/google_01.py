'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

import random
from itertools import combinations

'''
Space complexity: O(n²)
Time complexity: O(n²)
'''
def solution_1(l,k):

	for i in range(len(l)):
		for j in range(len(l)-1):
			if l[i] + l[j] == k:
				return True

	return False

'''
Space complexity: O(n²)
Time complexity: O(n)
'''
def solution_2(l,k):

	seen = set()
	for i in l:
		if (k-i) in seen:
			return True
		else:
			seen.add(i)

	return False

'''
Space complexity: O(n)
Time complexity: O(n!)
'''
def solution_3(l,k):
	return any(((i + j) == k) for i, j in combinations(l, 2))

def main():
	test_list = random.sample(range(20), 5)
	k = random.randint(10,30)

	print("The list is {} and the k is {}".format(test_list, k))
	print("Solution 1: {}".format(solution_1(test_list,k)))
	print("Solution 2: {}".format(solution_2(test_list,k)))
	print("Solution 3: {}".format(solution_3(test_list,k)))

if __name__ == '__main__':
	main()