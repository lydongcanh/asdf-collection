import pandas as pd
import os
import matplotlib.pyplot as plt

s = pd.DataFrame({'value':[x%64 for x in os.urandom(1000000)]})
s['value'].value_counts().sort_index().plot(figsize=(20,5), kind='bar')

plt.title("Number of occurrences by value")
plt.show()