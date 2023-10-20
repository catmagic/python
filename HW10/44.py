import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


def my_dummies(names):
    names_collectable=[name for name in set(names)]
    df = pd.DataFrame({name:[bool(0) for i in range(len(names))]for name in names_collectable})
    for i in range(len(names)):
        df.at[i,names[i]]=bool(1)
    return df
s=my_dummies(data['whoAmI'])
s
