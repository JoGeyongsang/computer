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

data = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/분기별구의성별인구,금리(완료).csv',index_col=0)
data

data1=data[(data['지역']=='종로구')]
data1
data1.drop(['지역'], axis=1,inplace=True)
data1
pd.DataFrame( data1 ).to_csv('/content/drive/MyDrive/data /프로젝트1/종로구의성별인구,금리(완료).csv')

data2=data[(data['지역']=='중구')]
data2
data2.drop(['지역'], axis=1,inplace=True)
data2
pd.DataFrame( data2 ).to_csv('/content/drive/MyDrive/data /프로젝트1/중구의성별인구,금리(완료).csv')

data3=data[(data['지역']=='용산구')]
data3
data3.drop(['지역'], axis=1,inplace=True)
data3
pd.DataFrame( data3 ).to_csv('/content/drive/MyDrive/data /프로젝트1/용산구의성별인구,금리(완료).csv')

data4=data[(data['지역']=='성동구')]
data4
data4.drop(['지역'], axis=1,inplace=True)
data4
pd.DataFrame( data4 ).to_csv('/content/drive/MyDrive/data /프로젝트1/성동구의성별인구,금리(완료).csv')

data5=data[(data['지역']=='광진구')]
data5
data5.drop(['지역'], axis=1,inplace=True)
data5
pd.DataFrame( data5 ).to_csv('/content/drive/MyDrive/data /프로젝트1/광진구의성별인구,금리(완료).csv')

data6=data[(data['지역']=='동대문구')]
data6
data6.drop(['지역'], axis=1,inplace=True)
data6
pd.DataFrame( data6 ).to_csv('/content/drive/MyDrive/data /프로젝트1/동대문구의성별인구,금리(완료).csv')

data7=data[(data['지역']=='중랑구')]
data7
data7.drop(['지역'], axis=1,inplace=True)
data7
pd.DataFrame( data7 ).to_csv('/content/drive/MyDrive/data /프로젝트1/중랑구의성별인구,금리(완료).csv')

data8=data[(data['지역']=='성북구')]
data8
data8.drop(['지역'], axis=1,inplace=True)
data8
pd.DataFrame( data8 ).to_csv('/content/drive/MyDrive/data /프로젝트1/성북구의성별인구,금리(완료).csv')

data9=data[(data['지역']=='강북구')]
data9
data9.drop(['지역'], axis=1,inplace=True)
data9
pd.DataFrame( data9 ).to_csv('/content/drive/MyDrive/data /프로젝트1/강북구의성별인구,금리(완료).csv')

data10=data[(data['지역']=='도봉구')]
data10
data10.drop(['지역'], axis=1,inplace=True)
data10
pd.DataFrame( data10 ).to_csv('/content/drive/MyDrive/data /프로젝트1/도봉구의성별인구,금리(완료).csv')

data11=data[(data['지역']=='노원구')]
data11
data11.drop(['지역'], axis=1,inplace=True)
data11
pd.DataFrame( data11 ).to_csv('/content/drive/MyDrive/data /프로젝트1/노원구의성별인구,금리(완료).csv')

data12=data[(data['지역']=='은평구')]
data12
data12.drop(['지역'], axis=1,inplace=True)
data12
pd.DataFrame( data12 ).to_csv('/content/drive/MyDrive/data /프로젝트1/은평구의성별인구,금리(완료).csv')

data13=data[(data['지역']=='서대문구')]
data13
data13.drop(['지역'], axis=1,inplace=True)
data13
pd.DataFrame( data13 ).to_csv('/content/drive/MyDrive/data /프로젝트1/서대문구의성별인구,금리(완료).csv')

data14=data[(data['지역']=='마포구')]
data14
data14.drop(['지역'], axis=1,inplace=True)
data14
pd.DataFrame( data14 ).to_csv('/content/drive/MyDrive/data /프로젝트1/마포구의성별인구,금리(완료).csv')

data15=data[(data['지역']=='양천구')]
data15
data15.drop(['지역'], axis=1,inplace=True)
data15
pd.DataFrame( data15 ).to_csv('/content/drive/MyDrive/data /프로젝트1/양천구의성별인구,금리(완료).csv')

