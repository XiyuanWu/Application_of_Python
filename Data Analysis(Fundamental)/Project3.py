import pandas as pd
import matplotlib.pyplot as plt

df2019 = pd.read_csv("/Users/Lily/2019年下半年订单表.csv")
df2020 = pd.read_csv("/Users/Lily/2020年上半年订单表.csv")

dfYear = pd.concat([df2019, df2020])
dfYear["下单时间"] = pd.to_datetime(dfYear["下单时间"])

dfnewYear = dfYear.set_index("下单时间")
dfSales = dfnewYear["数量"].groupby(dfnewYear["商品ID"]).resample("M").sum()
dfnewSales = dfSales.reset_index()
dfnewSales["下单时间"] = dfnewSales["下单时间"].dt.strftime("%Y-%m")

dfEV = pd.read_csv("/Users/Lily/Exposure.csv")
dfTotal = pd.merge(dfEV, dfnewSales, left_on=["ID", "Month"], right_on=["商品ID", "下单时间"])
dfTotal["购买转化率"] = dfTotal["数量"] / dfTotal["Exposure"]
groupbyID = dfTotal.groupby(dfTotal["ID"]).count()
ID = groupbyID.index


for i in range(len(ID)):
    plt.subplot(2, 3, i+1)
    df1 = dfTotal[dfTotal["ID"] == ID[i]]

    plt.plot(df1["Month"], df1["购买转化率"].round(2), marker="o", label="转化率")
    plt.xticks(rotation=90)
    plt.ylim(0, 0.3)
    plt.legend()
    plt.title(ID[i])

plt.tight_layout()
plt.show()
