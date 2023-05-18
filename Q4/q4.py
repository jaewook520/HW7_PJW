import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('gender2.csv', encoding='ANSI', index_col=0)
    df = df.loc[:,['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']]
    df.columns = ['Total','Male','Female']
    print(df)
    
if __name__=="__main__":
    main()
