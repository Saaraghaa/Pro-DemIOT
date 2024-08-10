import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime

class Sensor:
    def __init__(self, name, frequency=0, promotion_threshold=0.8, demotion_threshold=0.3, last_promotion=0, last_demotion=0):
        """
        Initialize Sensor object with specified attributes.

        Parameters:
        - name: str, name of the sensor
        - frequency: int, frequency of sensor readings
        - promotion_threshold: float, threshold for promotion
        - demotion_threshold: float, threshold for demotion
        - last_promotion: float, timestamp of last promotion
        - last_demotion: float, timestamp of last demotion
        """
        self.name = name
        self.frequency = frequency
        self.promotion_threshold = promotion_threshold
        self.demotion_threshold = demotion_threshold
        self.last_promotion = last_promotion
        self.last_demotion = last_demotion

    def promote(self, timestamp):
        """
        Promote sensor based on frequency and time elapsed since last promotion.

        Parameters:
        - timestamp: float, current timestamp
        """
        self.frequency += 1
        if self.frequency >= self.promotion_threshold * (timestamp - self.last_promotion):
            self.last_promotion = timestamp
            self.promotion_threshold *= 1.5

    def demote(self, timestamp):
        """
        Demote sensor based on frequency and time elapsed since last demotion.

        Parameters:
        - timestamp: float, current timestamp
        """
        if self.frequency < self.demotion_threshold * (timestamp - self.last_demotion):
            self.last_demotion = timestamp
            self.promotion_threshold /= 1.5

    def __str__(self):
        return self.name

# Load data
data = pd.read_csv('iot_sensors_data.csv')

# Preprocess data
te = TransactionEncoder()
te_ary = te.fit(data.values).transform(data.values)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Binarize the data
df = df.astype(bool)

# Train FP-growth model
frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)

# Additional data processing
# Perform clustering using KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans.fit_predict(df)
df['cluster'] = cluster_labels

# Initialize sensors
sensors = []
for column in frequent_itemsets['itemsets']:
    print(column)
    timestamp = datetime.now().timestamp()
    sensors.append(Sensor(column, last_promotion=timestamp, last_demotion=timestamp))
