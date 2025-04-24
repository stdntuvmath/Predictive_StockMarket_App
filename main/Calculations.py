
import main.DataBase_Management as DM
from json import load
import numpy as np
import pandas as pd
from statistics import mean, stdev


def TBDaily_GetRawData_NormalizeData_InsertIntoDB(symbol):

    df = DM.Data_Pulling_FromDB.TBDaily_Get_Historical_RawData_INTO_PandasDF(symbol)
    #df.head()

    # mean
    openPrice_mean = mean(df.OpenPrice)
    closePrice_mean = mean(df.ClosePrice)
    highPrice_mean = mean(df.HighPrice)
    lowPrice_mean = mean(df.LowPrice)
    volume_mean = mean(df.Volume)
    upDownDay_mean = mean(df.Up_Down_Day)

    # standard deviation
    openPrice_stDev = stdev(df.OpenPrice)
    closePrice_stDev = stdev(df.ClosePrice)
    highPrice_stDev = stdev(df.HighPrice)
    lowPrice_stDev = stdev(df.LowPrice)
    volume_stDev = stdev(df.Volume)
    upDownDay_stDev = stdev(df.Up_Down_Day)

    # OpenPrice---------------------------------
    norm_OpenPrice_Array = list()
    for openPrice in df.OpenPrice.values:
        norm_OpenPrice = (openPrice-openPrice_mean)/openPrice_stDev
        norm_OpenPrice_Array.append(norm_OpenPrice)

    # ClosePrice---------------------------------
    norm_ClosePrice_Array = list()
    for closePrice in df.ClosePrice.values:
        norm_ClosePrice = (closePrice-closePrice_mean)/closePrice_stDev
        norm_ClosePrice_Array.append(norm_ClosePrice)

    # HighPrice---------------------------------
    norm_HighPrice_Array = list()
    for highPrice in df.HighPrice.values:
        norm_HighPrice = (highPrice-highPrice_mean)/highPrice_stDev
        norm_HighPrice_Array.append(norm_HighPrice)

    # LowPrice---------------------------------
    norm_LowPrice_Array = list()
    for lowPrice in df.LowPrice.values:
        norm_LowPrice = (lowPrice-lowPrice_mean)/lowPrice_stDev
        norm_LowPrice_Array.append(norm_LowPrice)

    # Volume---------------------------------
    norm_Volume_Array = list()
    for volume in df.Volume.values:
        norm_Volume = (volume-volume_mean)/volume_stDev
        norm_Volume_Array.append(norm_Volume)

    # Up_Down_Day---------------------------------
    norm_Up_Down_DayArray = list()
    for day in df.Up_Down_Day.values:
        norm_Up_Down_Day = (day-upDownDay_mean)/upDownDay_stDev
        norm_Up_Down_DayArray.append(norm_Up_Down_Day)

    # put all lists* into one pandas dataframe--------------------------------------------
    newDF = pd.DataFrame({'Symbol': df.Symbol, 'nDate': df.nDate, 'OpenPrice': \
                          norm_OpenPrice_Array, 'ClosePrice': norm_ClosePrice_Array, \
                          'HighPrice': norm_HighPrice_Array, 'LowPrice': norm_LowPrice_Array, \
                          'Volume': norm_Volume_Array,'Up_Down_Day': norm_Up_Down_DayArray})
    return newDF



















# import main.DataBase_Management as DM
# import pandas as pd
# import numpy as np
# from os.path import exists



# class Normalize_Data:

#     def TBDaily_GetRawData_NormalizedData_InsertIntoDB(symbol):

#         df = DM.Data_Pulling_FromDB.Get_TBDaily_Historical_RawData_INTO_PandasDF(symbol)

#         #mean
#         openPrice_mean = df["OpenPrice"].mean()
#         closePrice_mean = df["ClosePrice"].mean()
#         highPrice_mean = df["HighPrice"].mean()
#         lowPrice_mean = df["LowPrice"].mean()
#         volume_mean = df["Volume"].mean()
#         upDownDay_mean = df["Up_Down_Day"].mean()

#         #standard deviation
#         openPrice_stDev = df["OpenPrice"].std()
#         closePrice_stDev = df["ClosePrice"].std()
#         highPrice_stDev = df["HighPrice"].std()
#         lowPrice_stDev = df["LowPrice"].std()
#         volume_stDev = df["Volume"].std()
#         upDownDay_stDev = df["Up_Down_Day"].std()



