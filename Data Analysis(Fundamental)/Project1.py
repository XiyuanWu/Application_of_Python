import pandas as pd

df = pd.read_csv("180101-190630交易数据.csv",index_col="id")

df[['payment', 'price', 'cutdown_price', 'post_fee']] = df[['payment', 'price', 'cutdown_price', 'post_fee']] / 100

df['create_time'] = pd.to_datetime(df['create_time'])
df['pay_time'] = pd.to_datetime(df['pay_time'])

df.drop(index=df[df['order_id']<=0].index,inplace = True)
df.drop(index=df[df['user_id']<=0].index,inplace = True)
df.drop(index=df[df['payment']<0].index,inplace = True)
df.drop(index=df[df['price']<0].index,inplace = True)
df.drop(index=df[df['items_count']<0].index,inplace = True)
df.drop(index=df[df['cutdown_price']<0].index,inplace = True)
df.drop(index=df[df['post_fee']<0].index,inplace = True)
df.drop(index = df[df['create_time'] > df['pay_time']].index,inplace=True)

dfOrderDu = df[df['order_id'].duplicated()]
df.drop(index = dfOrderDu.index, inplace = True)
df.info()