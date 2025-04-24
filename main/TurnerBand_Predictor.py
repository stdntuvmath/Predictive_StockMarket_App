
from tda.client import Client
from tda.auth import easy_client
import main.config_TDA_Live as cf
from urllib.error import HTTPError
import pytz
import datetime
from main import Calculations as calc
import pandas as pd
import json
from sklearn.metrics import confusion_matrix as cm
import main.DataBase_Management as DM
import main.RandomForestClassifierModel as RFM




def Run_TurnerBandsDaily(numberOfSymbols):


    client = easy_client(
        api_key=cf.api_key,
        redirect_uri=cf.redirect_url,
        token_path=cf.token_path)


    allSymbols = DM.Data_Pulling_FromDB.Get_SymbolList_FromDB()


    counter_ofSymbols = 0
    
    for symbol in allSymbols:
        if(counter_ofSymbols < numberOfSymbols):
  
            try:

                result = client.get_price_history_every_day(symbol,
                                                start_datetime=None,
                                                end_datetime=None)

            except HTTPError:
                print('HTTPError: Candle data could not be pulled from TDAs server.')


            except TypeError:
                print('TypeError: Candle data could not be pulled from TDAs server.')
            #print(result)
            #convert to json
            pricedata = result.json()
            #print(pricedata)

            


            #parse json data
            for candle in pricedata['candles']:  
                openPrice = candle.get("open","")
                closePrice = candle.get("close","")
                highPrice = candle.get("high","")
                lowPrice = candle.get("low","")
                volume = candle.get("volume","")
                epochTime = candle.get("datetime","") / 1000

                tz = pytz.timezone('US/Central')

                stringLocalTime = str(datetime.datetime.utcfromtimestamp(epochTime).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%Y%m%d %H:%M:%S'))#from utc to local time

                stringLocalTimeArray = []

                stringLocalTimeArray = stringLocalTime.split(" ")

                localDate = stringLocalTimeArray[0]
                #localTime = stringLocalTimeArray[1]

                #print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(openPrice, closePrice, highPrice, lowPrice, volume, localDate, localTime))



                #calculations _____________________________________________________________________

                #up/down days

                middleCandleLength = closePrice - openPrice

                if(middleCandleLength > 0):
                    upDownDay = 1
                elif(middleCandleLength < 0):
                    upDownDay = 0

                
                #put raw data into server
                DM.Data_Pushing_ToDB.InsertInto_TBDaily(symbol, localDate, openPrice, closePrice, highPrice, lowPrice, volume, upDownDay)
                #pull raw data into data frame




            
            print(str(counter_ofSymbols)+". Raw Data for "+symbol+" has been inserted into DB.\n\n")
            df = DM.Data_Pulling_FromDB.TBDaily_Get_Historical_RawData_INTO_PandasDF(symbol)
            print("Raw Data and Raw Data Description for stock "+symbol+"\n")
            print(df)
            print(df.describe())
            print("\n")

            normalized_df = calc.TBDaily_GetRawData_NormalizeData_InsertIntoDB(symbol)

            print("Normalized Data Description for stock "+symbol+"\n\n")
            print(normalized_df)
            print(normalized_df.describe())
            print("\n")


            print("Prediction Description for stock "+symbol+"\n\n")
            predictions = RFM.UpDownDay_Predictor_Model.RunModel(normalized_df)
            print("\n")
            print(predictions)
            print(predictions.describe())
            print("\n")


            # predictionsINTArray = []

            # for prediction in predictions:
            #     prdInt = int(prediction)
            #     predictionsINTArray.append(prdInt)

            #create new dataframe with both data and predictions and insert into db

            


            newDF = pd.DataFrame({'Symbol': df.Symbol, 'nDate': df.nDate, 'OpenPrice': \
                        df.OpenPrice, 'ClosePrice': df.ClosePrice, \
                        'HighPrice': df.HighPrice, 'LowPrice': df.LowPrice, \
                        'Volume': df.Volume,'Up_Down_Day': df.Up_Down_Day, 'Up_Down_Day_Prediction':predictions})

            #newerDF = pd.DataFrame({})
            #delete excess rows
            # for column, row in newDF.iterrows():
            #     if(row['Up_Down_Day_Prediction'] != "NaN"):
            #         newerDF.append(row)          
            
            #pd.set_option('display.max_rows', df.shape[0]+1)
            #print(newerDF)

            #print(str(df.Symbol[1])+", "+str(df.ClosePrice[1]))
            
            #for row in newDF.iterrows():
                #print(row)
            DM.Data_Pushing_ToDB.TBDaily_Insert_Into_Daily_Historical_Prediction_Tables(df.Symbol, df.nDate, df.OpenPrice, df.ClosePrice, df.HighPrice, df.LowPrice, df.Volume, df.Up_Down_Day, predictions)
            #correct = 0
            # incorrect = 0
            # nan = 0
            # for column, row in newDF.iterrows():
            #     if(row['Up_Down_Day'] == row['Up_Down_Day_Prediction']):

            
            # score1 = correct/len(predictions)
            # score2 = incorrect/len(predictions)

            # print("correct: "+str(score1))
            # print("incorrect: "+str(score2))
            # print("correct + incorrect: "+str(score1 + score2))


            #print(newDF)

            #jsonObject = json.dumps(predictionsINTArray)



            counter_ofSymbols +=1



