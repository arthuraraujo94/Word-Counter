import pandas as pd
df = pd.read_csv('https://s3.amazonaws.com/projetobrumadinho/log.csv').sample(1000, random_state=42)
df.sentiment.value_counts()
df.head()