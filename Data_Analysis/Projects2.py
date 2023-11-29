# 尝试下地狱难度~
# 导入pandas模块
import pandas as pd

# 读取数据
df=pd.read_csv("/Users/data5_1/train_data.csv")

# 使用replace()函数将grade列的数据的A、B、C、D、E、F、G替换为7、6、5、4、3、2、1
df["grade"] = df["grade"].replace({'A': 7, 'B': 6, 'C': 5,'D': 4, 'E': 3, 'F': 2, 'G': 1})

# 将debt列和loan列的数据用0填充
df["debt"] = df["debt"].fillna(0)
df["loan"] = df["loan"].fillna(0)

"""回归预测缺失值"""

# 从sklearn.linear_model模块导入LinearRegression函数
from sklearn.linear_model import LinearRegression

# 将不含有缺失值的"code","investment","stock","income","expenditure_1","expenditure_2","debt","loan","grade","Label"列数据单独取出，赋值为lr_data
lr_data = df[["code","investment","stock","income","expenditure_1","expenditure_2","debt","loan","grade","Label"]]

# 循环遍历每个有缺失值的列名
for i in ["capital","assets_1","assets_2","expenditure_3","tax"]:
    
    # 将i列的数据拷贝出来赋值给dfi变量
    dfi = df[i].copy()
    # 用isnull()函数判断dfi中的缺失情况，为一个布尔序列，赋值给null_index
    null_index = dfi.isnull()
    # 用~null_index索引lr_data中不含有i列缺失值的行，做为回归的训练集的自变量x
    lr_train= lr_data[~null_index]
    # 用null_index索引lr_data中含缺失值的行，做为回归的测试集的自变量x
    lr_test = lr_data[null_index]
    # 用~null_index索引df中不含缺失值的行，然后取出它们i列的数据，做为回归的训练集的因变量y
    lr_y_train = df[~null_index][i]
    # 使用LinearRegression()初始化模型，赋值给lr_model
    lr_model = LinearRegression()
    # 使用lr_model模型的fit()函数，输入此时训练集的x和y训练模型
    lr_model.fit(lr_train,lr_y_train)
    # 用lr_model模型的predict()对测试集的自变量lr_test做预测，也就是预测缺失值的值，赋值为predict
    predict = lr_model.predict(lr_test)
    # 循环遍历测试集的长度
    for j in range(len(lr_test)):
        # 将测试集索引的第j个值取出赋值为index
        index = lr_test.index[j]
        # 将dfi中index出的值设置为predict中的第j个值，此步即是在用回归预测值填补缺失值
        dfi[index] = predict[j]
    # 最后将处理完的第i列数据dfi重新赋值给df[i]列，用填充完缺失值的列覆盖原列
    df[i] = dfi


"""决策树分类"""

# 将df中的ID列和Label列用drop()删去做为决策树分类的x
x = df.drop(columns=["ID","Label"]) 
# 将df中的Label列做为决策树分类的y
y = df["Label"]

# 导入sklearn.model_selection模块中的train_test_split函数
from sklearn.model_selection import train_test_split
# 使用train_test_split()函数划分训练集和测试集，test_size=0.2,random_state=51
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=51)

# 导入sklearn.tree模块中的分类决策树模型DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
# 使用DecisionTreeClassifier()初始化模型
# 并设置参数max_depth=3,random_state=598，赋值给model
DT_model = DecisionTreeClassifier(max_depth=3,random_state=598)

# 导入sklearn.model_selection模块中的交叉验证的函数cross_val_score
from sklearn.model_selection import cross_val_score

# 使用cross_val_score()函数进行交叉验证，将结果赋值给auc_score，scoring设置为'roc_auc',cv设置为10
cross_val_auc = cross_val_score(DT_model, x_train, y_train, scoring = 'roc_auc',cv=10)

# 输出cross_val_auc的均值
print(cross_val_auc.mean())

# 用训练集拟合DT_model
DT_model.fit(x_train, y_train)

# 对测试集的x做概率预测
y_pred_proba = DT_model.predict_proba(x_test)

"""输出AUC"""

# 导入sklearn.metrics模块中的roc_auc_score函数
from sklearn.metrics import roc_auc_score

# 将y_test和预测的概率传入roc_auc_score()，将结果赋值给auc
auc = roc_auc_score(y_test, y_pred_proba[:,1])

# 输出auc
print(auc)