# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:10:47 2026

@author: Felix
"""

from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tun14=pd.read_csv("stop_times_14.csv",na_filter=False,keep_default_na=False)
tun14=tun14.replace('',np.nan)
tun14=tun14.dropna()
tun14['arrival_time']=pd.to_datetime(pd.to_numeric(tun14['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
tun14['departure_time']=pd.to_datetime(pd.to_numeric(tun14['departure_time']), unit='s',origin='1970-01-01 02:00:00')


ros28=pd.read_csv("stop_times_28.csv",na_filter=False,keep_default_na=False)
ros28=ros28.replace('',np.nan)
ros28=ros28.dropna()
ros28['arrival_time']=pd.to_datetime(pd.to_numeric(ros28['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
ros28['departure_time']=pd.to_datetime(pd.to_numeric(ros28['departure_time']), unit='s',origin='1970-01-01 02:00:00')


ros28S=pd.read_csv("stop_times_28S.csv",na_filter=False,keep_default_na=False)
ros28S=ros28S.replace('',np.nan)
ros28S=ros28S.dropna()
ros28S['arrival_time']=pd.to_datetime(pd.to_numeric(ros28S['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
ros28S['departure_time']=pd.to_datetime(pd.to_numeric(ros28S['departure_time']), unit='s',origin='1970-01-01 02:00:00')


bus624=pd.read_csv("stop_times_624.csv",na_filter=False,keep_default_na=False)
bus624=bus624.replace('',np.nan)
bus624=bus624.dropna()
bus624['arrival_time']=pd.to_datetime(pd.to_numeric(bus624['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus624['departure_time']=pd.to_datetime(pd.to_numeric(bus624['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus624.dropna(axis=0,how='any')

bus626=pd.read_csv("stop_times_626.csv",na_filter=False,keep_default_na=False)
bus626=bus626.replace('',np.nan)
bus626=bus626.dropna()
bus626['arrival_time']=pd.to_datetime(pd.to_numeric(bus626['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus626['departure_time']=pd.to_datetime(pd.to_numeric(bus626['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus626.dropna(axis=0,how='any')

bus628=pd.read_csv("stop_times_628.csv",na_filter=False,keep_default_na=False)
bus628=bus628.replace('',np.nan)
bus628=bus628.dropna()
bus628['arrival_time']=pd.to_datetime(pd.to_numeric(bus628['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus628['departure_time']=pd.to_datetime(pd.to_numeric(bus628['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus628.dropna(axis=0,how='any')

bus629=pd.read_csv("stop_times_629.csv",na_filter=False,keep_default_na=False)
bus629=bus629.replace('',np.nan)
bus629=bus629.dropna()
bus629['arrival_time']=pd.to_datetime(pd.to_numeric(bus629['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus629['departure_time']=pd.to_datetime(pd.to_numeric(bus629['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus629.dropna(axis=0,how='any')

bus670=pd.read_csv("stop_times_670.csv",na_filter=False,keep_default_na=False)
bus670=bus670.replace('',np.nan)
bus670=bus670.dropna()
bus670['arrival_time']=pd.to_datetime(pd.to_numeric(bus670['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus670['departure_time']=pd.to_datetime(pd.to_numeric(bus670['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus670=bus670.dropna()

bus670X=pd.read_csv("stop_times_670X.csv",na_filter=False,keep_default_na=False)
bus670X=bus670X.replace('',np.nan)
bus670X=bus670X.dropna()
bus670X['arrival_time']=pd.to_datetime(pd.to_numeric(bus670X['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus670X['departure_time']=pd.to_datetime(pd.to_numeric(bus670X['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus670X.dropna(axis=0,how='any')

bus676=pd.read_csv("stop_times_676.csv",na_filter=False,keep_default_na=False)
bus676=bus676.replace('',np.nan)
bus676=bus676.dropna()
bus676['arrival_time']=pd.to_datetime(pd.to_numeric(bus676['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus676['departure_time']=pd.to_datetime(pd.to_numeric(bus676['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus676.dropna(axis=0,how='any')

bus676X=pd.read_csv("stop_times_676X.csv",na_filter=False,keep_default_na=False)
bus676X=bus676X.replace('',np.nan)
bus676X=bus676X.dropna()
bus676X['arrival_time']=pd.to_datetime(pd.to_numeric(bus676X['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus676X['departure_time']=pd.to_datetime(pd.to_numeric(bus676X['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus676X.dropna(axis=0,how='any')

bus680=pd.read_csv("stop_times_680.csv",na_filter=False,keep_default_na=False)
bus680=bus680.replace('',np.nan)
bus680=bus680.dropna()
bus680['arrival_time']=pd.to_datetime(pd.to_numeric(bus680['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus680['departure_time']=pd.to_datetime(pd.to_numeric(bus680['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus680=bus680.dropna()

bus694=pd.read_csv("stop_times_694.csv",na_filter=False,keep_default_na=False)
bus694=bus694.replace('',np.nan)
bus694=bus694.dropna()
bus694['arrival_time']=pd.to_datetime(pd.to_numeric(bus694['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus694['departure_time']=pd.to_datetime(pd.to_numeric(bus694['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus694.dropna(axis=0,how='any')

bus699=pd.read_csv("stop_times_699.csv",na_filter=False,keep_default_na=False)
bus699=bus699.replace('',np.nan)
bus699=bus699.dropna()
bus699['arrival_time']=pd.to_datetime(pd.to_numeric(bus699['arrival_time']), unit='s',origin='1970-01-01 02:00:00')
bus699['departure_time']=pd.to_datetime(pd.to_numeric(bus699['departure_time']), unit='s',origin='1970-01-01 02:00:00')
bus699.dropna(axis=0,how='any')
                                        
#filter
filterlist=['Arninge','Arninge station','Roslags Näsby','Roslags Näsby trafikplats','Danderyds sjukhus','Mörby','Universitetet','Universitetet norra','Universitetet södra','Stockholms östra','Tekniska högskolan']

tun14=tun14[(tun14['stop_name'].isin(filterlist))]

ros28=ros28[(ros28['stop_name'].isin(filterlist))]
ros28S=ros28S[(ros28S['stop_name'].isin(filterlist))]

bus624=bus624[(bus624['stop_name'].isin(filterlist))]
bus626=bus626[(bus626['stop_name'].isin(filterlist))]
bus628=bus628[(bus628['stop_name'].isin(filterlist))]
bus629=bus629[(bus629['stop_name'].isin(filterlist))]
bus670=bus670[(bus670['stop_name'].isin(filterlist))]
bus670X=bus670X[(bus670X['stop_name'].isin(filterlist))]
bus676=bus676[(bus676['stop_name'].isin(filterlist))]
bus676X=bus676X[(bus676X['stop_name'].isin(filterlist))]
bus680=bus680[(bus680['stop_name'].isin(filterlist))]
bus694=bus694[(bus694['stop_name'].isin(filterlist))]
bus699=bus699[(bus699['stop_name'].isin(filterlist))]


# %%28stk


#-----------------------------------------------------------

arn1=ros28.loc[ros28.stop_name=='Arninge']
arn1=arn1.loc[arn1.direction_id==1]
stk1=ros28.loc[ros28.stop_name=='Stockholms östra']
stk1=stk1.loc[stk1.direction_id==1]

t28=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=stk1[(stk1['trip_id']==num) & (stk1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
ros281=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%28arn

arn2=ros28.loc[ros28.stop_name=='Arninge']
arn2=arn2.loc[arn2.direction_id==0]
stk2=ros28.loc[ros28.stop_name=='Stockholms östra']
stk2=stk2.loc[stk2.direction_id==0]

t28=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=stk2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==stk2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=stk2.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
ros282=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%28Sstk

arn1=ros28S.loc[ros28S.stop_name=='Arninge']
arn1=arn1.loc[arn1.direction_id==1]
stk1=ros28S.loc[ros28S.stop_name=='Stockholms östra']
stk1=stk1.loc[stk1.direction_id==1]

t28=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=stk1[(stk1['trip_id']==num) & (stk1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
ros28S1=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%28Sarn

arn2=ros28S.loc[ros28S.stop_name=='Arninge']
arn2=arn2.loc[arn2.direction_id==0]
stk2=ros28S.loc[ros28S.stop_name=='Stockholms östra']
stk2=stk2.loc[stk2.direction_id==0]

t28=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=stk2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==stk2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=stk2.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
ros28S2=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%670stk

arn1=bus670.loc[bus670.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
stk1=bus670.loc[bus670.stop_name=='Tekniska högskolan']
stk1=stk1.loc[stk1.direction_id==0]

t28=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=stk1[(stk1['trip_id']==num) & (stk1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6701=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%670arn

arn2=bus670.loc[bus670.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
stk2=bus670.loc[bus670.stop_name=='Tekniska högskolan']
stk2=stk2.loc[stk2.direction_id==1]

t28=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=stk2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==stk2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=stk2.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6702=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%676stk

arn1=bus676.loc[bus676.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
stk1=bus676.loc[bus676.stop_name=='Tekniska högskolan']
stk1=stk1.loc[stk1.direction_id==0]

t28=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=stk1[(stk1['trip_id']==num) & (stk1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6761=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%676arn

arn2=bus676.loc[bus676.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
stk2=bus676.loc[bus676.stop_name=='Tekniska högskolan']
stk2=stk2.loc[stk2.direction_id==1]

t28=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=stk2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==stk2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=stk2.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6762=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%680stk

arn1=bus680.loc[bus680.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
stk1=bus680.loc[bus680.stop_name=='Tekniska högskolan']
stk1=stk1.loc[stk1.direction_id==0]

t28=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=stk1[(stk1['trip_id']==num) & (stk1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6801=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%680arn

arn2=bus680.loc[bus680.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
stk2=bus680.loc[bus680.stop_name=='Tekniska högskolan']
stk2=stk2.loc[stk2.direction_id==1]

t28=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=stk2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==stk2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=stk2.iloc[i]
    t=int((s['arrival_time']-a['departure_time']).total_seconds())
    t28.append(t)
    h28.append(int(a['departure_time'].time().hour))
bus6802=pd.DataFrame({'Hour':h28,'Travel_time':t28})

# %%tunnelbana

tundyd1=tun14.loc[tun14.stop_name=='Danderyds sjukhus']
tundyd1=tundyd1.loc[tundyd1.direction_id==0]
tunstk1=tun14.loc[tun14.stop_name=='Tekniska högskolan']
tunstk1=tunstk1.loc[tunstk1.direction_id==0]

tundyd2=tun14.loc[tun14.stop_name=='Danderyds sjukhus']
tundyd2=tundyd2.loc[tundyd2.direction_id==1]
tunstk2=tun14.loc[tun14.stop_name=='Tekniska högskolan']
tunstk2=tunstk2.loc[tunstk2.direction_id==1]

# %%624stk

arn1=bus624.loc[bus624.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus624.loc[bus624.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)].iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6241=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%624arn

arn2=bus624.loc[bus624.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus624.loc[bus624.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6242=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%626stk

arn1=bus626.loc[bus626.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus626.loc[bus626.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)].iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6261=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%626arn

arn2=bus626.loc[bus626.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus626.loc[bus626.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6262=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%628stk

arn1=bus628.loc[bus628.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus628.loc[bus628.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)].iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6281=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%628arn

arn2=bus628.loc[bus628.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus628.loc[bus628.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6282=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%629stk

arn1=bus629.loc[bus629.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus629.loc[bus629.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)].iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6291=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%624arn

arn2=bus629.loc[bus629.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus629.loc[bus629.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus6292=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%670tunstk

arn1=bus670.loc[bus670.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus670.loc[bus670.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus670tun1=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%670tunarn

arn2=bus670.loc[bus670.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus670.loc[bus670.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus670tun2=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%670Xtunstk

arn1=bus670X.loc[bus670X.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus670X.loc[bus670X.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus670Xtun1=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%670Xtunarn

arn2=bus670X.loc[bus670X.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus670X.loc[bus670X.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus670Xtun2=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%676tunstk

arn1=bus676.loc[bus676.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus676.loc[bus676.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus676tun1=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%676tunarn

arn2=bus676.loc[bus676.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus676.loc[bus676.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus676tun2=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%676Xtunstk

arn1=bus676X.loc[bus676X.stop_name=='Arninge station']
arn1=arn1.loc[arn1.direction_id==0]
dyd1=bus676X.loc[bus676X.stop_name=='Danderyds sjukhus']
dyd1=dyd1.loc[dyd1.direction_id==0]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn1), len(stk1))):
    num=arn1['trip_id'].iloc[i]
    s=dyd1[(dyd1['trip_id']==num) & (dyd1['start_date']==arn1['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=arn1.iloc[i]
    numtun=tundyd1[(tundyd1['departure_time']>s['arrival_time'])]
    numtun=numtun[((numtun['departure_time']-s['arrival_time'])>('0 days 00:02:00'))].iloc[0]
    numtunnel=numtun['trip_id']
    tun=tunstk1[((tunstk1['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==arn1['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((tun['arrival_time']-a['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((tun['arrival_time']-numtun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus676Xtun1=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%676Xtunarn

arn2=bus676X.loc[bus676X.stop_name=='Arninge station']
arn2=arn2.loc[arn2.direction_id==1]
dyd2=bus676X.loc[bus676X.stop_name=='Danderyds sjukhus']
dyd2=dyd2.loc[dyd2.direction_id==1]


t28=[]
tdyd28=[]
ttunnel=[]
h28=[]
for i in range(0,min(len(arn2), len(stk2))):
    num=dyd2['trip_id'].iloc[i]
    s=arn2[(arn2['trip_id']==num) & (arn2['start_date']==dyd2['start_date'].iloc[i])]
    if s.empty==True:
        continue
    s=s.iloc[0]
    a=dyd2.iloc[i]
    numtun=tundyd2[(tundyd2['arrival_time']<a['departure_time'])]
    numtun=numtun[((a['departure_time']-numtun['arrival_time'])>('0 days 00:02:00'))].iloc[-1]
    numtunnel=numtun['trip_id']
    tun=tunstk2[((tunstk2['trip_id']==numtunnel) & True)]
    tun=tun[((tun['start_date']==dyd2['start_date'].iloc[i]) & True)]
    if tun.empty==True:
        continue
    tun=tun.iloc[0]
    t=int((s['arrival_time']-tun['departure_time']).total_seconds())
    tdyd=int((s['arrival_time']-a['departure_time']).total_seconds())
    ttun=int((numtun['arrival_time']-tun['departure_time']).total_seconds())
    t28.append(t)
    tdyd28.append(tdyd)
    ttunnel.append(ttun)
    h28.append(int(a['departure_time'].time().hour))
bus676Xtun2=pd.DataFrame({'Hour':h28,'Travel_time':t28,'Travel_time_dyd':tdyd28,'Travel_time_tun':ttunnel})

# %%mean full distance

h=[]
m128=[]
s128=[]
m228=[]
s228=[]

m128S=[]
s128S=[]
m228S=[]
s228S=[]

m1670=[]
s1670=[]
m2670=[]
s2670=[]

m1676=[]
s1676=[]
m2676=[]
s2676=[]

m1680=[]
s1680=[]
m2680=[]
s2680=[]
for i in range(4,25):
    h.append(i)
    m128.append(round(ros281.Travel_time[ros281['Hour']==i].mean(),0))
    s128.append(round(ros281.Travel_time[ros281['Hour']==i].std(),0))
    m228.append(round(ros282.Travel_time[ros282['Hour']==i].mean(),0))
    s228.append(round(ros282.Travel_time[ros282['Hour']==i].std(),0))
    
    m128S.append(round(ros28S1.Travel_time[ros28S1['Hour']==i].mean(),0))
    s128S.append(round(ros28S1.Travel_time[ros28S1['Hour']==i].std(),0))
    m228S.append(round(ros28S2.Travel_time[ros28S2['Hour']==i].mean(),0))
    s228S.append(round(ros28S2.Travel_time[ros28S2['Hour']==i].std(),0))
    
    m1670.append(round(bus6701.Travel_time[bus6701['Hour']==i].mean(),0))
    s1670.append(round(bus6701.Travel_time[bus6701['Hour']==i].std(),0))
    m2670.append(round(bus6702.Travel_time[bus6702['Hour']==i].mean(),0))
    s2670.append(round(bus6702.Travel_time[bus6702['Hour']==i].std(),0))
    
    m1676.append(round(bus6761.Travel_time[bus6761['Hour']==i].mean(),0))
    s1676.append(round(bus6761.Travel_time[bus6761['Hour']==i].std(),0))
    m2676.append(round(bus6762.Travel_time[bus6762['Hour']==i].mean(),0))
    s2676.append(round(bus6762.Travel_time[bus6762['Hour']==i].std(),0))
    
    m1680.append(round(bus6801.Travel_time[bus6801['Hour']==i].mean(),0))
    s1680.append(round(bus6801.Travel_time[bus6801['Hour']==i].std(),0))
    m2680.append(round(bus6802.Travel_time[bus6802['Hour']==i].mean(),0))
    s2680.append(round(bus6802.Travel_time[bus6802['Hour']==i].std(),0))

total_runtime=pd.DataFrame({'Hour':h,'m128':m128,'s128':s128,'m228':m228,'s228':s228,
                            'm128S':m128S,'s128S':s128S,'m228S':m228S,'s228S':s228S,
                            'm1670':m1670,'s1670':s1670,'m2670':m2670,'s2670':s2670,
                            'm1676':m1676,'s1676':s1676,'m2676':m2676,'s2676':s2676,
                            'm1680':m1680,'s1680':s1680,'m2680':m2680,'s2680':s2680})
    

# %% mean tunnel

h=[]
m1624=[]
s1624=[]
m1624d=[]
s1624d=[]
m2624=[]
s2624=[]
m2624d=[]
s2624d=[]

m1626=[]
s1626=[]
m1626d=[]
s1626d=[]
m2626=[]
s2626=[]
m2626d=[]
s2626d=[]

m1628=[]
s1628=[]
m1628d=[]
s1628d=[]
m2628=[]
s2628=[]
m2628d=[]
s2628d=[]

m1629=[]
s1629=[]
m1629d=[]
s1629d=[]
m2629=[]
s2629=[]
m2629d=[]
s2629d=[]

m1670=[]
s1670=[]
m1670d=[]
s1670d=[]
m2670=[]
s2670=[]
m2670d=[]
s2670d=[]

m1670X=[]
s1670X=[]
m1670Xd=[]
s1670Xd=[]
m2670X=[]
s2670X=[]
m2670Xd=[]
s2670Xd=[]

m1676=[]
s1676=[]
m1676d=[]
s1676d=[]
m2676=[]
s2676=[]
m2676d=[]
s2676d=[]

m1676X=[]
s1676X=[]
m1676Xd=[]
s1676Xd=[]
m2676X=[]
s2676X=[]
m2676Xd=[]
s2676Xd=[]

for i in range(4,25):
    h.append(i)
    m1624.append(round(bus6241.Travel_time[bus6241['Hour']==i].mean(),0))
    s1624.append(round(bus6241.Travel_time[bus6241['Hour']==i].std(),0))
    m1624d.append(round(bus6241.Travel_time_dyd[bus6241['Hour']==i].mean(),0))
    s1624d.append(round(bus6241.Travel_time_dyd[bus6241['Hour']==i].std(),0))
    m2624.append(round(bus6242.Travel_time[bus6242['Hour']==i].mean(),0))
    s2624.append(round(bus6242.Travel_time[bus6242['Hour']==i].std(),0))
    m2624d.append(round(bus6242.Travel_time_dyd[bus6242['Hour']==i].mean(),0))
    s2624d.append(round(bus6242.Travel_time_dyd[bus6242['Hour']==i].std(),0))
    
    m1626.append(round(bus6261.Travel_time[bus6261['Hour']==i].mean(),0))
    s1626.append(round(bus6261.Travel_time[bus6261['Hour']==i].std(),0))
    m1626d.append(round(bus6261.Travel_time_dyd[bus6261['Hour']==i].mean(),0))
    s1626d.append(round(bus6261.Travel_time_dyd[bus6261['Hour']==i].std(),0))
    m2626.append(round(bus6262.Travel_time[bus6262['Hour']==i].mean(),0))
    s2626.append(round(bus6262.Travel_time[bus6262['Hour']==i].std(),0))
    m2626d.append(round(bus6262.Travel_time_dyd[bus6262['Hour']==i].mean(),0))
    s2626d.append(round(bus6262.Travel_time_dyd[bus6262['Hour']==i].std(),0))
    
    m1628.append(round(bus6281.Travel_time[bus6281['Hour']==i].mean(),0))
    s1628.append(round(bus6281.Travel_time[bus6281['Hour']==i].std(),0))
    m1628d.append(round(bus6281.Travel_time_dyd[bus6281['Hour']==i].mean(),0))
    s1628d.append(round(bus6281.Travel_time_dyd[bus6281['Hour']==i].std(),0))
    m2628.append(round(bus6282.Travel_time[bus6282['Hour']==i].mean(),0))
    s2628.append(round(bus6282.Travel_time[bus6282['Hour']==i].std(),0))
    m2628d.append(round(bus6282.Travel_time_dyd[bus6282['Hour']==i].mean(),0))
    s2628d.append(round(bus6282.Travel_time_dyd[bus6282['Hour']==i].std(),0))
    
    m1629.append(round(bus6291.Travel_time[bus6291['Hour']==i].mean(),0))
    s1629.append(round(bus6291.Travel_time[bus6291['Hour']==i].std(),0))
    m1629d.append(round(bus6291.Travel_time_dyd[bus6291['Hour']==i].mean(),0))
    s1629d.append(round(bus6291.Travel_time_dyd[bus6291['Hour']==i].std(),0))
    m2629.append(round(bus6292.Travel_time[bus6292['Hour']==i].mean(),0))
    s2629.append(round(bus6292.Travel_time[bus6292['Hour']==i].std(),0))
    m2629d.append(round(bus6292.Travel_time_dyd[bus6292['Hour']==i].mean(),0))
    s2629d.append(round(bus6292.Travel_time_dyd[bus6292['Hour']==i].std(),0))
    
    m1670.append(round(bus670tun1.Travel_time[bus670tun1['Hour']==i].mean(),0))
    s1670.append(round(bus670tun1.Travel_time[bus670tun1['Hour']==i].std(),0))
    m1670d.append(round(bus670tun1.Travel_time_dyd[bus670tun1['Hour']==i].mean(),0))
    s1670d.append(round(bus670tun1.Travel_time_dyd[bus670tun1['Hour']==i].std(),0))
    m2670.append(round(bus670tun2.Travel_time[bus670tun2['Hour']==i].mean(),0))
    s2670.append(round(bus670tun2.Travel_time[bus670tun2['Hour']==i].std(),0))
    m2670d.append(round(bus670tun2.Travel_time_dyd[bus670tun2['Hour']==i].mean(),0))
    s2670d.append(round(bus670tun2.Travel_time_dyd[bus670tun2['Hour']==i].std(),0))
    
    m1670X.append(round(bus670Xtun1.Travel_time[bus670Xtun1['Hour']==i].mean(),0))
    s1670X.append(round(bus670Xtun1.Travel_time[bus670Xtun1['Hour']==i].std(),0))
    m1670Xd.append(round(bus670Xtun1.Travel_time_dyd[bus670Xtun1['Hour']==i].mean(),0))
    s1670Xd.append(round(bus670Xtun1.Travel_time_dyd[bus670Xtun1['Hour']==i].std(),0))
    m2670X.append(round(bus670Xtun2.Travel_time[bus670Xtun2['Hour']==i].mean(),0))
    s2670X.append(round(bus670Xtun2.Travel_time[bus670Xtun2['Hour']==i].std(),0))
    m2670Xd.append(round(bus670Xtun2.Travel_time_dyd[bus670Xtun2['Hour']==i].mean(),0))
    s2670Xd.append(round(bus670Xtun2.Travel_time_dyd[bus670Xtun2['Hour']==i].std(),0))
    
    m1676.append(round(bus676tun1.Travel_time[bus676tun1['Hour']==i].mean(),0))
    s1676.append(round(bus676tun1.Travel_time[bus676tun1['Hour']==i].std(),0))
    m1676d.append(round(bus676tun1.Travel_time_dyd[bus676tun1['Hour']==i].mean(),0))
    s1676d.append(round(bus676tun1.Travel_time_dyd[bus676tun1['Hour']==i].std(),0))
    m2676.append(round(bus676tun2.Travel_time[bus676tun2['Hour']==i].mean(),0))
    s2676.append(round(bus676tun2.Travel_time[bus676tun2['Hour']==i].std(),0))
    m2676d.append(round(bus676tun2.Travel_time_dyd[bus676tun2['Hour']==i].mean(),0))
    s2676d.append(round(bus676tun2.Travel_time_dyd[bus670tun2['Hour']==i].std(),0))
    
    m1676X.append(round(bus676Xtun1.Travel_time[bus676Xtun1['Hour']==i].mean(),0))
    s1676X.append(round(bus676Xtun1.Travel_time[bus676Xtun1['Hour']==i].std(),0))
    m1676Xd.append(round(bus676Xtun1.Travel_time_dyd[bus676Xtun1['Hour']==i].mean(),0))
    s1676Xd.append(round(bus676Xtun1.Travel_time_dyd[bus676Xtun1['Hour']==i].std(),0))
    m2676X.append(round(bus676Xtun2.Travel_time[bus676Xtun2['Hour']==i].mean(),0))
    s2676X.append(round(bus676Xtun2.Travel_time[bus676Xtun2['Hour']==i].std(),0))
    m2676Xd.append(round(bus676Xtun2.Travel_time_dyd[bus676Xtun2['Hour']==i].mean(),0))
    s2676Xd.append(round(bus676Xtun2.Travel_time_dyd[bus676Xtun2['Hour']==i].std(),0))
    
total_runtime_tun=pd.DataFrame({'Hour':h,'m1624':m1624,'s1624':s1624,'m1624d':m1624d,'s1624d':s1624d,
                                'm2624':m2624,'s2624':s2624,'m2624d':m2624d,'s2624d':s2624d,
                                'm1626':m1626,'s1626':s1626,'m1626d':m1626d,'s1626d':s1626d,
                                'm2626':m2626,'s2626':s2626,'m2626d':m2626d,'s2626d':s2626d,
                                'm1628':m1628,'s1628':s1628,'m1628d':m1628d,'s1628d':s1628d,
                                'm2628':m2628,'s2628':s2628,'m2628d':m2628d,'s2628d':s2628d,
                                'm1629':m1629,'s1629':s1629,'m1629d':m1629d,'s1629d':s1629d,
                                'm2629':m2629,'s2629':s2629,'m2629d':m2629d,'s2629d':s2629d,
                                'm1670':m1670,'s1670':s1670,'m1670d':m1670d,'s1670d':s1670d,
                                'm2670':m2670,'s2670':s2670,'m2670d':m2670d,'s2670d':s2670d,
                                'm1670X':m1670X,'s1670X':s1670X,'m1670Xd':m1670Xd,'s1670Xd':s1670Xd,
                                'm2670X':m2670X,'s2670X':s2670X,'m2670Xd':m2670Xd,'s2670Xd':s2670Xd,
                                'm1676':m1676,'s1676':s1676,'m1676d':m1676d,'s1676d':s1676d,
                                'm2676':m2676,'s2676':s2676,'m2676d':m2676d,'s2676d':s2676d,
                                'm1676X':m1676X,'s1676X':s1676X,'m1676Xd':m1676Xd,'s1676Xd':s1676Xd,
                                'm2676X':m2676X,'s2676X':s2676X,'m2676Xd':m2676Xd,'s2676Xd':s2676Xd})
    

# %%actual plots

plt.plot(total_runtime['Hour'],total_runtime['m128'],'b-',
         total_runtime['Hour'],total_runtime['m128S'],'b--',
         total_runtime['Hour'],total_runtime['m1670'],'r-',
         total_runtime['Hour'],total_runtime['m1676'],'r-',
         total_runtime['Hour'],total_runtime['m1680'],'r-',)

plt.figure()
plt.plot(total_runtime['Hour'],total_runtime['m228'],'b-',
         total_runtime['Hour'],total_runtime['m228S'],'b--',
         total_runtime['Hour'],total_runtime['m2670'],'r-',
         total_runtime['Hour'],total_runtime['m2676'],'r-',
         total_runtime['Hour'],total_runtime['m2680'],'r-',)

plt.figure()
plt.plot(total_runtime_tun['Hour'],total_runtime_tun['m1624'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1626'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1628'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1629'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1670'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m1670X'],'b--',
         total_runtime_tun['Hour'],total_runtime_tun['m1676'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m1676X'],'b--',)

plt.figure()
plt.plot(total_runtime_tun['Hour'],total_runtime_tun['m1624d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1626d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1628d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1629d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m1670d'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m1670Xd'],'b--',
         total_runtime_tun['Hour'],total_runtime_tun['m1676d'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m1676Xd'],'b--',)

plt.figure()
plt.plot(total_runtime_tun['Hour'],total_runtime_tun['m2624'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2626'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2628'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2629'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2670'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m2670X'],'b--',
         total_runtime_tun['Hour'],total_runtime_tun['m2676'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m2676X'],'b--',)

plt.figure()
plt.plot(total_runtime_tun['Hour'],total_runtime_tun['m2624d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2626d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2628d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2629d'],'r-',
         total_runtime_tun['Hour'],total_runtime_tun['m2670d'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m2670Xd'],'b--',
         total_runtime_tun['Hour'],total_runtime_tun['m2676d'],'b-',
         total_runtime_tun['Hour'],total_runtime_tun['m2676Xd'],'b--',)



