import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Company = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
revenue = [140, 212, 230, 170, 189, 210, 211, 134, 219, 151, 121, 156, 185, 212, 134, 178, 115, 212, 190, 155]
print(revenue)

ypo = np.arange(len(Company))
print(ypo)

plt.xlabel('COMPANIES')
plt.ylabel('REVENUE IN LACkS')
plt.title('TECH STOCKS')
plt.bar(Company, revenue)

# MODE
print('Mode:', stats.mode(revenue))

# MEDIAN
revenue.sort()
print('sorted revenue: ', revenue)
print('Median:', np.median(revenue))

# MEAN
print('Mean:', np.mean(revenue))
