import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
df = sns.load_dataset("titanic")
df['family_size'] = df['sibsp'] + df['parch'] + 1  # sibsp + parch + 1 (including the passenger)
df_encoded = pd.get_dummies(df[['sex', 'embarked']], drop_first=True)
df[['age', 'fare', 'family_size']] = df[['age', 'fare', 'family_size']].fillna(df[['age', 'fare', 'family_size']].median())
scaler = MinMaxScaler()
df[['age', 'fare', 'family_size']] = scaler.fit_transform(df[['age', 'fare', 'family_size']])

df_transformed = pd.concat([df, df_encoded], axis=1)

df_transformed = df_transformed.drop(columns=['sibsp', 'parch', 'sex', 'embarked'])

print(df_transformed.head())