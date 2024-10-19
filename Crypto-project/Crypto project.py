#!/usr/bin/env python
# coding: utf-8

# ### Cryptocurrencies Price Tracker
# 
#     Just shift-Enter the below cell to run the GUI code

# In[1]:


from tkinter import *
from tkinter import ttk
import requests
from sys import exit
from time import perf_counter,ctime

win=Tk()
win.title('Cryptocurrency trade Checker')
win.geometry('400x400')

btc_price="starting!"
eth_price='starting!'
ltc_price='starting!'
ada_price='starting!'

#creating menu function
my_menu=Menu(win)
win.config(menu=my_menu)

# clicked button function
def func():
    
    #font
    f2=('arial',10,'bold')
    
    # for bitcoin
    Bitcoin=Label(win,text="Bitcoin -",bg='gold',font=f2)
    Bitcoin.place(x=100,y=90)
    Btc_Price=Label(win,text=btc_price)
    Btc_Price.place(x=160,y=90)
    
    #for etherum
    ether=Label(win,text='Ehterium- ',bg='blue',fg='white',font=f2)
    ether.place(x=100,y=120)
    Eth_Price=Label(win,text=eth_price)
    Eth_Price.place(x=170,y=120)
    
    #for litecoin
    ltc=Label(win,text='Litecoin- ',bg='green yellow',fg='black',font=f2)
    ltc.place(x=100,y=150)
    ltc_Price=Label(win,text=ltc_price)
    ltc_Price.place(x=170,y=150)
    
    #for cordano
    ada=Label(win,text='Cordano- ',bg='sky blue',fg='black',font=f2)
    ada.place(x=100,y=180)
    ada_Price=Label(win,text=ada_price)
    ada_Price.place(x=180,y=180)
    

    #get prices
    a=requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,ADA&tsyms=USD").json()
    Btc_Price.configure(text=str(a['BTC'])+" $",bg='ivory3',font=f2)
    Eth_Price.config(text=str(a['ETH'])+" $",bg='ivory3',font=f2)
    ltc_Price.config(text=str(a['LTC'])+" $",bg='ivory3',font=f2)
    ada_Price.config(text=str(a['ADA'])+" $",bg='ivory3',font=f2)
    win.after(15000,func)
    print("refreshed at {}  ".format(str(ctime())))



# button function
def demo():
    
    #font
    f1=('arial',10,'bold')
    
    check_label=Label(win,text='To check Trading prices of top 4 Cryptocurrencies',bg='blue',fg='white',font=f1)
    check_label.place(x=40,y=10)

    button=Button(win,text='Click here',bg='green',command=func)
    button.place(x=150,y=35)
    
    
#favorites
def demo2():
    fav_list=Listbox(win,width=27)
    items=['Bitcoin','Etherum','Litecoin','Cordano']
    for i in items:
        fav_list.insert(END,i)
    fav_list.pack()
    
    

# menu function
file_menu=Menu(my_menu)
my_menu.add_cascade(label='Tab-1',menu=file_menu)
file_menu.add_command(label='Check Crypto',command=demo)

file_menu.add_separator()

file_menu2=Menu(my_menu)
my_menu.add_cascade(label='Tab-2',menu=file_menu2)
file_menu2.add_command(label='Favorites',command=demo2)

win.mainloop()


# In[ ]:




