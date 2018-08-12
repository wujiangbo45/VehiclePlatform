import numpy as np
import pandas as pd

if __name__ == '__main__':
	# 构造4*4矩阵，行 a b c d,列 w x y z
	data = pd.DataFrame(np.arange(16).reshape(4,4),columns=list('wxyz'))
	'''
	# print(data)
	#     w   x   y   z
	# a   0   1   2   3
	# b   4   5   6   7
	# c   8   9  10  11
	# d  12  13  14  15
	'''
	
	ser = pd.Series(np.arange(3))

	# print(ser)
	'''
	a     0
	b     4
	c     8
	d    12
	'''
	# data.w 返回Series类型
	# data['w']
	'''
	a     0
	b     4
	c     8
	d    12
	Name: w, dtype: int64


	data['w'] > 0
	a    False
	b     True
	c     True
	d     True


	data[data['w'] > 0]
	    w   x   y   z
	b   4   5   6   7
	c   8   9  10  11
	d  12  13  14  15

	'''
	print(data[data['w']>0])
	data = data.set_index('z',drop=False)
	data_w_series = data['w']
	print(data)
	print(data_w_series[1:].values - data_w_series[:-1].values)
	print(data_w_series[1:].index.values - data_w_series[:-1].index.values)
	z = zip(data_w_series.index[:-1], data_w_series.index[1:])
	tz = zip([1,2,3,4],[4,3,2,1])
	print([1,2,3,4][0:-1])
	# print([s:e for s,e in z])