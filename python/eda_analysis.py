import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')

df.head()

df.info()

df.describe(include='all')

df.isnull().sum()

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

df.isnull().sum()

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

df.columns

# create a column age_group
labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels=labels)

df[['age','age_group']].head(10)

# create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

df[['purchase_frequency_days','frequency_of_purchases']].head(10)

df[['discount_applied','promo_code_used']].head(10)

(df['discount_applied']==df['promo_code_used']).all

df=df.drop('promo_code_used',axis=1)
df.columns

pip install psycopg2-binary sqlalchemy

from sqlalchemy import create_engine

#Step 1: Connect to PostgreSQL
#Replace placeholders with your actual details
username = "postgres" #default user
password = "Rahul2003" #the password you set during installation
host = "localhost" #if running Locolly
port = "5432" #default Postgresql port
database = "customer_behavior" #the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#Step 2: Load Dataframe into PostgreSQL
table_name = "customer" #choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f" Data successfully loaded into table '{table_name}' in database '{database}'.")

# Data successfully loaded into table 'customer' in database 'customer_behavior'.
