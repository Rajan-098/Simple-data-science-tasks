# from sklearn import linear_model
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# #df=pd.DataFrame({'area':np.array([2600,3000,3200,3600,4000]).reshape(1,5),'price':np.array([550000,565000,610000,680000,725000]).reshape(1, 5)})
# #area=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,20]
# #price=[100,200,333,455,600,765,864,900,1001,2001,3546,4865,6815,7654,8282,9000,10101,11000,12000]
# #plt.scatter(df[["area"]],df.price,color="red",marker="+")
# #plt.show()
# ##reg=linear_model.LinearRegression()
# ##reg.fit(df[['area']],df.price)
# ##print(reg.predict(205937))

# df=pd.read_csv(r"C:\Users\RAJAN\Desktop\DS\csv\IP_DATA_ALL.csv",low_memory=False)
# df=df.head(1000)
# print(df.head(len(df)))
# print(df.describe())
# print(df.columns)

# country_name=[]
# country_len=[]
# country_places=[]
# group=df.groupby("Country")
# for name,table in group:
#     country_places.append(table)
#     country_len.append(len(table))
#     country_name.append(name)
# i=1

# for name in country_places:
#     city_table_list=[]
#     city_name_len=[]
#     city_name_list=[]
#     for city_name,city_table in name.groupby("Place.Name"):
#         city_name_len.append(len(city_table))
#         city_table_list.append(city_table)
#         city_name_list.append(city_name)
#     plt.subplot(100+i)
#     plt.bar(city_name_list,city_name_len)
#     i+=1
# #plt.bar(country_name,country_len)
# plt.show()
import pandas as pd
import seaborn as sns
df=pd.read_csv(r"C:\Users\RAJAN\Desktop\DS\csv\datasets.csv")
print(df.columns)
print(df)
print(df[['categoryName']].head(50))
print(df.drop_duplicates().head(60))
print(df[not df['vintage'].isnull()])
print(df[df['vintage'].isnull()])# or df['cloud'].isnull()])
print(df['about'].values())
print(df.dropna(inplace=False))
print()
