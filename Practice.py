import pandas as pd
import numpy as np
import main.DataBase_Management as DM
from main import Calculations as calc, TurnerBand_Predictor as TB
from os.path import exists
import main.RandomForestClassifierModel as RF


#create df

#df = Data_Pulling_FromDB.Get_TBDaily_Historical_RawData_INTO_PandasDF("A")

DM.Data_Deleting_FromDB.Clear_Data_From_Tables.TBDaily_Clear_Daily_Historical_Data_From_ALL_Symbols()


#print(newDf)

#create random numpy array and put it into a pandas df


#newDf = pd.DataFrame({'Symbol':df["Symbol"], 'nDate':df["nDate"]})
#print(newDf.head())




TB.Run_TurnerBandsDaily(1)




