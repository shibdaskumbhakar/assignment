# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:55:31 2019

@author: SHIBDAS KUMBHAKAR

In This data set mostly delay values are null so I neglect the all null value. 
then I fetch the  trip_start_time data and find the month from date and collect only month and saved in a variable
i plot positive and negative delay values in one bar chat .
then Find Top 3 source form the response value and Find Top 3 distination form the response value
"""
from collections import Counter
import matplotlib.pyplot as plt
import requests
import json
import numpy as np



#send reques to
a=requests.get('https://asia-east2-greentoad-bfbb7.cloudfunctions.net/apiIndia/api/angular')
b=json.loads(a.text)

#fatch delay data
delay_data=[i['delay'] for i in b]
delay_data=list(dict.fromkeys(delay_data))
delay_data.pop(0)

#fatch trip start time
date_time=[i['trip_start_time'] for i in b]


month=[] #collect month from trip_start_time

#split all date time and collect only month
for i in date_time:
 
    c=i.split(":")
    
    d=c[0]
    
    e=d.split("-")
   
    f=e[1]
    
    month.append(f)
    
x=month[0:116]
x.sort()


#plot bar chart
plt.bar(x,delay_data , color='red')
plt.title('delay report')
plt.xlabel('month')
plt.ylabel('delay')
plt.show()













#top 3 source
source=[i['srcname'] for i in b]
lst=source
c = Counter(lst)

high = c.most_common(3)

print("Top 3 source are:")
print(high)



#top 3 destination
Destination=[i['destname'] for i in b]
lst1=Destination
d = Counter(lst1)

high1 = d.most_common(3) 
print("Top 3 destination are:") 
print(high1)