#         #change each df to a single array list so it can go into a for loop--------------------------------------------


#         #OpenPrice---------------------------------        
#         OpenPriceArray = []
#         OpenPriceArray = df["OpenPrice"].values
#         OpenPriceList = OpenPriceArray.tolist()
#         norm_OpenPrice_Array = np.empty([len(df["OpenPrice"])], dtype=float)


#         for i in OpenPriceList:
#             norm_OpenPrice = (i+openPrice_mean)/openPrice_stDev
#             np.append(norm_OpenPrice_Array, norm_OpenPrice)
#             i=None




#         #ClosePrice---------------------------------        
#         ClosePriceArray = []
#         ClosePriceArray = df["ClosePrice"].values
#         ClosePriceList = ClosePriceArray.tolist()
#         norm_ClosePrice_Array = np.empty([len(df["ClosePrice"])], dtype=float)

#         for i in ClosePriceList:
#             norm_ClosePrice = (i+closePrice_mean)/closePrice_stDev
#             np.append(norm_ClosePrice_Array, norm_ClosePrice)
#             i=None
       



#         #HighPrice---------------------------------        
#         HighPriceArray = []
#         HighPriceArray = df["HighPrice"].values
#         HighPriceList = HighPriceArray.tolist()
#         norm_HighPrice_Array = np.empty([len(df["HighPrice"])], dtype=float)

#         for i in HighPriceList:
#             norm_HighPrice = (i+highPrice_mean)/highPrice_stDev
#             np.append(norm_HighPrice_Array, norm_HighPrice)
#             i=None
        




#         #LowPrice---------------------------------        
#         LowPriceArray = []
#         LowPriceArray = df["LowPrice"].values
#         LowPriceList = LowPriceArray.tolist()
#         norm_LowPrice_Array = np.empty([len(df["LowPrice"])], dtype=float)

#         for i in LowPriceList:
#             norm_LowPrice = (i+lowPrice_mean)/lowPrice_stDev
#             np.append(norm_LowPrice_Array, norm_LowPrice)
        




#         #Volume---------------------------------        
#         VolumeArray = []
#         VolumeArray = df["Volume"].values
#         VolumeList = VolumeArray.tolist()
#         norm_Volume_Array = np.empty([len(df["Volume"])], dtype=float)

#         for i in VolumeList:
#             norm_Volume = (i+volume_mean)/volume_stDev
#             np.append(norm_Volume_Array, norm_Volume)
#         i=0




#         #Up_Down_Day---------------------------------        
#         Up_Down_DayArray = []
#         Up_Down_DayArray = df["Up_Down_Day"].values
#         Up_Down_DayList = Up_Down_DayArray.tolist()
#         norm_Up_Down_DayArray = np.empty([len(df["Up_Down_Day"])], dtype=float)

#         for i in Up_Down_DayList:
#             norm_Up_Down_Day = (i+upDownDay_mean)/upDownDay_stDev
#             np.append(norm_Up_Down_DayArray, norm_Up_Down_Day)
#         i=0







#         #put all arrays into one pandas dataframe--------------------------------------------





#         newDF = pd.DataFrame({'Symbol': df["Symbol"], 'nDate': df["nDate"], 'OpenPrice': norm_OpenPrice_Array, 'ClosePrice': norm_ClosePrice_Array,
#                               'HighPrice': norm_HighPrice_Array, 'LowPrice': norm_LowPrice_Array, 'Volume': norm_Volume_Array, 
#                               'Up_Down_Day':norm_Up_Down_DayArray })
#         #print(newDF)



#         #create file for Logan to view

#         newDF_json = newDF.to_json(indent=4)

#         file_exists = exists("PriceData\\{}_priceData.json".format(symbol))    

#         if(file_exists == True):

#             outFile = open("PriceData\\{}_priceData.json".format(symbol), "a")
#             outFile.write("{}".format(newDF_json))
#             outFile.close()            

#         else:
#             outFile = open("PriceData\\{}_priceData.json".format(symbol), "a")
#             outFile.write("{}".format(newDF_json))
#             outFile.close()






