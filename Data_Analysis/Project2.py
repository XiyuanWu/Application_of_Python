import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import roc_auc_score

df = pd.read_csv("/Users/data5_1/train_data.csv")

df["grade"] = df["grade"].replace({'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1})

df["debt"] = df["debt"].fillna(0)
df["loan"] = df["loan"].fillna(0)

lr_data = df[["code", "investment", "stock", "income", "expenditure_1", "expenditure_2", "debt", "loan", "grade", "Label"]]

for i in ["capital", "assets_1", "assets_2", "expenditure_3", "tax"]:
    dfi = df[i].copy()
    null_index = dfi.isnull()
    lr_train = lr_data[~null_index]
    lr_test = lr_data[null_index]
    lr_y_train = df[~null_index][i]
    lr_model = LinearRegression()
    lr_model.fit(lr_train, lr_y_train)
    predict = lr_model.predict(lr_test)
    for j in range(len(lr_test)):
        index = lr_test.index[j]
        dfi[index] = predict[j]
    df[i] = dfi

x = df.drop(columns=["ID", "Label"])
y = df["Label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=51)

DT_model = DecisionTreeClassifier(max_depth=3, random_state=598)

cross_val_auc = cross_val_score(DT_model, x_train, y_train, scoring='roc_auc', cv=10)

print(cross_val_auc.mean())

DT_model.fit(x_train, y_train)

y_pred_proba = DT_model.predict_proba(x_test)

auc = roc_auc_score(y_test, y_pred_proba[:, 1])

print(auc)
