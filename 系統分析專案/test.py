
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, axes = plt.subplots(2, 2)

data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))

data.plot.bar(ax=axes[1,1], color='b', alpha = 0.5)
data.plot.barh(ax=axes[0,1], color='k', alpha=0.5)

plt.show()