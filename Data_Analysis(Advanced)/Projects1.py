import pandas as pd

data = pd.read_csv("/Users/huanhuan/bilibili.csv")

count = data.groupby("author").count()
count = count["分区"].reset_index()
count.columns = ["author","times"]
com = pd.merge(count,data,on="author",how="inner")
com["date"] = pd.to_datetime(com["date"])
result = com[com["times"] >= 5]

'''Calculate IFL'''
# 1. Calculate I
groupByAuthor = result.groupby("author").sum()
danmu = groupByAuthor["danmu"]
reply = groupByAuthor["reply"]
view =groupByAuthor["view"]
count = result.groupby("author")["times"].count()
# Formula of I 
I = ((danmu+reply)/view/count*100)

# 2. Calculate F
latest = result.groupby("author")["date"].max()
earliest = result.groupby("author")["date"].min()
# Formula of F
F = ((latest-earliest).dt.days/count)

# 3. Calculate L
likes = groupByAuthor["likes"]
coins = groupByAuthor["coins"]
favorite = groupByAuthor["favorite"]
# Formula of L
L = ((likes+coins+favorite)/view*100)

# 4. Combine
IFL = pd.concat([I,F,L], axis=1)
IFL.columns = ["I","F","L"]

'''Mark layering'''

IFL['I_score'] = pd.qcut(IFL['I'],q=5,labels = [1,2,3,4,5])
IFL['F_score'] = pd.qcut(IFL['F'],q=5,labels = [5,4,3,2,1])
IFL['L_score'] = pd.qcut(IFL['L'],q=5,labels = [1,2,3,4,5])


def rfmTrans(x):
    if x > 3:
        return 1
    else:
        return 0

IFL["I_score"] = IFL["I_score"].apply(rfmTrans)
IFL["F_score"] = IFL["F_score"].apply(rfmTrans)
IFL["L_score"] = IFL["L_score"].apply(rfmTrans)


IFL["mark"] = IFL["I_score"].astype(str) + IFL["F_score"].astype(str) + IFL["L_score"].astype(str)

# Convert to corresponding user stratification
def rfmType(x):     
    if x == "111":
        return "高质量UP主"
    elif x == "101":
        return "高质量拖更UP主"
    elif x == "011":
        return "高质量内容高深UP主"
    elif x == "001":
        return "高质量内容高深拖更UP主"
    elif x == "110":
        return "接地气活跃UP主"
    elif x == "100":
        return "接地气UP主"
    elif x == "010":
        return "活跃UP主"
    else:
        return "还在成长的UP主"


IFL["up_type"] = IFL["mark"].apply(rfmType)


up_type = IFL["up_type"].groupby(IFL["up_type"]).count()
up_type = up_type / up_type.sum()

'''Visualization'''
import matplotlib.pyplot as plt

plt.bar(up_type.index, up_type.values)
plt.xticks(rotation=45)
plt.show()
