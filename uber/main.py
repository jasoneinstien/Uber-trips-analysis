import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("data/uber.csv")
data = data.head(10000)

data["Date/Time"] = data["Date/Time"].map(pd.to_datetime)

data["Day"] = data["Date/Time"].apply(lambda x: x.day)
data["Weekday"] = data["Date/Time"].apply(lambda x: x.weekday())
data["Hour"] = data["Date/Time"].apply(lambda x: x.hour)



sns.set(rc={'figure.figsize':(12, 10)})

def displayday():
    sns.distplot(data["Day"])
    plt.show()

def displayweek():
    sns.displot(data["Weekday"])
    plt.show()

def displayhour():
    sns.displot(data["Hour"])
    plt.show()

def corrolation():
    df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
    df = df.unstack()
    sns.heatmap(df, annot=False)
    plt.show()

def place():
    data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
    figsize=(12, 8), cmap=plt.get_cmap('jet'))
    plt.title("Uber Trips Analysis")
    plt.legend()
    plt.show()

#testing

place()
