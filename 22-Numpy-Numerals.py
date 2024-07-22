import numpy as np

# create array using range api
timeRange = np.arange(9, dtype=np.float32).reshape(3, 3)
print('Time range data : ', timeRange)

# another array, as a margin or a parameter
margin = np.array([10,10,10])
print('Add time ', np.add(timeRange, margin))

# arithmetic operations
a = np.array([0.25, 1.33, 1, 0.1, 100])
print('Reciprocal ',  np.reciprocal(a))
print('\n Subtract', np.subtract(timeRange, margin))
print('Multiply ', np.multiply(timeRange, margin))
print('Divide ', np.divide(timeRange, margin))