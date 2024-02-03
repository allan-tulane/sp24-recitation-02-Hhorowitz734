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
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

	#UNCOMMENT THE BELOW ---- THEY ARE PART OF LAB WORK
    #res = compare_work(work_fn1, work_fn2)
	#print(res)
	pass

	
def test_compare_span():
	# TODO
	pass
