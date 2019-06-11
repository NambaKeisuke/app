#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
 
def Recommend(ddf, wine, weight, fruity, acidity, spicy, food=None):
    
    df = ddf.copy()
    
    #idolの作成
    idx = df.index[df["wine_name"]==wine]
    idol = df.iloc[idx, 1:5].copy()
    idol["重み"] = float(idol["重み"]) + float(weight)
    idol["果実味"] = float(idol["果実味"]) + float(fruity)
    idol["酸味"] = float(idol["酸味"]) + float(acidity)
    idol["辛み"] = float(idol["辛み"]) + float(spicy)
    #print("idol\n", idol)
    #連続変数を標準化
    _val = df.iloc[:, 1:5].values
    scaler = StandardScaler()
    _val = scaler.fit_transform(_val)
    df.iloc[:, 1:5] = _val
    #idolも標準化
    idol = scaler.transform(idol.values)
    
    #一緒に食べるものに絞る
    if food:
        food_df = df[df["食べ物"]==food].copy()
    else:
        food_df = df.copy()
    #idolに近いワインを探す
    gap_list = []
    for i in range(len(food_df)):
        gap = np.linalg.norm(food_df.iloc[i, 1:5].values-idol)
        gap_list.append(gap)
    food_df["gap"] = gap_list
    food_df = food_df.sort_values(by="gap")
    #元々のワインを候補から削除
    food_df = food_df[food_df["wine_name"]!=wine]
    
    return food_df.head(3)

def search_info(base_df, wine_df):
    base_df = base_df.rename(columns={'wine_name': 'id'})
    wine_df['id'] = wine_df['id'].astype(np.int64)
    df = pd.merge(base_df, wine_df, on='id')
    df.to_csv("test.csv", encoding='utf-8')
    return df


# ## レコメンド結果

#next_wine = Recommend(base_df, wine=0, weight=1, fruity=0, acidity=-2, spicy=-1)
#print("次に飲むべきワイン：", next_wine)
#next_wine


#next_wine = Recommend(base_df, wine=1, weight=2, fruity=0, acidity=0, spicy=0, food="たこ焼き")