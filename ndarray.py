import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=100)

# Create a box plot
plt.boxplot(data)

# Set labels and title
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Box Plot')

# Display the plot
plt.show()