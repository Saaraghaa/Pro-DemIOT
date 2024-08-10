import matplotlib.pyplot as plt
import numpy as np

precision = np.array([0.82, 0.79, 0.75, 0.68, 0.62, 0.56, 0.50])
recall = np.array([0.55, 0.62, 0.70, 0.78, 0.85, 0.91, 0.97])
f1_score = np.array([0.66, 0.69, 0.72, 0.72, 0.71, 0.67, 0.60])
min_support = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])

# plot the data
plt.plot(min_support, precision, label='Precision')
plt.plot(min_support, recall, label='Recall')
plt.plot(min_support, f1_score, label='F1 Score')

# add title and labels
plt.title('Performance of the Trained Model')
plt.xlabel('Minimum Support Threshold')
plt.ylabel('Performance Score')

# add legend
plt.legend()

# display the plot
plt.show()
