#hours wasted 4hrs and 30mins
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
n=0
par={'Current Liability':n,'Current Assets':n,'Liquid Assets':n,'Debt':n,'Shareholders equity':n,'Net profit':n,'Gross profit':n,
     'revenue':n,'cost of investment':n}
for i in par:
   n=int(input('enter'+" "+i+':')) 
   par[i]=n
   
def Working_capital():
 working_capital=par['Current Liability']-par['Current Assets']
 print(working_capital)
 
def Current_ratio():
   cr=par['Current Assets']//par['Current Liability']
   print(cr)
   if par['Current Assets']*2==par['Current Liability']:
      print('ratio is ideal')
   else:
      print('ratio is not ideal')
      
def Liquid_ratio():
   lr=par['Liquid Assets']//par['Current Liability']
   print(lr)
   if par['Liquid Assets']==par['Current Liability']:
      print('ratio is ideal')
   else:
      print('ratio is not ideal')
      
def debt_to_equity():
   de=par['Debt']//par['Shareholders equity']
   print(de)
   if par['Debt']*2==par['Shareholders equity']:
      print('ratio is ideal')
   else:
      print('ratio is not ideal')
      
def Gross_profit_ratio():
   gp=(par['Gross profit']//par['revenue'])*100
   print(gp)
   if gp>=20 and gp<=40:
     print('ratio is ideal')
   else:
      print('ratio is not ideal')
           
def Return_on_equity():
   re=(par['Net profit']//par['Shareholders equity'])*100
   print(re)
   if re>=15:
     print('ratio is ideal')
   else:
      print('ratio is not ideal')
      
def Return_on_investment():
   ri=(par['Net profit']//par['cost of investment'])*100
   print(ri)
   if ri>=10:
     print('ratio is ideal')
   else:
      print('ratio is not ideal')
      
def barofcashflow():     
      co=[]
      for i in range(1,5,1):
        n=int(input("enter the ammout of cashoutflow in Quarters:"))
        n2=-n
        co.append(n2)

      ci=[]
      for p in range(1,5,1):
        m=int(input("enter the ammout of cashinflow in Quarters:"))
        ci.append(m)

      ma=int(input("enter the maximum cashinflow:"))
      ma2=int(input("enter the maximum cashoutflow:"))

      pdf=pd.DataFrame(
      {"cashoutflow":co,
      "cashinflow":ci},
      index=['1st','2nd','3rd','4th'])


      pdf.plot(kind='bar',stacked=True)
      plt.ion()
      plt.title("cashflow bar")
      plt.yticks(np.arange(ma2,ma,20))
      plt.xlabel('amount')
      plt.ylabel('Quarter')
      plt.axhline(0, color='black', linewidth=0.8)
      plt.legend()
      plt.show()
      
def piebal():
   label=list(par.keys())
   size=list(par.values())   
   plt.ion()
   plt.pie(size,labels=label,shadow=True, startangle=140)
   plt.legend(label, loc='upper left', bbox_to_anchor=(1, 1))
   plt.show()

def stockstrend():
   sl=[]
   for j in range(1,13,1):
      s=int(input('enter the amount of stocks each month:'))
      sl.append(s)
   stocks=pd.Series(sl)
   print('enter 1 to get line chart')
   print('enter 2 to get histogram')
   c=int(input('enter the choice:'))
   if c==1:
      stocks.plot(marker='*')
      plt.ion()
      plt.title("stocks trend")
      plt.ylabel('time')
      plt.xlabel('price')
      plt.show()
   elif c==2:
      stocks.hist()
      plt.ion()
      plt.title("stocks trend")
      plt.ylabel('time')
      plt.xlabel('price')
      plt.show()
   else:
      print('invalid choice,choose stocks trend choice again')
      
while True:
   print('enter 1 to get working capital:')
   print('enter 2 to get Current ratio :')
   print('enter 3 to get Liquid ratio:')
   print('enter 4 to get debt to equity:')
   print('enter 5 to get Gross profit ratio:')
   print('enter 6 to get Return on equity:')
   print('enter 7 to get Return on investment:')
   print('enter 8 to display a bar graph of cashflow')
   print('enter 9 to display a pie chart of balance sheet')
   print('enter 10 to display a line chart or histogram of stocks trends')
   print('enter 11 to exit')
   cho=int(input('enter the choice:'))
   if cho==1:
      Working_capital()
   elif cho==2:
      Current_ratio()
   elif cho==3:
      Liquid_ratio()
   elif cho==4:
      debt_to_equity()
   elif cho==5:
      Gross_profit_ratio()
   elif cho==6:
      Return_on_equity()
   elif cho==7:
      Return_on_investment()
   elif cho==8:
      barofcashflow()
   elif cho==9:
      piebal()
   elif cho==10:
      stockstrend()
   elif cho==11:
      break
   else:
       print("Invalid choice")
       
