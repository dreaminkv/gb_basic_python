import pandas as pd

# with open('test_crv.py', 'r', encoding='utf-8') as f:
#     data = f.readlines()

data = pd.read_csv('train.csv')
print(data)
print(data['Survived'])