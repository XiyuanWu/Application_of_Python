import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/forecast/jetrail.csv")

df["Datetime"] = pd.to_datetime(df["Datetime"]) 
df.set_index(["Datetime"], inplace=True)

train = df.iloc[10000:17553]
test = df.iloc[17553:]

df = df.resample("D").mean()
train = train.resample("D").mean()
test = test.resample("D").mean()

y_hat_avg = test.copy()

y_hat_avg["avg_forecast"] = train["Count"].mean()

train_series = train["Count"].copy()

result = []

for i in y_hat_avg.index:
    predict = train_series.rolling(window=10).mean()[-1]
    train_series[i] = predict
    result.append(predict)

plt.plot(train.index, train["Count"], color="blue", label="train")
plt.plot(test.index, test["Count"], color="gray", label="test")
plt.plot(y_hat_avg.index, y_hat_avg["avg_forecast"], color="red", label="Average Forecast")
plt.plot(y_hat_avg.index, result, color="green", label="Moving Average Forecast")

plt.legend()
plt.show()
