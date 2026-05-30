
# 1. 加载数据
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target
print(X.shape, y.shape)
print(X)
print(y)

# 2. 划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 选择并训练模型
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 4. 模型预测与评估
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print(f"模型准确率: {accuracy_score(y_test, y_pred):.2f}")