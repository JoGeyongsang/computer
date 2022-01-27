import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

!pip install xmltodict

import requests
import xmltodict

from matplotlib import font_manager, rcParams
!apt-get install fonts-nanum*
rcParams['font.family'] = 'NanumGothicCoding'
rcParams['axes.unicode_minus'] = False
font_manager._rebuild()

code1 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/아파트 전세가격지수 금리합본(완료).csv',index_col=0)
code1
code1.drop(['연%'], axis=1,inplace=True)
code1

code2 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/본원통화변화량.csv',index_col=0)
code2
code2.drop(['증감량','변동율','기준금리(%)'], axis=1,inplace=True)
code2
code2.drop(index=['2011-01','2011-02','2011-03','2011-04','2011-05','2011-06','2011-07','2011-08','2011-09','2011-10','2011-11','2011-12','2021-07','2021-08','2021-09','2021-10','2021-11'],inplace=True)
code2

code3=code1.join(code2)
code3

plt.figure( figsize=(10,5) )
plt.plot( code3['본원통화'])
plt.ylabel('본원통화량')
# plt.xticks( rotation=90 )
ax = plt.gca()
ax.plot(code3['본원통화'], color='red',label='본원통화')
ax1 = ax.twinx()
ax1.set_ylabel('아파트 전세가격지수')
ax1 = plt.gca()
ax1.plot( code3['서울 강북지역 도심권 종로구'])
ax2 = plt.gca()
ax2.plot( code3['서울 강북지역 도심권 중구'])
ax3 = plt.gca()
ax3.plot( code3['서울 강북지역 도심권 용산구'])
ax4 = plt.gca()
ax4.plot( code3['서울 강북지역 동북권 성동구'])
ax5 = plt.gca()
ax5.plot( code3['서울 강북지역 동북권 광진구'])
ax6 = plt.gca()
ax6.plot( code3['서울 강북지역 동북권 동대문구'])
ax7 = plt.gca()
ax7.plot( code3['서울 강북지역 동북권 중랑구'])
ax8 = plt.gca()
ax8.plot( code3['서울 강북지역 동북권 성북구'])
ax9 = plt.gca()
ax9.plot( code3['서울 강북지역 동북권 강북구'])
ax10 = plt.gca()
ax10.plot( code3['서울 강북지역 동북권 도봉구'])
ax11 = plt.gca()
ax11.plot( code3['서울 강북지역 동북권 노원구'])
ax12 = plt.gca()
ax12.plot( code3['서울 강북지역 서북권 은평구'])
ax13 = plt.gca()
ax13.plot( code3['서울 강북지역 서북권 서대문구'])
ax14 = plt.gca()
ax14.plot( code3['서울 강북지역 서북권 마포구'])
ax15 = plt.gca()
ax15.plot( code3['서울 강남지역 서남권 양천구'])
ax16 = plt.gca()
ax16.plot( code3['서울 강남지역 서남권 강서구'])
ax17 = plt.gca()
ax17.plot( code3['서울 강남지역 서남권 구로구'])
ax18 = plt.gca()
ax18.plot( code3['서울 강남지역 서남권 금천구'])
ax19 = plt.gca()
ax19.plot( code3['서울 강남지역 서남권 영등포구'])
ax20 = plt.gca()
ax20.plot( code3['서울 강남지역 서남권 동작구'])
ax21 = plt.gca()
ax21.plot( code3['서울 강남지역 서남권 관악구'])
ax22 = plt.gca()
ax22.plot( code3['서울 강남지역 동남권 서초구'])
ax23 = plt.gca()
ax23.plot( code3['서울 강남지역 동남권 강남구'])
ax24 = plt.gca()
ax24.plot( code3['서울 강남지역 동남권 송파구'])
ax25 = plt.gca()
ax25.plot( code3['서울 강남지역 동남권 강동구'])
ax.legend()
plt.title('아파트 전세가격과 본원통화량 비교')
plt.show()

list1 = code3.index
list1 = pd.to_datetime(list1, format='%Y-%m')
code3.index = list1

code4 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/물가지수와주택가격지수.csv',index_col=0)
code4
code4.drop(['주택대출(서울)','전세가격지수','소비자물가지수','생산자물가지수'], axis=1, inplace=True)
code4

code5 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/한국은행기준금리월별(완료).csv',index_col=0)
code5

code6=code4.join(code5)
code6

plt.figure(figsize=(10,5))
sns.lineplot( data=code6, x='시점', y='매매가격지수', label='아파트 매매가격지수')
# sns.lineplot( data=mulga_corr1, x='시점', y='매매가격지수', label='매매가격지수')
ax = plt.gca()
ax2 = ax.twinx()
sns.lineplot( data=code6, x='시점', y='연%', color='black',label='한국은행 기준금리')
plt.show()

plt.figure( figsize=(20,5) )
plt.plot( code6['매매가격지수'], color='red')
plt.ylabel('아파트 매매가격지수')
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( code6['연%'], color='black')
ax2.set_ylabel('한국은행 기준금리')
plt.title('아파트가격지수와 기준금리')
plt.show()

code6['본원통화'] = code3['본원통화'].str.replace(',', '').astype(np.float64)

list1 = code6.index
list1 = pd.to_datetime(list1, format='%Y-%m')
code6.index = list1

sns.regplot(data=code6, x='매매가격지수', y='연%',line_kws={'color':'red'})

code6[['매매가격지수', '연%']].corr()
pd.DataFrame( code6 ).to_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/매매가격지수 금리합본(완료).csv')

sns.jointplot(x='매매가격지수',y='연%',kind='reg',data=code6)
plt.show()

sns.lmplot(x="매매가격지수", y="연%", height=8, data=code6)
plt.show()
code6

code7 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/본원통화변화량.csv',index_col=0)
code7
code7.drop(['증감량','변동율','기준금리(%)'], axis=1, inplace=True)
code7

code8=code6.join(code7)
code8
code8.drop(['연%'], axis=1, inplace=True)
code8

plt.figure( figsize=(20,5) )
plt.plot( code8['본원통화'], color='red')
plt.ylabel('본원통화')
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( code8['매매가격지수'], color='black')
ax2.set_ylabel('매매가격지수')
plt.title('매매가격지수와 본원통화')
plt.show()

code8['본원통화'] = code8['본원통화'].str.replace(',', '').astype(np.float64)

list1 = code8.index
list1 = pd.to_datetime(list1, format='%Y-%m')
code8.index = list1

pd.options.display.float_format = '{:.6f}'.format

code8
