import pandas as pd
import statsmodels.api as sm

def cgmac(data=None,lag=None):
    df =data
    AC= pd.DataFrame()
    for i in range (0,len(df.iloc[:,0])):
        X = df.iloc[i,2:]
        dff=pd.DataFrame(sm.tsa.stattools.acf(X,nlags=lag,fft=False))
        AC=pd.concat([AC, pd.DataFrame([df.iloc[i,0],X.mean(),X.std(),dff.iloc[1:].mean()[0],dff.iloc[1:].var()[0]]).T])
    AC=AC.rename(columns={0: 'ID'}).rename(columns={1: 'Mean'}).rename(columns={2: 'Std'}).rename(columns={3: 'AC_Mean'}).rename(columns={4: 'AC_Var'})
    return AC
  
