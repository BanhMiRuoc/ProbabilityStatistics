import pandas as pd

data = pd.read_csv("iris.csv", delimiter = ',')

print(data.head(5))

x = {'sepal_length': [data.shape[0], data["sepal_length"].mean(), data["sepal_length"].std(), data["sepal_length"].min(), data["sepal_length"].max()], 'sepal_width': [data.shape[0], data["sepal_width"].mean(), data["sepal_width"].std(), data["sepal_width"].min(), data["sepal_width"].max()], 'petal_length': [data.shape[0], data["petal_length"].mean(), data["petal_length"].std(), data["petal_length"].min(), data["petal_length"].max()], 'petal_width': [data.shape[0], data["petal_width"].mean(), data["petal_width"].std(), data["petal_width"].min(), data["petal_width"].max()]}
df = pd.DataFrame(x, index=['count', 'mean', 'std', 'min', 'max'])
print(df)