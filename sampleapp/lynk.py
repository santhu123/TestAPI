#pip install pandas
import pandas as pd
import json
from pandas.io.json import json_normalize

with open('Mouni.json') as json_file:
    newdata=json.load(json_file)
data=json.loads(newdata[0])
mydata=data["analysis"]
mylist=[]
df=pd.json_normalize(mydata,'timeseries','company_name')
df1=pd.json_normalize(mydata,'networks','company_name')



results=pd.merge(df,df1,on='company_name')
results.to_csv('MYFineTest.csv',index=False)


# from the post man..there we have to giv one json file ..

# api---read the file from the request  
# how do u process file 




# df.to_csv('dftest.csv',index=False)
#df1.to_csv('dftest1.csv',index=False)

#frames=[df,df1]

#result=pd.concat(frames,axis=0)
#result.to_csv('finalop.csv',index=False)
#concatenation of data frames
## u need to do Flatten the JSON


# json.loads('list')---op will list
# json.loads('dict') --op dict
    