data16=data[(data['지역']=='강서구')]
data16
data16.drop(['지역'], axis=1,inplace=True)
data16
pd.DataFrame( data16 ).to_csv('/content/drive/MyDrive/data /프로젝트1/강서구의성별인구,금리(완료).csv')

data17=data[(data['지역']=='구로구')]
data17
data17.drop(['지역'], axis=1,inplace=True)
data17
pd.DataFrame( data17 ).to_csv('/content/drive/MyDrive/data /프로젝트1/구로구의성별인구,금리(완료).csv')

data18=data[(data['지역']=='금천구')]
data18
data18.drop(['지역'], axis=1,inplace=True)
data18
pd.DataFrame( data18 ).to_csv('/content/drive/MyDrive/data /프로젝트1/금천구의성별인구,금리(완료).csv')

data19=data[(data['지역']=='영등포구')]
data19
data19.drop(['지역'], axis=1,inplace=True)
data19
pd.DataFrame( data19 ).to_csv('/content/drive/MyDrive/data /프로젝트1/영등포구의성별인구,금리(완료).csv')

data20=data[(data['지역']=='동작구')]
data20
data20.drop(['지역'], axis=1,inplace=True)
data20
pd.DataFrame( data20 ).to_csv('/content/drive/MyDrive/data /프로젝트1/동작구의성별인구,금리(완료).csv')

data21=data[(data['지역']=='관악구')]
data21
data21.drop(['지역'], axis=1,inplace=True)
data21
pd.DataFrame( data21 ).to_csv('/content/drive/MyDrive/data /프로젝트1/관악구의성별인구,금리(완료).csv')

data22=data[(data['지역']=='서초구')]
data22
data22.drop(['지역'], axis=1,inplace=True)
data22
pd.DataFrame( data22 ).to_csv('/content/drive/MyDrive/data /프로젝트1/서초구의성별인구,금리(완료).csv')

data23=data[(data['지역']=='강남구')]
data23
data23.drop(['지역'], axis=1,inplace=True)
data23
pd.DataFrame( data23 ).to_csv('/content/drive/MyDrive/data /프로젝트1/강남구의성별인구,금리(완료).csv')

data24=data[(data['지역']=='송파구')]
data24
data24.drop(['지역'], axis=1,inplace=True)
data24
pd.DataFrame( data24 ).to_csv('/content/drive/MyDrive/data /프로젝트1/송파구의성별인구,금리(완료).csv')

data25=data[(data['지역']=='강동구')]
data25
data25.drop(['지역'], axis=1,inplace=True)
data25
pd.DataFrame( data25 ).to_csv('/content/drive/MyDrive/data /프로젝트1/강동구의성별인구,금리(완료).csv')

data1 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/종로구의성별인구,금리(완료).csv',index_col=0)
data1

