import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load example dataset
tips = sns.load_dataset("tips")

# Prepare data for the bar chart (average total bill by day)
avg_bill = tips.groupby('day')['total_bill'].mean().reset_index()

# Prepare data for the line chart (average tip by day)
avg_tip = tips.groupby('day')['tip'].mean().reset_index()

# Start plotting
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Create bar chart
bar = sns.barplot(x='day', y='total_bill', data=avg_bill, color='lightblue', label='Average Total Bill')

# Create line chart
line = sns.lineplot(x='day', y='tip', data=avg_tip, sort=False, marker='o', color='red', label='Average Tip')

# Adding legend
plt.legend()

# Show the plot
plt.show()
