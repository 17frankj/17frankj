import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Save DataFrame as an image
df.to_string(buf=open('output.txt', 'w'))

# Save Plot as an image
df.plot(kind='bar')
plt.savefig('output.png')
