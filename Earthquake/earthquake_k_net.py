# -*- coding: utf-8 -*-
"""Earthquake_k_Net

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hUN2lbQoFdDYYConj2b5B23-Ih4p_rr0

## Drive Mount
"""

from google.colab import drive
drive.mount('/content/drive')

"""## K_Net_Tc_Pd Record"""

import pandas as pd

file_paths = ['/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1996.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1997.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1998.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1999.csv'
              ]

filenames = []
record_counts = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    filenames.append(file_path.split('/')[-1])
    record_counts.append(len(df))
record_info_df = pd.DataFrame({'Filename': filenames, 'Record Count': record_counts})
print(record_info_df)

"""## UD file Records"""

import os

root_dir = "/content/drive/MyDrive/Earthquake_K_Net"

year_file_count = {}

for year_folder in os.listdir(root_dir):
    year_folder_path = os.path.join(root_dir, year_folder)
    if os.path.isdir(year_folder_path):
        year_count = 0
        for knt_folder in os.listdir(year_folder_path):
            knt_folder_path = os.path.join(year_folder_path, knt_folder)
            if os.path.isdir(knt_folder_path):
                # Count .UD files in each .knt folder
                ud_files = [f for f in os.listdir(knt_folder_path) if f.endswith('.UD')]
                year_count += len(ud_files)
        year_file_count[year_folder] = year_count        # Store the count for this year


year_file_count_df = pd.DataFrame.from_dict(year_file_count, orient='index', columns=['Number of .UD Files'])

print(year_file_count_df)

"""##CSV File record > .UD File Record"""

final_table = pd.merge(record_info_df, year_file_count_df, left_on='Year', right_index=True, how='outer')

# Fill NaN values with 0
final_table.fillna(0, inplace=True)

final_table = final_table[['Year', 'Record Count', 'Number of .UD Files']]

print(final_table)

import pandas as pd
import os

def preprocess_csv(file_path):
    df = pd.read_csv(file_path)
    df = df[df['pick_index_manually'] >= 100]
    processed_folder = "/content/drive/MyDrive/processed_data"
    os.makedirs(processed_folder, exist_ok=True)  # Create the folder if it doesn't exist
    processed_file_path = os.path.join(processed_folder, os.path.basename(file_path))
    df.to_csv(processed_file_path, index=False)
    print(f"Processed file saved at: {processed_file_path}")

file_paths = ['/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1996.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1997.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1998.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_1999.csv']

for file_path in file_paths:
    preprocess_csv(file_path)

import pandas as pd
import os
def preprocess_and_count_records(file_path):
    df = pd.read_csv(file_path)
    total_records = len(df)
    processed_df = df[df['pick_index_manually'] >= 100]
    processed_records = len(processed_df)

    return total_records, processed_records

records_info = []
for file_path in file_paths:
    year = file_path.split('_')[-1].split('.')[0]  # Extract year from file path
    total_records, processed_records = preprocess_and_count_records(file_path)
    records_info.append({'Year': year, 'Total Records': total_records, 'Processed Records': processed_records})
records_info_df = pd.DataFrame(records_info)
print(records_info_df)

merged_table = pd.merge(records_info_df, year_file_count_df, left_on='Year', right_index=True, how='left')
merged_table['Number of .UD Files'].fillna(0, inplace=True)
merged_table = merged_table[['Year', 'Total Records', 'Number of .UD Files', 'Processed Records']]
print(merged_table)

import os
import pandas as pd

root_dir = "/content/drive/MyDrive/Earthquake_K_Net"

