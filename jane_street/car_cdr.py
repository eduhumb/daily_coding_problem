'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a,b):
	def pair(f):
		return f(a, b)
	return pair	

# Content of the Address part of the Register number
def car(pair):
	def first_element(a, b):
		return a
	return pair(first_element)

# Content of the Decrement part of the Register number
def cdr(pair):
	def last_element(a, b):
		return b
	return pair(last_element)

def main():
	pair = cons(2,3)

	print('calling pair = cons(2,3)...')
	print('calling car(pair)...')
	print(car(pair))
	print('calling cdr(pair)...')
	print(cdr(pair))

if __name__ == "__main__":
	main()