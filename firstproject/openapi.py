import json
import requests

client_secret='M3DN4Sqler'
client_id='kl_ECfp5_4AkL7sTmbAg'

url = 'https://openapi.naver.com/v1/datalab/search'
header = {
  'X-Naver-Client-Id': client_id,
  'X-Naver-Client-Secret': client_secret,
  'Content-Type': 'application/json'
}

data = {
  'startDate':'2021-01-01',
  'endDate':'2021-12-31',
  'timeUnit':'week',
  'keywordGroups':[
    {
      'groupName':'이재명',
      'keywords':['더불어민주당','이재명',]
    },
    {
      'groupName':'윤석열',
      'keywords':['국민의힘','윤석열']
    },
    {
      'groupName':'허경영',
      'keywords':['국가혁명당','허경영']
    },
    {
      'groupName':'안철수',
      'keywords':['국민의당','안철수']
    },
    {
      'groupName':'심상정',
      'keywords':['정의당','심상정']
    },
  ],
  'ages':['3', '4', '5', '6', '7', '8', '9', '10', '11']
}

import pandas as pd
result=response.json()
lee=pd.DataFrame(result['results'][0]['data'])
lee.rename(columns={'ratio':'lee'}, inplace=True)
lee

yoon=pd.DataFrame(result['results'][1]['data'])
yoon.rename(columns={'ratio':'yoon'}, inplace=True)
yoon

huh=pd.DataFrame(result['results'][2]['data'])
huh.rename(columns={'ratio':'huh'}, inplace=True)
huh

ahn = pd.DataFrame( result['results'][3]['data'] )
ahn.rename( columns={'ratio':'ahn'}, inplace=True )
ahn

sim=pd.DataFrame(result['results'][4]['data'])
sim.rename(columns={'ratio':'sim'}, inplace=True)
sim

rawData=pd.merge(left=lee,right=yoon,on='period')
rawData=pd.merge(left=rawData,right=huh, on='period')
rawData=pd.merge(left=rawData,right=ahn, on='period')
rawData=pd.merge(left=rawData,right=sim, on='period')
rawData

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure( figsize=(15,5) )
sns.lineplot(data=rawData, x='period', y='lee')
plt.xticks(rotation=180)

plt.figure( figsize=(20,5) )
sns.lineplot(data=rawData, x='period', y='lee', label='lee')
sns.lineplot(data=rawData, x='period', y='yoon', label='yoon')
sns.lineplot(data=rawData, x='period', y='huh', label='huh')
sns.lineplot(data=rawData, x='period', y='ahn', label='ahn')
sns.lineplot(data=rawData, x='period', y='sim', label='sim')

plt.ylabel('trend')
plt.xticks(rotation=30)
plt.legend()

plt.show()

!pip install xmltodict

import requests
import xmltodict

serviceKey = '9Td+AysuLzv3Fq4/SIhE/ri4rGiZiFjD92SQxmfQalI/2vW3xPEOcSNURc+LUMqpgZoCrTL8gD1mXFb1QhXBIg=='
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
result=xmltodict.parse(response.text)
result

for row in result['response']['body']['items']['item']:
  print('날짜:', row['createDt'], '지역:', row['gubun'], '사망자 수:', row['deathCnt'], '확진자 수:', row['defCnt'])

confirmed={}
for row in result['response']['body']['items']['item']:
  key=row['createDt'].split(' ')[0]
  if key in confirmed.keys():
    confirmed[key][row['gubun']]=row['defCnt']
  else:
    confirmed[key]={}
    confirmed[key][row['gubun']]=row['defCnt']
confirmed

from collections import defaultdict
confirm = defaultdict(dict)

for row in result['response']['body']['items']['item']:
  key = row['createDt'].split(' ')[0]
  locate = row['gubun']
  if locate != '검역' and locate != '합계':
    confirm[key][locate] = row['defCnt']
confirm

import pandas as pd
pd.DataFrame(confirm).T.sort_index()

from collections import defaultdict
death = defaultdict(dict)

for row in result['response']['body']['items']['item']:
  key = row['createDt'].split(' ')[0]
  locate = row['gubun']
  if locate != '검역' and locate != '합계':
    death[key][locate] = row['deathCnt']
pd.DataFrame(death).T.sort_index()

import pickle
with open('/content/drive/MyDrive/멀티캠퍼스 조경상/confirm.pk','wb')as file:
  pickle.dump(confirm, file)
with open('/content/drive/MyDrive/멀티캠퍼스 조경상/confirm.pk','rb')as file:
  rawData=pickle.load(file)
rawData

import json
with open('/content/drive/MyDrive/멀티캠퍼스 조경상/confirm.json','w')as file:
  json.dump(confirm, file)
with open('/content/drive/MyDrive/멀티캠퍼스 조경상/confirm.json','r')as file:
  rawData=json.load(file)
rawData