for year_folder in os.listdir(root_dir):
    year_folder_path = os.path.join(root_dir, year_folder)
    if os.path.isdir(year_folder_path):
        ud_files = []  # List to store names of .UD files
        for knt_folder in os.listdir(year_folder_path):
            knt_folder_path = os.path.join(year_folder_path, knt_folder)
            if os.path.isdir(knt_folder_path):
                ud_files.extend([f for f in os.listdir(knt_folder_path) if f.endswith('.UD')])
        ud_files_df = pd.DataFrame(ud_files, columns=['UD File Name'])
        csv_file_path = os.path.join(root_dir, f'{year_folder}_UD_files.csv')
        ud_files_df.to_csv(csv_file_path, index=False)
        print(f"CSV file saved for {year_folder}: {csv_file_path}")

import pandas as pd
import os

# Paths
root_files = ['/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_2000.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_2001.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/KNet_Tc_Pd_ManuallyPlusKalkan_2002.csv',
              ]

ud_files_csvs = ['/content/drive/MyDrive/Earthquake_K_Net/2000_UD_files.csv',
                 '/content/drive/MyDrive/Earthquake_K_Net/2001_UD_files.csv',
                 '/content/drive/MyDrive/Earthquake_K_Net/2002_UD_files.csv',
                 ]

matched_data_folder = "/content/drive/MyDrive/Earthquake_K_Net/matched_data"
os.makedirs(matched_data_folder, exist_ok=True)  # Create the folder if it doesn't exist

def retrieve_matching_records(root_file, ud_files_csv):
    root_df = pd.read_csv(root_file)
    ud_df = pd.read_csv(ud_files_csv)
    matched_records_df = root_df[root_df['records name'].isin(ud_df['UD File Name'])]
    return matched_records_df
for root_file, ud_files_csv in zip(root_files, ud_files_csvs):
    matched_records_df = retrieve_matching_records(root_file, ud_files_csv)
    matched_data_file = os.path.join(matched_data_folder, os.path.basename(root_file).replace(".csv", "_matched.csv"))
    matched_records_df.to_csv(matched_data_file, index=False)
    print(f"Matched data saved for {os.path.basename(root_file)}: {matched_data_file}")

import os
import pandas as pd
matched_data_folder = "/content/drive/MyDrive/Earthquake_K_Net/matched_data"
matched_record_counts = {}
for filename in os.listdir(matched_data_folder):
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(matched_data_folder, filename))
        record_count = len(df)
        matched_record_counts[filename] = record_count
matched_record_counts_df = pd.DataFrame.from_dict(matched_record_counts, orient="index", columns=["Record Count"])
print(matched_record_counts_df)

merged_table = pd.merge(merged_table, matched_record_counts_df, left_on='Year', right_index=True, how='left')
merged_table['Record Count'].fillna(0, inplace=True)
print(merged_table)

import pandas as pd
import os

def preprocess_csv(file_path):
    df = pd.read_csv(file_path)
    df = df[df['pick_index_manually'] >= 100]
    processed_folder = "/content/drive/MyDrive/Final_processed_data"
    os.makedirs(processed_folder, exist_ok=True)  # Create the folder if it doesn't exist
    processed_file_path = os.path.join(processed_folder, os.path.basename(file_path))
    df.to_csv(processed_file_path, index=False)
    print(f"Processed file saved at: {processed_file_path}")

matched_paths = ['/content/drive/MyDrive/Earthquake_K_Net/matched_data/KNet_Tc_Pd_ManuallyPlusKalkan_2000_matched.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/matched_data/KNet_Tc_Pd_ManuallyPlusKalkan_2001_matched.csv',
              '/content/drive/MyDrive/Earthquake_K_Net/matched_data/KNet_Tc_Pd_ManuallyPlusKalkan_2002_matched.csv',
              ]

for file_path in matched_paths:
    preprocess_csv(file_path)

"""# Single DataFrame
### Train & Test dataset
"""

import pandas as pd

# List of file paths for year-wise CSV files
file_paths = [
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_1996_matched.csv",
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_1997_matched.csv",
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_1998_matched.csv",
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_1999_matched.csv",
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_2000_matched.csv",
    "/content/drive/MyDrive/Final_processed_data/KNet_Tc_Pd_ManuallyPlusKalkan_2002_matched.csv",

]

dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

train_df = combined_df.sample(frac=0.8, random_state=42)  # 80% for training
test_df = combined_df.drop(train_df.index)  # Remaining 20% for testing

# Print shapes of training and testing sets
print("Training set shape:", train_df.shape)
print("Testing set shape:", test_df.shape)

print("Column Names:")                           # Display column names
print(train_df.columns)

print("\nSummary Statistics:")                   # Display summary statistics of numerical features

print(train_df.describe())

print("\nInformation:")                          # Display information about non-null values and data types of features
print(train_df.info())

"""### Visualizing Records on Train & Test"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))

# Plot (a) Mag vs Epicentral Distance
sns.scatterplot(data=train_df, x='epi_dist', y='mag', color='green', label='Training', ax=axes[0])
sns.scatterplot(data=test_df, x='epi_dist', y='mag', color='blue', label='Testing', ax=axes[0])
axes[0].set_title("Distribution of Earthquake Magnitude vs. Epicentral Distance")
axes[0].set_xlabel("Epicentral Distance")
axes[0].set_ylabel("Magnitude")
axes[0].legend()

# Plot (b) Epicentral Distance vs Records
sns.histplot(train_df['epi_dist'], color='green', label='Training', ax=axes[1])
sns.histplot(test_df['epi_dist'], color='blue', label='Testing', ax=axes[1])
axes[1].set_title("Distribution of Earthquake Records vs. Epicentral Distance")
axes[1].set_xlabel("Epicentral Distance")
axes[1].set_ylabel("Count")
axes[1].legend()

# Plot (c) Magnitude vs Records
sns.histplot(train_df['mag'], color='green', label='Training', ax=axes[2])
sns.histplot(test_df['mag'], color='blue', label='Testing', ax=axes[2])
axes[2].set_title("Distribution of Earthquake Records vs. Magnitude")
axes[2].set_xlabel("Magnitude")
axes[2].set_ylabel("Count")
axes[2].legend()

plt.tight_layout()
plt.show()

import pandas as pd

#data = pd.read_csv("your_data.csv")  # Replace "your_data.csv" with the path to your CSV file

numerical_features = combined_df.select_dtypes(include=['float64', 'int64'])

correlation_matrix_pearson = numerical_features.corr(method='pearson')

correlation_matrix_spearman = numerical_features.corr(method='spearman')

# Print correlation matrix for Pearson method
print("Correlation Matrix (Pearson):")
print(correlation_matrix_pearson)

# Print correlation matrix for Spearman method
print("\nCorrelation Matrix (Spearman):")
print(correlation_matrix_spearman)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

numerical_features = combined_df.select_dtypes(include=['float64', 'int64'])
X = numerical_features.drop(columns=['mag'])  # Features
y = numerical_features['mag']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

feature_importances = rf_model.feature_importances_
plt.figure(figsize=(10, 8))
sorted_indices = feature_importances.argsort()[::-1]
feature_names = X.columns
plt.barh(X.columns, feature_importances)
plt.xlabel('Feature Importance Score ')
plt.ylabel('Features')
plt.title('Feature Importance Scores by Random Forest')
plt.show()

from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

numerical_features = combined_df.select_dtypes(include=['float64', 'int64'])
X = numerical_features.drop(columns=['mag'])  # Features
y = numerical_features['mag']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
gb_regressor = GradientBoostingRegressor()
gb_regressor.fit(X, y)

feature_importances = gb_regressor.feature_importances_
sorted_indices = feature_importances.argsort()[::-1]
feature_names = X.columns
plt.figure(figsize=(10, 8))
plt.bar(range(len(feature_importances)), feature_importances[sorted_indices], align='center')
plt.xticks(range(len(feature_importances)), feature_names[sorted_indices], rotation=90)
plt.xlabel('Features')
plt.ylabel('Importance Score')
plt.title('Feature Importance by Gradient Boosting Regressor')
plt.show()

