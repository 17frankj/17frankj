import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'Reason\'s to hire me': [1000],
    'Reason\'s not to hire me': [-1000]
})

# Save DataFrame as an image
df.to_string(buf=open('output.txt', 'w'))

# Save Plot as an image
df.plot(kind='bar')
plt.savefig('output.png')