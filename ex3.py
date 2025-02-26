import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the Titanic dataset
df = sns.load_dataset("titanic")

# Step 2: Create the 'family_size' feature
df['family_size'] = df['sibsp'] + df['parch'] + 1  # sibsp + parch + 1 (including the passenger)

# Step 3: One-hot encode the categorical columns 'sex' and 'embarked'
df_encoded = pd.get_dummies(df[['sex', 'embarked']], drop_first=True)

# Step 4: Scale the numerical features ('age', 'fare', 'family_size')
# We will fill missing values with the median for scaling to work correctly
df[['age', 'fare', 'family_size']] = df[['age', 'fare', 'family_size']].fillna(df[['age', 'fare', 'family_size']].median())

# Instantiate the MinMaxScaler
scaler = MinMaxScaler()

# Scale the selected columns
df[['age', 'fare', 'family_size']] = scaler.fit_transform(df[['age', 'fare', 'family_size']])

# Step 5: Combine the transformed columns with the original dataset
df_transformed = pd.concat([df, df_encoded], axis=1)

# Step 6: Drop columns that are no longer needed (e.g., 'sibsp', 'parch', 'sex', 'embarked')
df_transformed = df_transformed.drop(columns=['sibsp', 'parch', 'sex', 'embarked'])

# Display the cleaned and transformed DataFrame
print(df_transformed.head())