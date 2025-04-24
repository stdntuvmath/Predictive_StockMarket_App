import pyodbc
import regex as re
import datetime
import pandas as pd


class Data_Pulling_FromDB:



    #____________________________________________________________________________________________________________________
    #TURNER BANDS DAILY PULLING METHODS
    #____________________________________________________________________________________________________________________

    
    def TBDaily_Get_Up_Down_Day_Data_Only_FromDB(symbol):    

            #database stuff
            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            data = cursor.execute('SELECT Up_Down_Day FROM {}_Daily_Historical ORDER BY nDate ASC'.format(symbol))

            cursor.close()
            return data



    def TBDaily_Get_Historical_RawData_INTO_PandasDF(symbol):

        connection = pyodbc.connect('Driver={SQL Server};'
                                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                        'Database=LootLoader;'
                                        'Trusted_Connection=yes;')

        df = pd.read_sql_query ('''
                                    SELECT
                                    *
                                    FROM {}_Daily_Historical ORDER BY nDate ASC
                                    '''.format(symbol), connection)

        #print(sql_query)

        #df = pd.DataFrame(sql_query, columns = ['Symbol', 'nDate', 'open', 'close', 'high', 'low', 'volume', 'upDownDay'])
        #dfValues = pd.concat(df)
        connection.close()
        #It already is a pandas dataframe from the read_sql_query so you don't need to do pd.DataFrame.
        return df


    #____________________________________________________________________________________________________________________
    #TURNER BANDS PULLING METHODS
    #____________________________________________________________________________________________________________________  


    def Get_Account_TEST():#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')


        
        with LootLoaderDBConnection.cursor() as cursor:

            cursor.execute('SELECT * FROM Account_Test')


            return cursor.fetchone()


    def Get_okToBuyStatus_FromDB(symbol, localDate):    

        #database stuff
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #insert data int table
        cursor.execute('SELECT TOP 1 * FROM {}_okToBuy  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, localDate))
        
        status = 0

        for i in cursor:

            st = str(i)
            crapRemoval1 = st.replace("(","")
            status = crapRemoval1.replace(", )","")

        #print(status)    

        #print(status)

        cursor.close()
        return status


    def GetBuyPrice(symbol):#returns a float number

        todaysDate = datetime.datetime.today().date()
        #todaysDate = "2022-04-05"

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT TOP 1 * FROM {}_Trading  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, todaysDate))

        array=[]

        for i in cursor:
            
            array.append(i)
            
        #print(array)
        cursor.close()
 

    def GetShareAmount(symbol):#returns a float number

        todaysDate = datetime.datetime.today().date()

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT TOP 1 * FROM {}_Trading  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, todaysDate))

        array=[]

        for i in cursor:

            array.append(i)
            

        buyPrice = array[4]
        cursor.close()
        
        return buyPrice


    def Get_EMA200Array_FromDB(symbol):#returns array of angles

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT * FROM {}_EMA200AngleArray'.format(symbol))

        array=[]

        for i in cursor:

            st = str(i)
            crapRemoval1 = st.replace("(","")
            crapRemoval2 = crapRemoval1.replace(", )","")
            flt = float(crapRemoval2)
            array.append(flt)
                
        cursor.close()

        return array


    def Get_Newest_ClosingPrice(symbol):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT * FROM {}_singleEntry'.format(symbol))

        array=[]

        for i in cursor:

            array.append(i)
            

        cursor.close()
        
        recordString = str(array)
        crap1 = recordString.replace('[','')
        crap2 = crap1.replace(']','')
        crap3 = crap2.replace('(','')
        crap4 = crap3.replace(')','')
        crap5 = crap4.replace('   \'','')
        crap6 = crap5.replace('\'','')
        crap7 = crap6.replace(' ', '')
        #print(crap7)

        record=crap7.split(',')

        closingPrice = float(record[3])

        return closingPrice


    def Get_Newest_EMA200_FromDB(symbol):

        todaysDate = datetime.datetime.today().date()
        #todaysDate = "2022-04-01"   

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;') 

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT TOP 1 * FROM {}_Historical  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, todaysDate))
        array=[]


        for i in cursor:

            array.append(i)
            

        cursor.close()
        
        recordString = str(array)
        crap1 = recordString.replace('[','')
        crap2 = crap1.replace(']','')
        crap3 = crap2.replace('(','')
        crap4 = crap3.replace(')','')
        crap5 = crap4.replace('   \'','')
        crap6 = crap5.replace('\'','')
        crap7 = crap6.replace(' ', '')
        #print(crap7)

        record=crap7.split(',')

        ema200 = float(record[4])
        #print(ema200)
        return ema200


    def Get_SymbolList_FromDB():
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('SELECT Symbol FROM Symbols')

        symbolList = [] #you have to start with a list and then convert the list to a tuple

        for i in cursor:

            makeString = str(i)
            onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
            symbolList.append(onlySymbol)

    

        return symbolList


    def Get_Status(symbol, localDate):    

        #database stuff
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #insert data int table
        cursor.execute('SELECT TOP 1 * FROM {}_okToBuy  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, localDate))
        
        status = 0

        for i in cursor:

            st = str(i)
            crapRemoval1 = st.replace("(","")
            status = crapRemoval1.replace(", )","")

        #print(status)    

        #print(status)

        cursor.close()
        return status


class Data_Pushing_ToDB:


    #____________________________________________________________________________________________________________________
    #TURNER BANDS DAILY PUSHING METHODS
    #____________________________________________________________________________________________________________________

    def InsertInto_TBDaily(symbol, date, open, close, high, low, volume, upDownDay):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO {}_Daily_Historical VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(symbol, symbol, date, open, close, high, low, volume, upDownDay))
        
        cursor.commit()
        cursor.close()


    def TBDaily_Insert_Into_Daily_Historical_Prediction_Tables(symbol, date, open, close, high, low, volume, upDownDay, newDFWithPredictions):

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO {}_Daily_Historical_Prediction VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(symbol, symbol, date, open, close, high, low, volume, upDownDay, newDFWithPredictions))
        
        cursor.commit()
        cursor.close()








    #____________________________________________________________________________________________________________________
    #TURNER BANDS PUSHING METHODS
    #____________________________________________________________________________________________________________________

    def TB_Insert_Initial_AccountValue_TEST(accountValue):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO Account_Test VALUES (\'{}\')'.format(accountValue))
        
        cursor.commit()
        cursor.close()




    def TB_Insert_AccountValue_TEST(accountValue):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO Account_Test (accountValue) VALUES (\'{}\')'.format(accountValue))
        
        cursor.commit()
        cursor.close()




    def TB_Insert_TradeData_IntoDB(symbol, dayOfWeek, tradeType, localDate, localTime, buyPrice, numberOfShares, accountValue, profit_loss, goodTrade, ema200Angle, ema200Value, ema1000Value):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO {}_Trading (Symbol, dayOfWeek, tradeType, nDate, nTime, Price, numberOfShares, accountProfit, profit_loss, Good_Trade, EMA200Angle, EMA200Value, EMA1000Value) VALUES (\'{}\',\'{}\',\'{}\', \'{}\',\'{}\', \'{}\', \'{}\', \'{}\', \'{}\',\'{}\', \'{}\', \'{}\', \'{}\')'.format(symbol, symbol, dayOfWeek, tradeType, localDate, localTime, buyPrice, numberOfShares, accountValue, profit_loss, goodTrade, ema200Angle, ema200Value, ema1000Value))
        
        cursor.commit()
        cursor.close()




    def TB_Insert_Symbol_Price_andDateTime_Data(symbol, price, date, time):
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()


        #insert data int table
        cursor.execute('INSERT INTO {} (Symbol, Price, nDate, nTime) VALUES (\'{}\', {}, \'{}\', \'{}\')'.format(symbol, symbol, price, date, time))
        cursor.commit()
        cursor.close()




    def TB_Insert_Into_Historical_Data(symbol, localDate, localTime, closePrice, newEma200Value, newEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10):
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #
        #insert data int table
        cursor.execute('INSERT INTO {}_Historical (Symbol, nDate, nTime, Price, EMA200, EMA200Angle, stdrdDev1, stdrdDev2, stdrdDev3, stdrdDev4, stdrdDev5, stdrdDev6, stdrdDev7, stdrdDev8, stdrdDev9, stdrdDev10) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(symbol, symbol, localDate, localTime, closePrice, newEma200Value, newEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10))
        cursor.commit()
        cursor.close()




    def TB_Insert_EMA200AngleArray_IntoDB(symbol, EMA200AngleArray):    
        
        #database stuff
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()




        for angle in EMA200AngleArray:

            #insert data int table
            cursor.execute('INSERT INTO {}_EMA200AngleArray (ema200Angle) VALUES (\'{}\')'.format(symbol, angle))
            cursor.commit()
        cursor.close()




    def TB_Insert_Symbol_Price_andDateTime_Data(symbol, price, date, time):
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()


        #insert data int table
        cursor.execute('INSERT INTO {} (Symbol, Price, nDate, nTime) VALUES (\'{}\', {}, \'{}\', \'{}\')'.format(symbol, symbol, price, date, time))
        cursor.commit()
        cursor.close()




    def TB_Insert_Boolean_Data(symbol):
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()



        cursor.execute('INSERT INTO {}_okToBuy (yes_no) VALUES (TRUE);'.format(symbol))
        cursor.commit()


        cursor.close()




    def TB_Insert_Dummy_Data(symbol):
        #database stuff

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()


        #insert dummy data first so fields can be updated
        cursor.execute('INSERT INTO {}_singleEntry (Symbol, nDate, nTime, Price) VALUES (\'{}\', \'2022/03/02\', \'00:00:00\', \'1.00\')'.format(symbol, symbol))
        cursor.commit()


        cursor.execute('INSERT INTO {}_okToBuy (yes_no) VALUES (\'TRUE\');'.format(symbol))
        cursor.commit()


        cursor.close()


    #   ***in order to UPDATE any table, there must first be data in the table to find with the WHERE clause***
    def TB_UPDATE_Newest_Data_IntoDB(symbol, localDate, localTime, closePrice):
        #database stuff
        #print("getting inside update method")
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #
        #UPDATE data
        cursor.execute('UPDATE {}_singleEntry SET Symbol=\'{}\', nDate=\'{}\', nTime=\'{}\', Price=\'{}\' WHERE Symbol=\'{}\''.format(symbol, symbol, localDate, localTime, closePrice, symbol))
        cursor.commit()
        cursor.close()



    def TB_Insert_okToBuyStatus_IntoDB(symbol,  localDate, localTime, okToBuy):
    #database stuff
    #print("getting inside update method")
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #
        #UPDATE data
        cursor.execute('INSERT INTO {}_okToBuy (Symbol, nDate, nTime, yes_no) VALUES (\'{}\', \'{}\', \'{}\', \'{}\')'.format(symbol, symbol, localDate, localTime, okToBuy))
        cursor.commit()
        cursor.close()





    #____________________________________________________________________________________________________________________
    #STAR C BANDS AND EMA200 PUSHING METHODS
    #____________________________________________________________________________________________________________________



    def StarC_Insert_AllData_IntoDB(symbol,  localDate, localTime, closePrice, TopBand, MiddleBand, BottomBand, EMA200, ATR, highPrice, lowPrice):
    #database stuff
    #print("getting inside update method")
        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                            'Database=LootLoader;'
                            'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        #
        #UPDATE data
        cursor.execute('INSERT INTO {}_StarCBands_EMA200 (Symbol, nDate, nTime, Price, TopBand, MiddleBand, BottomBand, EMA200, ATR, highPrice, lowPrice) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(symbol, symbol,  localDate, localTime, closePrice, TopBand, MiddleBand, BottomBand, EMA200, ATR, highPrice, lowPrice))
        cursor.commit()
        cursor.close()



    def StarC_Insert_TradeData_IntoDB(symbol, tradeType, localDate, localTime, buyPrice, sellPrice, numberOfShares, accountValue, 
                                                                    profit_loss, goodTrade, newEma200Value):#returns a float number

        LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                'Database=LootLoader;'
                                                'Trusted_Connection=yes;')

        cursor = LootLoaderDBConnection.cursor()

        cursor.execute('INSERT INTO {}_StarC_EMA200_Trading (symbol, tradeType, localDate, localTime, buyPrice, sellPrice, numberOfShares, accountValue, profit_loss, goodTrade, newEma200Value) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(symbol, symbol, tradeType, localDate, localTime, buyPrice, sellPrice, numberOfShares, accountValue, profit_loss, goodTrade, newEma200Value))
        
        cursor.commit()
        cursor.close()


class Data_Deleting_FromDB:

    class Clear_Data_From_Tables:

        def Clear_All_Tables_In_LootLoaderDB_ForStrategyCalled(strategyName):
        #database stuff

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                    'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                    'Database=LootLoader;'
                                                    'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #clears data in tables
            for symbol in symbolList:

                if(strategyName == "TurnerBands"):
                    cursor.execute('DELETE {}_EMA200AngleArray'.format(symbol))
                    cursor.commit()

                    cursor.execute('DELETE {}_Historical'.format(symbol))
                    cursor.commit()

                    cursor.execute('DELETE {}_okToBuy'.format(symbol))
                    cursor.commit()

                    cursor.execute('DELETE {}_singleEntry'.format(symbol))
                    cursor.commit()

                    cursor.execute('DELETE {}_Trading'.format(symbol))
                    cursor.commit()

                elif(strategyName == "StarC_EMA200"):

                    cursor.execute('DELETE {}_StarCBands_EMA200'.format(symbol))
                    cursor.commit()

                    cursor.execute('DELETE {}_StarC_EMA200_Trading'.format(symbol))
                    cursor.commit()


            cursor.execute('DELETE Account_Test'.format(symbol))
            cursor.commit()

            cursor.close()


        def TBDaily_Clear_Daily_Historical_Data_From_ALL_Symbols():

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                    'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                    'Database=LootLoader;'
                                                    'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #clears data in tables
            for symbol in symbolList:

                cursor.execute('DELETE {}_Daily_Historical'.format(symbol))
                cursor.commit()               

            cursor.close()


    class Delete_Tables:

        def TBDaily_Delete_Daily_Historical_Tables_FORALL_Symbols():


            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                    'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                    'Database=LootLoader;'
                                                    'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #clears data in tables
            for symbol in symbolList:

                cursor.execute('DROP TABLE {}_Daily_Historical'.format(symbol))
                cursor.commit()               

            cursor.close()



        #____________________________________________________________________________________________________________________
        #STAR C BANDS AND EMA200 DELETING METHODS
        #____________________________________________________________________________________________________________________








        #____________________________________________________________________________________________________________________
        #TURNER BANDS DELETING METHODS
        #____________________________________________________________________________________________________________________

        def TB_Delete_Table_For_Specific_Symbol(symbol, tableType):
            #database stuff

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            if(tableType == "BuyPrice"):

                cursor.execute('DROP TABLE {}_BuyPrice'.format(symbol))
                cursor.commit()

            if(tableType == "EMA200AngleArray"):

                cursor.execute('DROP TABLE {}_EMA200AngleArray'.format(symbol))
                cursor.commit()


            if(tableType == "Historical"):

                cursor.execute('DROP TABLE {}_Historical'.format(symbol))
                cursor.commit()

            if(tableType == "okToBuy"):

                cursor.execute('DROP TABLE {}_okToBuy'.format(symbol))
                cursor.commit()

            if(tableType == "singleEntry"):

                cursor.execute('DROP TABLE {}_singleEntry'.format(symbol))
                cursor.commit()

            cursor.close()



        def TB_Delete_Symbol_AND_SymbolTables(symbol):
            

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            
            
            #delete tables

            cursor.execute('DROP TABLE {}_EMA200AngleArray'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_Historical'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_okToBuy'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_singleEntry'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_Trading'.format(symbol))
            cursor.commit()
            
            #delete stock from symbol list

            cursor.execute('DELETE FROM LootLoader.dbo.Symbols WHERE Symbol=\'{}\''.format(symbol))
            cursor.commit()

            cursor.close()



        def TB_Delete_AllTables_ForSymbol(symbol):
            

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            
            
            #delete tables

            cursor.execute('DROP TABLE {}_EMA200AngleArray'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_Historical'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_okToBuy'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_singleEntry'.format(symbol))
            cursor.commit()

            cursor.execute('DROP TABLE {}_Trading'.format(symbol))
            cursor.commit()
            
        
            cursor.close()



        def TB_Delete_All_Tables_ForAllSymbols():
            #database stuff

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #delete tables
            for symbol in symbolList:

                cursor.execute('DROP TABLE {}_EMA200AngleArray'.format(symbol))
                cursor.commit()

                cursor.execute('DROP TABLE {}_Historical'.format(symbol))
                cursor.commit()

                cursor.execute('DROP TABLE {}_okToBuy'.format(symbol))
                cursor.commit()

                cursor.execute('DROP TABLE {}_singleEntry'.format(symbol))
                cursor.commit()

                cursor.execute('DROP TABLE {}_Trading'.format(symbol))
                cursor.commit()

            cursor.close()







        #____________________________________________________________________________________________________________________
        #GENERAL PUSHING METHODS
        #____________________________________________________________________________________________________________________

        def Delete_SpecificTable_ForAllStocks(tableType):
            #database stuff

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #delete tables
            for symbol in symbolList:

                cursor.execute('DROP TABLE {}_{}'.format(symbol, tableType))
                cursor.commit()

            cursor.close()



        def Delete_SpecificTable_ForSpecificStock(symbol, tableType):
            #database stuff

            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                'Database=LootLoader;'
                                'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('DROP TABLE {}_{}'.format(symbol, tableType))
            cursor.commit()

            cursor.close()

            
class DB_Setup:

    class Create_Tables:

        #____________________________________________________________________________________________________________________
        #TURNER BANDS DAILY METHODS
        #____________________________________________________________________________________________________________________

        def Create_TBDailyCandle_Historical_Prediction_Databases_ForAll_Symbols():


            LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                    'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                    'Database=LootLoader;'
                                                    'Trusted_Connection=yes;')

            cursor = LootLoaderDBConnection.cursor()

            cursor.execute('SELECT Symbol FROM Symbols')

            symbolList = [] #you have to start with a list and then convert it to a tuple

            for i in cursor:

                makeString = str(i)
                onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                symbolList.append(onlySymbol)
            
            
            #delete tables
            for symbol in symbolList:

                cursor.execute('CREATE TABLE LootLoader.dbo.{}_Daily_Historical_Prediction(Symbol nchar(4), nDate date, OpenPrice float, ClosePrice float, HighPrice float, LowPrice float, Volume bigint, Up_Down_Day int, Up_Down_Day_Prediction int);'.format(symbol))
                cursor.commit()


            cursor.close()





        def Create_TBDailyCandle_Historical_Databases_ForAll_Symbols():


                LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                                        'Database=LootLoader;'
                                                        'Trusted_Connection=yes;')

                cursor = LootLoaderDBConnection.cursor()

                cursor.execute('SELECT Symbol FROM Symbols')

                symbolList = [] #you have to start with a list and then convert it to a tuple

                for i in cursor:

                    makeString = str(i)
                    onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
                    symbolList.append(onlySymbol)
                
                
                #delete tables
                for symbol in symbolList:

                    cursor.execute('CREATE TABLE LootLoader.dbo.{}_Daily_Historical (Symbol nchar(4), nDate date, OpenPrice float, ClosePrice float, HighPrice float, LowPrice float, Volume bigint, Up_Down_Day int);'.format(symbol))
                    cursor.commit()


                cursor.close()

