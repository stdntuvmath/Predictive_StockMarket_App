#dependencies
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd



class UpDownDay_Predictor_Model:
    def RunModel(pandasDataFrame_OfSymbolData):

        # y = pandasDataFrame_OfSymbolData["ClosePrice"]
        # plt.plot(y)
        # plt.grid()
        # plt.show()
        data = pandasDataFrame_OfSymbolData[["ClosePrice"]]
        data=data.rename(columns = {'ClosePrice':'Actual_Close'})
        data["Up_Down_Day"] = pandasDataFrame_OfSymbolData.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])["ClosePrice"]

        #print(data.head(5))


        symbol_previous = pandasDataFrame_OfSymbolData.copy()
        symbol_previous = symbol_previous.shift(1)

        predictors = ["ClosePrice", "HighPrice","LowPrice", "OpenPrice", "Volume"]

        #join the predictors to the data table

        data = data.join(symbol_previous[predictors]).iloc[1:]


        model = RandomForestClassifier(n_estimators=100, min_samples_split=200, random_state=1)


        start = 1000
        step = 750

        predictionsArray = []
        for i in range(start, data.shape[0], step):

            train = data.iloc[0:i].copy()
            test = data.iloc[i:i+step].copy()

            model.fit(train[predictors], train["Up_Down_Day"])

            predictions = model.predict_proba(test[predictors])[:,1]
            predictions = pd.Series(predictions, index=test.index)
            predictions[predictions > 0.6] = 1
            predictions[predictions <= 0.7] = 0

            combined = pd.concat({"Up_Down_Day": test["Up_Down_Day"], "Predictions": predictions}, axis=1)
            predictionsArray.append(combined)

            #separate accuracy score
            # for()
            # for prediction in predictionsArray:
            #     if(prediction == test["Up_Down_Day"]):



        if(len(predictionsArray)<1):
            print("do nothing for now...")
        elif(len(predictionsArray)>=1):
            predictionsArray = pd.concat(predictionsArray)
            print("Target Raw data counts: \n")
            print(predictionsArray["Up_Down_Day"].value_counts())
            print("Total: "+str(len(predictionsArray["Up_Down_Day"])))
            print("\nTarget Prediction data counts: \n")
            print(predictionsArray["Predictions"].value_counts())
            print("Total: "+str(len(predictionsArray["Predictions"])))

            print("\n\nPrecision Score: ")
            print(precision_score(predictionsArray["Up_Down_Day"], predictionsArray["Predictions"]))

        return predictions






class Example:
    def RunModel(symbol):
        yahooSymbolData = yf.Ticker(symbol)
        symbol_history = yahooSymbolData.history(period="max")

        #symbol.head(5)

        #x = symbol_history(["Date"])
        y = symbol_history["Close"]

        plt.plot(y)
        plt.grid()
        #plt.show()

        data = symbol_history[["Close"]]
        data=data.rename(columns = {'Close':'Actual_Close'})
        data["Target"] = symbol_history.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0])["Close"]
        #print(data.head(5))

        symbol_previous = symbol_history.copy()
        symbol_previous = symbol_previous.shift(1)
        #print(symbol_previous.head(5))

        weekly_mean = data.rolling(5).mean()

        #predictors = pd.DataFrame(["Close", "High","Low", "Open", "Volume"])
        predictors = ["Close", "High","Low", "Open", "Volume"]

        #join the predictors to the data table

        data = data.join(symbol_previous[predictors]).iloc[1:]

        #print(data.head(5))

        #data = new_symbol_history.merge(predictors, right_on='Close', left_index=True)

        #data = new_symbol_history.join(predictors, how='left', lsuffix='left', rsuffix='right' )#.iloc[1:]

        #data = new_symbol_history.merge(predictors, how='left')#.iloc[1:]




        # train = data.iloc[:-100]#all data up to the last 100 rows of the data frame
        # test = data.iloc[-100:]#only the last 100 rows of the data frame


        # #This will train the model by predicting the target using the predictors
        # model.fit(train[predictors], train["Target"])

        # predictions = model.predict(test[predictors])
        # #print(predictions.head(5))

        # predictions = pd.Series(predictions, index=test.index)

        # print(predictions)

        # accuracy = precision_score(test["Target"], predictions)

        # print(accuracy)

        # combined = pd.concat({"Target": test["Target"], "Predictions": predictions}, axis=1)

        # print(combined)



        #create model
        model = RandomForestClassifier(n_estimators=100, min_samples_split=200, random_state=1)


        start = 1000
        step = 750

        predictionsArray = []
        for i in range(start, data.shape[0], step):

            train = data.iloc[0:i].copy()
            test = data.iloc[i:i+step].copy()

            model.fit(train[predictors], train["Target"])

            predictions = model.predict_proba(test[predictors])[:,1]
            predictions = pd.Series(predictions, index=test.index)
            predictions[predictions > 0.6] = 1
            predictions[predictions <= 0.6] = 0

            combined = pd.concat({"Target": test["Target"], "Predictions": predictions}, axis=1)
            predictionsArray.append(combined)


        predictionsArray = pd.concat(predictionsArray)

        print(predictionsArray["Target"].value_counts())
        print(predictionsArray["Predictions"].value_counts())

        print(precision_score(predictionsArray["Target"], predictionsArray["Predictions"]))






