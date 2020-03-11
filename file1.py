import numpy as np

def init_array(LEN):
	return np.zeros(LEN)
	
def create_key(LEN, seed, mod):
	arr = init_array(LEN)
	myseed = seed
	for it in range(LEN):
		arr[it] = myseed
		myseed = myseed + seed
		myseed = myseed % mod
	return arr

def visualise_array(array):
	print(array)



