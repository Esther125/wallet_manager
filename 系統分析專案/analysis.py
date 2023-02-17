import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties as font
#首先import一大堆東西
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfile 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)



# 設定字型的路徑
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False


def startAnalysis():
    #設定視窗
    window=tk.Tk()
    window.title("My Window")
    window.geometry("850x850")#視窗大小
    window['bg']='#faf4e0'
    w = tk.Label(window, text="十二月份紀錄" ,font=('Arial', 25))
    w['bg']='#faf4e0'
    w.pack()
    
    # 讀入記帳明細資料
    df = pd.read_csv ('record.csv' ,encoding='utf-8')
    print(df)

    # 依類別計算總花費
    food_sum = 0
    drink_sum = 0
    food_num = 0
    drink_num = 0
    # 判斷類別並加總
    for i in range(0,len(df)):
        if df['category'][i] == "food":
            food_sum = food_sum + df['amount'][i]
            food_num = food_num+1
        elif df['category'][i] == "drink":
            drink_sum = drink_sum + df['amount'][i]
            drink_num = drink_num+1
    
    ##圓餅圖
    category = ['food','drink']
    value = [food_sum,drink_sum]
    
    pie = plt.figure(figsize=(6, 4),facecolor="#faf4e0",dpi=75)  #圓餅圖的白框會比其他圖的大 我不知道為甚麼
    axes2 = pie.add_subplot()                                    #所以我沒有畫白框
    pie.labels = category
    pie.sizes = value
    pie.colors = ['green', 'blue']  
    pie.explode = (0.05, 0.04)  # 分割，值越大分割出的间隙越大
    pie.patches, pie.text2, pie.text1 = plt.pie(pie.sizes,
                                            explode=pie.explode,
                                            labels=pie.labels,
                                            colors=pie.colors,
                                            autopct='%3.1f%%',  # 数值保留小数位数
                                            shadow=True,  # 有、无阴影设置
                                            startangle=90,  # 逆时针起始角度设置
                                            pctdistance=1.4,#标签数字和圆心的距离
                                            textprops={'fontsize': 12, 'color': '#000080'}
                                            )
    axes2=plt.axis('equal') #正圆
    #plt.title('十二月份紀錄')
    canvas2 = FigureCanvasTkAgg(pie, window)
    canvas2.get_tk_widget().place(x=400, y=40)#根据坐标，放在指主窗口的指定位置



    ##長條圖
    data = df.loc[:, ['description', 'amount']]
    data = data.set_index('description')
    
    # create a figure
    bar = Figure(figsize=(6, 4), dpi=65)#改dpi的數字會比較方便 他可以等比例縮放

    # create FigureCanvasTkAgg object
    canvas1 = FigureCanvasTkAgg(bar, window)

    # create axes
    axes1 = bar.add_subplot()

    # create the barchart
    axes1.bar(df['description'],df['amount'])
    #axes1.set_title('十二月份')
    axes1.set_ylabel('總花費',fontsize=12, labelpad = 15)
    axes1.set_xlabel('商品名稱',fontsize=10, labelpad = 15)
    
    canvas1.get_tk_widget().place(x=20,y=60)#用place可以自己設定離邊界的距離
    
    
    ##折線圖
    x = category
    y=[food_sum/food_num,drink_sum/drink_num]
    line = plt.figure(figsize=(6, 4), dpi=65)
    axes3 = line.add_subplot()
    axes3=plt.plot(x, y, 'ro--', linewidth=2, markersize=6)
    plt.ylabel("平均消費量", fontsize=12, labelpad = 15)
    canvas3 = FigureCanvasTkAgg(line, window)
    canvas3.get_tk_widget().place(x=20,y=350)


    ##曲線圖
    #curve = Figure(figsize=(6, 4), dpi=65)
    #axes4 = curve.add_subplot()

    # 我這裡畫sin圖 我不知道要畫甚麼了 所以亂畫 讓他看起來很厲害
    #x = np.arange(0, 3, 0.01)
    #y = np.sin(2 * np.pi * x)

    #axes4.plot(x, y)
    #canvas4 = FigureCanvasTkAgg(curve, master=window)
    #canvas4.get_tk_widget().place(x=450,y=350)

    ##長條圖
    # create a figure
    bar2 = Figure(figsize=(6, 4), dpi=65)#改dpi的數字會比較方便 他可以等比例縮放

    # create FigureCanvasTkAgg object
    canvas4 = FigureCanvasTkAgg(bar2, window)

    # create axes
    axes4 = bar2.add_subplot()

    # create the barchart
    axes4.bar(category,value)
    #axes1.set_title('十二月份')
    axes4.set_ylabel('總花費',fontsize=12, labelpad = 15)
    axes4.set_xlabel('商品種類',fontsize=10, labelpad = 15)
    
    canvas4.get_tk_widget().place(x=450,y=350)#用place可以自己設定離邊界的距離