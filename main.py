from datetime import datetime
from numpy import nan
import numpy as np
import pandas as pd 

#######################

# Read data
path = '/Users/jorgesierra/Desktop/DIDi/Analyst python/service_ticket_global.csv'
df = pd.read_csv(path, sep=';')
df[['date','time']]= df.local_create_time.str.split(' ', expand= True,)
df['date']=df['date'].astype('datetime64')


#Convert 2091 values to 2021 if it's >2091-06-02 
indexNames = df[df['date'] >= '2091-05-31'].index
df.drop(indexNames , inplace=True)
df['date'] = df['date'].mask(df['date'].dt.year == 2091, df['date'] + pd.offsets.DateOffset(year=2021))

# Drop values >2021-06-02, create week number
indexNames2 = df[df['date'] >= '2021-05-31'].index
df.drop(indexNames2 , inplace=True)
df['Week_Number'] = df['date'].dt.isocalendar().week
df['Week_Number'] = df['Week_Number'].replace([df.loc[df['Week_Number']==53]],1)

df = df.sort_values(by=['name_en'])



df_tickets = df.loc[df['date']> '2021-02-28', ['name_en', 'oorder_id','date']]
df_tickets["month"] = pd.to_datetime(df["date"]).dt.month


tickets_month = pd.DataFrame(columns=['city','M1','M2','M3'])
cities = df_tickets['name_en'].drop_duplicates()
months = df_tickets['month'].drop_duplicates()

for i in range(cities.count()):
 
    count_city_month1 = df_tickets.loc[(df_tickets['name_en'] == cities.iloc[i]) & (df_tickets['month'] == months.iloc[1]),'name_en'].count()
    count_city_month2 = df_tickets.loc[(df_tickets['name_en'] == cities.iloc[i]) & (df_tickets['month'] == months.iloc[0]),'name_en'].count()
    count_city_month3 = df_tickets.loc[(df_tickets['name_en'] == cities.iloc[i]) & (df_tickets['month'] == months.iloc[2]),'name_en'].count()
    tickets_month = tickets_month.append({'city': cities.iloc[i],'M1':count_city_month1,'M2':count_city_month2,'M3':count_city_month3},ignore_index=True)

#Avg tickets of the last three months 

col = tickets_month.loc[: , "M1":"M3"]
tickets_month['avg']= col.mean(axis=1)
tickets_month_final = tickets_month.sort_values('avg', ascending=False).head(5)

#CSV
tickets_month_final.to_csv('/Users/jorgesierra/Desktop/DIDi/Analyst python/number_tickets_month.csv')

###################

#Second question 

df['Week_Day'] = df['date'].dt.day_name()
top_ten_cities = tickets_month.sort_values('avg',ascending=False).head(10).reset_index()['city']
Week_days = df['Week_Day'].drop_duplicates()

tickets_day= pd.DataFrame(columns=['city','Mon','Tue','Wed','Thu','Fri','Sat','Sun'])

#Tickets per day in the the top 10 cities

for i in range(top_ten_cities.count()):
    mon_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[2]),'name_en'].count()
    tue_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[6]),'name_en'].count()
    wed_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[3]),'name_en'].count()
    thu_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[0]),'name_en'].count()
    fri_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[5]),'name_en'].count()
    sat_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[4]),'name_en'].count()
    sun_count=df.loc[(df['name_en']==top_ten_cities.iloc[i]) & (df['Week_Day']==Week_days.iloc[1]),'name_en'].count()
    tickets_day=tickets_day.append({'city':top_ten_cities.iloc[i],'Mon':mon_count,'Tue':tue_count,'Wed':wed_count,'Thu':thu_count,'Fri':fri_count,'Sat':sat_count,'Sun':sun_count},ignore_index=True)

#Creating the CSV file

tickets_day=tickets_day.append({'city':'Avg','Mon':tickets_day['Mon'].mean(),'Tue':tickets_day['Tue'].mean(),'Wed':tickets_day['Wed'].mean(),'Thu':tickets_day['Thu'].mean(),'Fri':tickets_day['Fri'].mean(),'Sat':tickets_day['Sat'].mean(),'Sun':tickets_day['Sun'].mean()},ignore_index=True)
tickets_day[['Mon','Tue','Wed','Thu','Fri','Sat','Sun']]=tickets_day[['Mon','Tue','Wed','Thu','Fri','Sat','Sun']].astype('float')
tickets_day_final = tickets_day.T
tickets_day_final.columns = tickets_day_final.iloc[0]
tickets_day_final = tickets_day_final[1:]
Max_avg_tck_day = tickets_day_final['Avg'].astype('float').idxmax()
Max_mode_tck_day = df.loc[df['name_en'].isin(top_ten_cities),'Week_Day'].mode()
tickets_day_final.to_csv('/Users/jorgesierra/Desktop/DIDi/Analyst python/Avg_day.csv')



print('More tickets Day(Avg): ',Max_avg_tck_day)
print('More tickets Day(Mode): ',Max_mode_tck_day)

###########################

last4weeks = df.loc[df['Week_Number']>=15]

# Week 15 

week15 = last4weeks.loc[last4weeks['Week_Number']==15,'Week_Number'].count()

# Week 16 

week16 = last4weeks.loc[last4weeks['Week_Number']==16,'Week_Number'].count()

# Week 17 

week17 = last4weeks.loc[last4weeks['Week_Number']==17,'Week_Number'].count()

# Week 18

week18 = last4weeks.loc[last4weeks['Week_Number']==18,'Week_Number'].count()


growth_index = pd.DataFrame(columns=['Description','Week1','Week2','Week3','Week4'])

growth_index = growth_index.append({'Description':'Total_tkts','Week1':week15,'Week2':week16,'Week3':week17,'Week4':week18},ignore_index=True)
growth_index = growth_index.append({'Description':'Growth_index(%)','Week1':0,'Week2':0,'Week3':((week17-week16)/((week16+week17)/2))*100,'Week4':((week18-week17)/((week17+week18)/2))*100},ignore_index=True)
growth_index.to_csv('/Users/jorgesierra/Desktop/DIDi/Analyst python/growth_index.csv')




