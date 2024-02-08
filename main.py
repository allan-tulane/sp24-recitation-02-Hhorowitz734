"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	
	if (n < b): return n #Base case -> if n < b, n // b will return 1 always, and it will continue forver

	return a * simple_work_calc(n // b, a, b) + n #Code representation of aW(n/b) + n


def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if (n < b): return n #Base case 

	return a * work_calc(n // b, a, b, f) + f(n) #Recursive call, this is aW(n/b) + f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n <= 1: return f(1) #Base case of f(1)

	return span_calc(n // b, a, b, f) + f(n) #By recursive definition of span



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result
	

def asymptotic_behavior(n_values, a, b):

    for f, label in [(lambda n: 1, 'f(n) = 1'), 
					 (lambda n: math.log(n), 'f(n) = log n'), 
					 (lambda n: n, 'f(n) = n')]: #Functions that we are comparing
		
        print(f"W(n)for {label}")

        for n in n_values:

            print(f"n={n}, W(n)={work_calc(n, a, b, f)}") #Goes over every n we're testing sends into work calc

        print()

asymptotic_behavior([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], 2, 2)