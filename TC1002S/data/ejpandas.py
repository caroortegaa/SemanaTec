import pandas as pd

def read_pandas(filepath):
    """
    read a csv in pandas
    """

iris_df = pd.read_csv(
    filepath,
    names=['sepal_length','sepal_width','petal_length','petal_width','class'])

iris_df


with open(filepath,'r') as fp:
    data = fp.read().split('\n')

data = [f.split(',') for f in data]

iris_df_v2 = pd.DataFrame(
    data=data,
    columns=['sepal_length','sepal_width','petal_length','petal_width','class'])
     
if __name__ == "__main__":
    filepath = "./data/iris.data"
    df =read_pandas(filepath)
    print(df)
