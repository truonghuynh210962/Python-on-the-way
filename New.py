import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.DataFrame({'a':[1,2,3],'b':[1,2,3]})
print(dataset)

sns.barplot(x ='a', y = 'b',data = dataset)
plt.show()

print(1,2)