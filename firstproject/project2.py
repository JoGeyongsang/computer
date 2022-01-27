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

code1 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/단독주택 전세가격지수(완료).csv',index_col=0)
code1

code2 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/한국은행기준금리월별(완료).csv',index_col=0)
code2
code2.drop(index=['2011-01','2011-02','2011-03','2011-04','2011-05','2011-06','2011-07','2011-08','2011-09','2011-10','2011-11','2011-12','2021-07','2021-08','2021-09','2021-10','2021-11','2021-12'],inplace=True)
code2

code3=code1.join(code2)
code3
pd.DataFrame( code3 ).to_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/단독주택 전세가격지수 금리합본(완료).csv')

plt.figure( figsize=(20,5) )
plt.plot( code3['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot( code3['서울 강북지역 도심권'], color='orange')
ax2.set_ylabel('단독주택 전세가격지수')
ax3 = plt.gca()
ax3.plot( code3['서울 강북지역 동북권'], color='blue')
ax4 = plt.gca()
ax4.plot( code3['서울 강북지역 서북권'], color='green')
ax5 = plt.gca()
ax5.plot( code3['서울 강남지역 서남권'], color='gray')
ax6 = plt.gca()
ax6.plot( code3['서울 강남지역 동남권'], color='purple')
plt.title('단독주택 전세가격지수와 한국은행 기준금리 비교')
plt.show()

sns.regplot(data=code3, x='서울 강북지역 도심권', y='연%',line_kws={'color':'red'})

code3[['서울 강북지역 도심권','연%']].corr()

sns.regplot(data=code3, x='서울 강북지역 동북권', y='연%',line_kws={'color':'red'})

code3[['서울 강북지역 동북권','연%']].corr()

sns.regplot(data=code3, x='서울 강북지역 서북권', y='연%',line_kws={'color':'red'})

code3[['서울 강북지역 서북권','연%']].corr()

sns.regplot(data=code3, x='서울 강남지역 서남권', y='연%',line_kws={'color':'red'})

code3[['서울 강남지역 서남권','연%']].corr()

sns.regplot(data=code3, x='서울 강남지역 동남권', y='연%',line_kws={'color':'red'})

code3[['서울 강남지역 동남권','연%']].corr()

code4 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/연립주택 전세가격지수(완료).csv',index_col=0)
code4
code4.drop(index=['2011-01','2011-02','2011-03','2011-04','2011-05','2011-06','2011-07','2011-08','2011-09','2011-10','2011-11','2011-12'],inplace=True)

code5=code4.join(code2)

code5.drop(['서울 강북지역','서울 강남지역','경기 경부1권','경기 경부2권','경기 서해안권','경기 동부1권','경기 동부2권','경기 경의권','경기 경원권'],axis=1,inplace=True)
code5
pd.DataFrame( code5 ).to_csv('/content/drive/MyDrive/data /프로젝트1/연립주택 전세가격지수 금리합본(완료).csv')

code11=sns.regplot(data=code5, x='서울 강북지역 도심권', y='연%',line_kws={'color':'red'})

code5[['서울 강북지역 도심권','연%']].corr()

sns.regplot(data=code5, x='서울 강북지역 동북권', y='연%',line_kws={'color':'red'})

code5[['서울 강북지역 동북권','연%']].corr()

sns.regplot(data=code5, x='서울 강북지역 서북권', y='연%',line_kws={'color':'red'})

code5[['서울 강북지역 서북권','연%']].corr()

sns.regplot(data=code5, x='서울 강남지역 서남권', y='연%',line_kws={'color':'red'})

code5[['서울 강남지역 서남권','연%']].corr()

sns.regplot(data=code3, x='서울 강남지역 동남권', y='연%',line_kws={'color':'red'})

code5[['서울 강남지역 동남권','연%']].corr()

code6 = pd.read_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/아파트 전세가격지수(완료).csv',index_col=0)
code6

code6.drop(index=['2011-01','2011-02','2011-03','2011-04','2011-05','2011-06','2011-07','2011-08','2011-09','2011-10','2011-11','2011-12','2021-07'],inplace=True)
code6.drop(['경기 경부2권 과천시','경기 경부3권 안양시','경기 경부4권 안양시 만안구','경기 경부5권 안양시 동안구','경기 경부6권 성남시','경기 경부7권 성남시 수정구','경기 경부8권 성남시 중원구','경기 경부9권 성남시 분당구','경기 경부10권 군포시','경기 경부11권 의왕시','경기 경부3권 안성시','경기 경부4권 용인시','경기 경부5권 용인시 처인구','경기 경부6권 용인시 기흥구','경기 경부7권 용인시 수지구','경기 경부8권 수원시','경기 경부9권 수원시 장안구','경기 경부10권 수원시 권선구','경기 경부11권 수원시 팔달구','경기 경부12권 수원시 영통구','경기 서해안권 부천시','경기 서해안권 안산시','경기 서해안권 안산시 상록구','경기 서해안권 안산시 단원구','경기 서해안권 시흥시','경기 서해안권 광명시','경기 서해안권 화성시','경기 서해안권 오산시','경기 서해안권 평택시','경기 동부2권 남양주시','경기 동부3권 구리시','경기 동부4권 하남시','경기 동부5권 광주시','경기 동부3권 이천시','경기 동부4권 여주시','경기 경의권 김포시','경기 경의권 고양시','경기 경의권 고양시 덕양구','경기 경의권 고양시 일산동구','경기 경의권 고양시 일산서구','경기 경의권 파주시','경기 경원권 포천시','경기 경원권 양주시','경기 경원권 의정부시'],axis=1,inplace=True)
code6.drop(['경기 경원권 동두천시'],axis=1,inplace=True)
code6

code7=code6.join(code2)
code7

code7.drop(['서울 강북지역','서울 강북지역 동북권','서울 강북지역 서북권','서울 강남지역 서북권','서울 강남지역 서남권','서울 강남지역 동남권'], axis=1, inplace=True)
code7
code7.drop(['경기 경부1권','경기 경부2권','경기 서해안권','경기 동부1권','경기 동부2권','경기 경의권','경기 경원권'], axis=1, inplace=True)
code7
code7.drop(['서울 강북지역 도심권'], axis=1, inplace=True)
code7
pd.DataFrame( code7 ).to_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/아파트 전세가격지수 금리합본(완료).csv')

plt.figure( figsize=(20,5) )
plt.plot( code7['연%'], color='red')
plt.ylabel('한국은행 기준금리')
plt.xticks( rotation=90 )
ax = plt.gca()
ax1 = ax.twinx()
ax1.set_ylabel('아파트 전세가격지수')
ax1 = plt.gca()
ax1.plot( code7['서울 강북지역 도심권 종로구'])
ax2 = plt.gca()
ax2.plot( code7['서울 강북지역 도심권 중구'])
ax3 = plt.gca()
ax3.plot( code7['서울 강북지역 도심권 용산구'])
ax4 = plt.gca()
ax4.plot( code7['서울 강북지역 동북권 성동구'])
ax5 = plt.gca()
ax5.plot( code7['서울 강북지역 동북권 광진구'])
ax6 = plt.gca()
ax6.plot( code7['서울 강북지역 동북권 동대문구'])
ax7 = plt.gca()
ax7.plot( code7['서울 강북지역 동북권 중랑구'])
ax8 = plt.gca()
ax8.plot( code7['서울 강북지역 동북권 성북구'])
ax9 = plt.gca()
ax9.plot( code7['서울 강북지역 동북권 강북구'])
ax10 = plt.gca()
ax10.plot( code7['서울 강북지역 동북권 도봉구'])
ax11 = plt.gca()
ax11.plot( code7['서울 강북지역 동북권 노원구'])
ax12 = plt.gca()
ax12.plot( code7['서울 강북지역 서북권 은평구'])
ax13 = plt.gca()
ax13.plot( code7['서울 강북지역 서북권 서대문구'])
ax14 = plt.gca()
ax14.plot( code7['서울 강북지역 서북권 마포구'])
ax15 = plt.gca()
ax15.plot( code7['서울 강남지역 서남권 양천구'])
ax16 = plt.gca()
ax16.plot( code7['서울 강남지역 서남권 강서구'])
ax17 = plt.gca()
ax17.plot( code7['서울 강남지역 서남권 구로구'])
ax18 = plt.gca()
ax18.plot( code7['서울 강남지역 서남권 금천구'])
ax19 = plt.gca()
ax19.plot( code7['서울 강남지역 서남권 영등포구'])
ax20 = plt.gca()
ax20.plot( code7['서울 강남지역 서남권 동작구'])
ax21 = plt.gca()
ax21.plot( code7['서울 강남지역 서남권 관악구'])
ax22 = plt.gca()
ax22.plot( code7['서울 강남지역 동남권 서초구'])
ax23 = plt.gca()
ax23.plot( code7['서울 강남지역 동남권 강남구'])
ax24 = plt.gca()
ax24.plot( code7['서울 강남지역 동남권 송파구'])
ax25 = plt.gca()
ax25.plot( code7['서울 강남지역 동남권 강동구'])
plt.title('아파트 전세가격과 한국은행 기준금리 비교')
plt.show()

sns.regplot(data=code7, x='서울 강북지역 도심권 종로구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 도심권 종로구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 도심권 중구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 도심권 중구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 도심권 용산구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 도심권 용산구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 성동구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 성동구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 광진구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 광진구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 동대문구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 동대문구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 중랑구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 중랑구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 성북구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 성북구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 강북구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 강북구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 도봉구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 도봉구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 동북권 노원구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 동북권 노원구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 서북권 은평구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 서북권 은평구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 서북권 서대문구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 서북권 서대문구','연%']].corr()

sns.regplot(data=code7, x='서울 강북지역 서북권 마포구', y='연%',line_kws={'color':'red'})

code7[['서울 강북지역 서북권 마포구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 양천구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 양천구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 강서구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 강서구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 구로구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 구로구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 금천구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 금천구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 영등포구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 영등포구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 동작구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 동작구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 서남권 관악구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 서남권 관악구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 동남권 서초구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 동남권 서초구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 동남권 강남구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 동남권 강남구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 동남권 송파구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 동남권 송파구','연%']].corr()

sns.regplot(data=code7, x='서울 강남지역 동남권 강동구', y='연%',line_kws={'color':'red'})

code7[['서울 강남지역 동남권 강동구','연%']].corr()

pd.DataFrame( code7 ).to_csv('/content/drive/MyDrive/data /프로젝트1/진짜완료버전/아파트 전세가격지수 금리합본(완료).csv')