plt.figure( figsize=(20,5) )
plt.plot( data1['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data1['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data1['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data1['합계'], color='green', label='합계' )
plt.title('종로구')
plt.legend()
plt.show()

sns.regplot(data=data1, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data2['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data2['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data2['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data2['합계'], color='green', label='합계' )
plt.title('중구')
plt.legend()
plt.show()

sns.regplot(data=data2, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data3['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data3['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data3['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data3['합계'], color='green', label='합계' )
plt.title('용산구')
plt.legend()
plt.show()

sns.regplot(data=data3, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data4['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data4['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data4['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data4['합계'], color='green', label='합계' )
plt.title('성동구')
plt.legend()
plt.show()

sns.regplot(data=data4, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data5['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data5['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data5['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data5['합계'], color='green', label='합계' )
plt.title('광진구')
plt.legend()
plt.show()

sns.regplot(data=data5, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data6['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data6['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data6['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data6['합계'], color='green', label='합계' )
plt.title('동대문구')
plt.legend()
plt.show()

sns.regplot(data=data6, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data7['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data7['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data7['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data7['합계'], color='green', label='합계' )
plt.title('중랑구')
plt.legend()
plt.show()

sns.regplot(data=data7, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data8['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data8['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data8['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data8['합계'], color='green', label='합계' )
plt.title('성북구')
plt.legend()
plt.show()

sns.regplot(data=data8, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data9['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data9['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data9['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data9['합계'], color='green', label='합계' )
plt.title('강북구')
plt.legend()
plt.show()

sns.regplot(data=data9, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data10['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data10['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data10['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data10['합계'], color='green', label='합계' )
plt.title('도봉구')
plt.legend()
plt.show()

sns.regplot(data=data10, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data11['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data11['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data11['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data11['합계'], color='green', label='합계' )
plt.title('노원구')
plt.legend()
plt.show()

sns.regplot(data=data11, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data12['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data12['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data12['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data12['합계'], color='green', label='합계' )
plt.title('은평구')
plt.legend()
plt.show()

sns.regplot(data=data12, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data13['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data13['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data13['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data13['합계'], color='green', label='합계' )
plt.title('서대문구')
plt.legend()
plt.show()

sns.regplot(data=data13, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data14['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data14['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data14['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data14['합계'], color='green', label='합계' )
plt.title('마포구')
plt.legend()
plt.show()

sns.regplot(data=data14, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data15['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data15['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data15['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data15['합계'], color='green', label='합계' )
plt.title('양천구')
plt.legend()
plt.show()

sns.regplot(data=data15, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data16['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data16['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data16['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data16['합계'], color='green', label='합계' )
plt.title('강서구')
plt.legend()
plt.show()

sns.regplot(data=data16, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data17['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data17['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data17['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data17['합계'], color='green', label='합계' )
plt.title('구로구')
plt.legend()
plt.show()

sns.regplot(data=data17, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data18['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data18['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data18['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data18['합계'], color='green', label='합계' )
plt.title('금천구')
plt.legend()
plt.show()

sns.regplot(data=data18, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data19['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data19['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data19['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data19['합계'], color='green', label='합계' )
plt.title('영등포구')
plt.legend()
plt.show()

sns.regplot(data=data19, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data20['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data20['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data20['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data20['합계'], color='green', label='합계' )
plt.title('동작구')
plt.legend()
plt.show()

sns.regplot(data=data20, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data21['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data21['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data21['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data21['합계'], color='green', label='합계' )
plt.title('관악구')
plt.legend()
plt.show()

sns.regplot(data=data21, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data22['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data22['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data22['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data22['합계'], color='green', label='합계' )
plt.title('서초구')
plt.legend()
plt.show()

sns.regplot(data=data22, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data23['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data23['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data23['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data23['합계'], color='green', label='합계' )
plt.title('강남구')
plt.legend()
plt.show()

sns.regplot(data=data23, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data24['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data24['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data24['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data24['합계'], color='green', label='합계' )
plt.title('송파구')
plt.legend()
plt.show()

sns.regplot(data=data24, x='합계', y='연%',line_kws={'color':'red'})

plt.figure( figsize=(20,5) )
plt.plot( data25['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( data25['남자'], color='red', label='남자')
ax2.set_ylabel('인구 수')
ax3 = plt.gca()
ax3.plot( data25['여자'], color='blue', label='여자' )
ax4 = plt.gca()
ax4.plot( data25['합계'], color='green', label='합계' )
plt.title('강동구')
plt.legend()
plt.show()

sns.regplot(data=data25, x='합계', y='연%',line_kws={'color':'red'})

kain = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/가계부채,임대보증금.csv',index_col=0)
kain

kain1 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/년도별금리.csv',index_col=0)
kain1

kain2=kain.join(kain1)
kain2

plt.figure( figsize=(10,5))
plt.title('금융부채, 임대보증금, 기준금리')
plt.plot(kain2['금융부채'],label='금융부채')
plt.plot(kain2['임대보증금'],label='전세보증금')
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( kain2['연%'], color='black',label='연%' )
ax2.set_ylabel('한국은행 기준금리')
plt.legend()
ax.legend()
plt.show()

sns.regplot(data=kain2, x='금융부채', y='연%',line_kws={'color':'red'})

sns.regplot(data=kain2, x='임대보증금', y='연%',line_kws={'color':'red'})

kain2[['금융부채','임대보증금','연%']].corr()

code4 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/물가지수와주택가격지수.csv',index_col=0)
code4

code4.drop(['주택대출(서울)','전세가격지수','소비자물가지수','생산자물가지수'], axis=1, inplace=True)
code4

code5 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/한국은행기준금리월별(완료).csv',index_col=0)
code5

code6=code4.join(code5)
code6


















