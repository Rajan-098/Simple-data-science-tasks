import pandas as pd
import datetime
##import sqlite3
##import matplotlib.pyplot as plt
##cur=sqlite3.connect("History").cursor()
##command=''' sp_columns @visits="News" '''
##command="SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE visits = N'''Customers''' "
##command="   SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('dbo.visits')"
##command="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='visits'"
##command="EXEC sp_columns 'visits'"
##command='''SELECT * FROM urls'''
##length=[]
##_all=cur.execute(command).fetchall()
##file=open("urls.csv","w")
##file.write("index,url,header,num,num,adress,num")
##file.write("\n")
##iteration=0
##for tuple_ in _all:
##    try:
##        data=list(tuple_)
##        occur=0
##        for index,char in enumerate(data[1]):
##            if char=="/":
##                occur+=1
##                if occur==3:
##                    end=index
##        if occur>2:
##            data[1]=data[1][:end+1]
##        string=str(tuple(data))[1:-1]
##        
##        occur=0
##        for index,char in enumerate(data[2]):
##            if char=="/":
##                occur+=1
##                if occur==3:
##                    end=index
##        if occur>2:
##            data[2]=data[2][:end+1]
##        data[2]=data[2][:20]
##        string=str(tuple(data))[1:-1]
##        string=string.replace("""'""",'''"''')
##        file.write(string)
##        print(string)
##        file.write('\n')
##    except Exception as e:
##        err_index=int(str(e)[str(e).find("position ")+9:str(e).find(": character")])
##        #print(err_index)
##        final_string=''.join([string[i] for i in range(len(string)) if i!=err_index])
##        print(final_string)
##        file.write(final_string)
##        file.write("\n")
##    if iteration==234:
##        print(",.................................")
##    iteration+=1
##file.close()
pd.read_csv("urls.csv",encoding="cp1252")
