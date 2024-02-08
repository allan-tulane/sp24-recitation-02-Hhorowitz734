from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(6, 3, 3) == 12
	assert simple_work_calc(10, 2, 5) == 14

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(15, 4, 2, lambda n: 2*n) == 246
	assert work_calc(25, 1, 5, lambda n: 5) == 11
	assert work_calc(12, 2, 3, lambda n: n**2) == 180



def test_compare_work():

	a = 2
	b = 2

	#log_2(2) = 1
	#0.5 < 1 < 2, so we will go with these vlues

	work_fn1 = lambda n: work_calc(n, a, b, lambda n: n**0.5)
	work_fn2 = lambda n: work_calc(n, a, b, lambda n: n**2)

	res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():

	b = 2
	a = 2

	span_fn1 = lambda n: span_calc(n, a, b, lambda n: n**0.5)
	span_fn2 = lambda n: span_calc(n, a, b, lambda n: n**2)

	res = compare_span(span_fn1, span_fn2)

	print(res)


'''
test_compare_span()
[(10, 7.812559200041264, 130), 
(20, 12.284695155040843, 530), 
(50, 20.716709977355286, 3315), 
(100, 30.716709977355286, 13315), 
(1000, 103.66774226670526, 1333214), 
(5000, 238.06940627807464, 33332873), 
(10000, 338.06940627807467, 133332873)]


test_compare_work()
[(10, 21.291267864660337, 174),
(20, 47.054671684320255, 748), 
(50, 110.23620513578395, 4790), 
(100, 230.4724102715679, 19580), 
(1000, 2075.117102760963, 1990744), 
(5000, 14251.20819850244, 49957880), 
(10000, 28602.41639700488, 199915760)]
'''
