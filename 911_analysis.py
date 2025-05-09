import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
ds = pd.read_csv('C:/Users/TAHIR/Downloads/911.csv')

# 1. Top 10 zipcodes with the most 911 calls
top_zip = ds['zip'].value_counts().head(10)
print("Top ZipCodes:\n", top_zip)
print("Is Zipcode 19446 present?", 19446 in ds['zip'].values)
print("Is Zipcode 19090 present?", 19090 in ds['zip'].values)

# 2. Top 4 townships and check for specific ones
top_twp = ds['twp'].value_counts().head(4)
print("\nTop Townships:\n", top_twp)
print("Is LOWER POTTSGROVE not present?", "LOWER POTTSGROVE" not in ds['twp'].values)
print("Is NORRISTOWN not present?", "NORRISTOWN" not in ds['twp'].values)
print("Is HORSHAM not present?", "HORSHAM" not in ds['twp'].values)
print("Is ABINGTON not present?", "ABINGTON" not in ds['twp'].values)

# 3. Extract the reason for 911 call from the title
ds['Reason'] = ds['title'].str.split(':').str[0]
reasons = ds['Reason'].value_counts()
print("\nCall Reasons:\n", reasons)

# Set up subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 4. Bar chart for call reasons
reasons.plot(kind='barh', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('911 Calls by Reason')
axes[0, 0].set_xlabel('Number of Calls')
axes[0, 0].set_ylabel('Reason')

# 5. Convert timestamps and extract day/month info
ds['timeStamp'] = pd.to_datetime(ds['timeStamp'])
ds['Day of Week'] = ds['timeStamp'].dt.day_name()
ds['Month'] = ds['timeStamp'].dt.month_name()

# Heatmap of 911 calls by day and reason
calls = ds.groupby(['Day of Week', 'Reason']).size().unstack()
sns.heatmap(data=calls, cmap='Greens', annot=True, fmt='d', ax=axes[0, 1])
axes[0, 1].set_title('911 Calls by Day and Reason')
axes[0, 1].set_xlabel('Reason')
axes[0, 1].set_ylabel('Day of Week')

# 6. Countplot of Day of Week with hue by Reason
sns.countplot(data=ds, x='Day of Week', hue='Reason', ax=axes[1, 0])
axes[1, 0].set_title('911 Calls by Day and Reason')
axes[1, 0].set_xlabel('Day of Week')
axes[1, 0].set_ylabel('Number of Calls')
axes[1, 0].set_xticklabels([label.get_text()[:3] for label in axes[1, 0].get_xticklabels()])

# 7. Countplot of Month with hue by Reason
sns.countplot(data=ds, x='Month', hue='Reason', palette="Set2", ax=axes[1, 1])
axes[1, 1].set_title('911 Calls by Month and Reason')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Number of Calls')
axes[1, 1].set_xticklabels([label.get_text()[:3] for label in axes[1, 1].get_xticklabels()])

# Make fonts smaller to reduce clutter
for ax in axes.flat:
    for label in ax.get_xticklabels():
        label.set_fontsize(8)

plt.tight_layout(pad=2.0)
plt.subplots_adjust(hspace=0.4)
plt.show()
