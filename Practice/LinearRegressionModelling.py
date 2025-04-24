#dependencies

import imp
from matplotlib.pyplot import plot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pyodbc
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def LinearRegressionModel():

    #sql connection

    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

    sql_query = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM A_Historical
                                ''', connection)

    df = pd.DataFrame(sql_query, columns = ['Symbol', 'nDate', 'nTime', 'Price', 'EMA200', 'EMA200Angle', 'stdrdDev1', 'stdrdDev2', 'stdrdDev3', 'stdrdDev4', 'stdrdDev5', 'stdrdDev6', 'stdrdDev7', 'stdrdDev8', 'stdrdDev9', 'stdrdDev10'])
    print(df)
    #print(df.columns)
    #print(df.isnull().sum())
    print(df.describe())



    train = df.drop(['EMA200Angle', 'Symbol', 'nDate', 'nTime'], axis=1)
    test = df['EMA200Angle']

    X_train, X_test, Y_train, Y_test = train_test_split(train, test, test_size=0.9, random_state=2)

    regr = LinearRegression()

    regr.fit(X_train, Y_train)

    pred = regr.predict(X_test)

    score = regr.score(X_test, Y_test)

    print(pred)
    print(len(pred))
    print(score)


    #sns.relplot(x='nTime', y='Price', data=df)
    #plt.show()

