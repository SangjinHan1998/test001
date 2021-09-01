a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 411
print(a)
print(b)