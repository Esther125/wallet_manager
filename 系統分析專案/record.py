import pandas as pd 

def showRecordList():
    show_record = []

    df = pd.read_csv ('record.csv' ,encoding='utf-8')
    show_record.append(['description','category','quantity','unitPrice','amount'])
    show_record.append(["------------------------------------------------------------"])
    for i in range(0,len(df)):
        temp = []

        temp.append(df['description'][i])
        temp.append(df['category'][i])
        temp.append(df['quantity'][i])
        temp.append(df['unitPrice'][i])
        temp.append(df['amount'][i])

        show_record.append(temp)

    return show_record
