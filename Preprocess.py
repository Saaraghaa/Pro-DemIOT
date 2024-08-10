import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

class Sensor:
    def __init__(self, name):
        self.name = name
        self.frequency = 0
        self.promotion_threshold = 0.8
        self.demotion_threshold = 0.3
        self.last_promotion = 0
        self.last_demotion = 0

    def promote(self, timestamp):
        self.frequency += 1
        if self.frequency >= self.promotion_threshold * (timestamp - self.last_promotion):
            self.last_promotion = timestamp
            self.promotion_threshold *= 1.5

    def demote(self, timestamp):
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
print(df)
# Train FP-growth model
frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)
# Initialize sensors
sensors = []
for column in frequent_itemsets['itemsets']:
    print(column)
    sensors.append(Sensor(column))

