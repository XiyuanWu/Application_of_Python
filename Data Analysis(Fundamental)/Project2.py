import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("/Users/binbin/avocado.csv")

data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")

groupByRegion = data.groupby(["region", pd.Grouper(freq="M")]).mean()

NewYork_AveragePrice = groupByRegion.loc["NewYork"]
Chicago_AveragePrice = groupByRegion.loc["Chicago"]

plt.plot(NewYork_AveragePrice.index, NewYork_AveragePrice["AveragePrice"], marker="o", color="skyblue", label="纽约价格水平")
plt.plot(Chicago_AveragePrice.index, Chicago_AveragePrice["AveragePrice"], marker="o", color="blue", label="芝加哥价格水平")

TotalUS_AveragePrice = data.groupby(pd.Grouper(freq="M")).mean()

plt.plot(TotalUS_AveragePrice.index, TotalUS_AveragePrice["AveragePrice"], marker="o", color="green", label="全美价格水平")

plt.xlabel("时间")
plt.ylabel("价格水平")

plt.legend(loc="upper left")
plt.show()
