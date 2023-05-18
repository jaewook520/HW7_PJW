import pandas as pd
import numpy as np

def main():
    df = pd.DataFrame({'unit price':[1000,280,900], 'number':[25,120,30]}, index=['store1', 'store2','store3'])
    print(df)
    print()
    df['total price'] = np.prod(df, axis=1)
    print(df)
    print()
    df = df.sort_values(by="total price", ascending = False)
    print(df.head(2))

if __name__=="__main__":
    main()
