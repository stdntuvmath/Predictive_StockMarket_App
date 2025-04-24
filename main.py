import main.RandomForestClassifierModel as RF
import main.TurnerBand_Predictor as TB
import main.DataBase_Management as DM

DM.Data_Deleting_FromDB.Clear_Data_From_Tables.TBDaily_Clear_Daily_Historical_Data_From_ALL_Symbols()

TB.Run_TurnerBandsDaily(10)

#RF.RunModel()



#-----------------------------------------------
#          PRACTICE SECTION                   --
#-----------------------------------------------


#df = DM.Data_Pulling_FromDB.Get_TBDaily_Historical_RawData_INTO_PandasDF("AA")
#print(df.head())
