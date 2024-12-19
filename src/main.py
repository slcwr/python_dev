import os
from faker import Faker
import pandas as pd

# ディレクトリ作成
os.makedirs('data', exist_ok=True)

# Fakerインスタンスの作成
fake = Faker('ja_JP')

# ダミーデータの生成（source_data）
names = [fake.name() for _ in range(10)]

source_data = {
    '転記元列名': names,
    '条件列名': ['条件値' if i % 2 == 0 else '他の値' for i in range(10)],
    'キー列名1': [f'キー{i}' for i in range(10)]
}

# ターゲットデータの生成
target_data = {
    'A列': [fake.company() for _ in range(10)],
    'B列': [''] * 10,
    'C列': [fake.date() for _ in range(10)],
    'キー列名2': [f'キー{i}' for i in range(10)]
}

# DataFrameの作成とデータ型の明示的な設定
source_df = pd.DataFrame(source_data)
target_df = pd.DataFrame(target_data)

# データ型を明示的に文字列に設定
source_df['転記元列名'] = source_df['転記元列名'].astype(str)
target_df['B列'] = target_df['B列'].astype(str)

# 転記処理
for i, row in source_df.iterrows():
    if row['条件列名'] == '条件値':
        target_df.loc[target_df['キー列名2'] == row['キー列名1'], 'B列'] = row['転記元列名']

# ファイル保存
source_df.to_excel('data/source.xlsx', index=False)
target_df.to_excel('data/target.xlsx', index=False)
