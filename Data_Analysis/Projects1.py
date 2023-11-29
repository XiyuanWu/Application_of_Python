'''一、 读取文件并划分数据集'''
# 导入pandas模块，简写成pd
import pandas as pd
# 导入matplotlib库中的pyplot包，简写成plt
import matplotlib.pyplot as plt

# 读取路径为/Users/forecast/jetrail.csv的文件，赋值给变量df
df = pd.read_csv("/Users/forecast/jetrail.csv")

# 使用to_datetime函数将df中Datetime列数据转化为时间格式，赋值给df["Datetime"]
df["Datetime"] = pd.to_datetime(df["Datetime"]) 
# 使用set_index函数将Datetime列设为行索引，并对原DataFrame df生效
df.set_index(["Datetime"],inplace=True)

# 划分训练集和测试集
# df中10000-17552行数据为训练集，赋值给变量train
train = df.iloc[10000:17553]
# df中17553-最后一行数据为测试集，赋值给变量test
test = df.iloc[17553:]

# 使用resample()函数按天聚合数据，并通过.mean()函数计算均值，赋值给变量df
df = df.resample("D").mean()
# 使用resample()函数按天聚合数据，并通过.mean()函数计算均值，赋值给变量train
train = train.resample("D").mean()
# 使用resample()函数按天聚合数据，并通过.mean()函数计算均值，赋值给变量test
test = test.resample("D").mean()

# 使用copy()函数，将test数据复制给变量y_hat_avg
y_hat_avg = test.copy()

'''二、 直接均值法'''
# 使用mean()函数计算train中Count列的均值，赋值给y_hat_avg["avg_forecast"]
y_hat_avg["avg_forecast"] = train["Count"].mean()

'''三、 移动均值法（10日移动均值）'''
# 将train["Count"].copy()赋值给新变量train_series
train_series = train["Count"].copy()

# 定义一个空列表result，用于存储预测结果
result = []

# for循环遍历y_hat_avg.index
for i in y_hat_avg.index:
    
    # 用rolling()函数求train_series的移动平均值，聚合函数用mean()，将移动平均值的最后一个值赋值给变量
    predict = train_series.rolling(window=10).mean()[-1]
    
    # 将predict赋值给train_series[i]
    train_series[i] = predict
    
    # 使用append()函数，将predict添加到result中
    result.append(predict)
    
'''四、结果可视化'''
# 使用plot()函数画出训练集折线图
# X轴数据为train.index，Y轴数据为train["Count"]，颜色为blue，label为train
plt.plot(train.index, train["Count"],color="blue",label="train")

# 使用plot()函数画出测试集折线图
# X轴数据为test.index，Y轴数据为test["Count"]，颜色为orange，label为test
plt.plot(test.index, test["Count"],color="gray",label="test")

# 使用plot()函数画出直接均值法预测折线图
# 轴数据为y_hat_avg.index，Y轴数据为y_hat_avg["avg_forecast"]
# 颜色为red，label为Average Forecast
plt.plot(y_hat_avg.index,y_hat_avg["avg_forecast"],color="red",label="Average Forecast")

# 使用plot()函数画出移动均值法预测折线图
# X轴数据为y_hat_avg.index，Y轴数据为y_hat_avg["moving_avg_forecast"]
# 颜色为green，label为Moving Average Forecast
plt.plot(y_hat_avg.index,result,color="green",label="Moving Average Forecast")

# 使用legend()函数显示图例
plt.legend()

# 使用show()函数显示图片
plt.show()
