import warnings 
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def conv(x):
  x.fillna('0', inplace=True)
  if x.name == '행정구역': return x
  return x.str.replace(',', '').astype(np.int)

def preProcessing( df ):
  tmp = df.iloc[:, 0::3]
  tmp['행정구역'] = tmp['행정구역'].str.split(' ').str[0]
  names = []
  for name in tmp.columns:
    if name == '행정구역':
      names.append(name)
      continue
    names.append(pd.to_datetime(name.split('_')[0], format='%Y년%m월'))
  tmp.columns = names
  tmp = tmp.apply( conv )
  tmp = tmp.set_index('행정구역')

  return tmp.T

tmp1 = pd.read_csv('/content/drive/MyDrive/data /200801_201012_주민등록인구기타현황(출생등록)_birth.csv', encoding='cp949')
tmp1 = preProcessing(tmp1)

tmp2 = pd.read_csv('/content/drive/MyDrive/data /201101_201312_주민등록인구기타현황(출생등록)_birth.csv', encoding='cp949')
tmp2 = preProcessing(tmp2)

tmp3 = pd.read_csv('/content/drive/MyDrive/data /201401_201612_주민등록인구기타현황(출생등록)_birth.csv', encoding='cp949')
tmp3 = preProcessing(tmp3)

tmp4 = pd.read_csv('/content/drive/MyDrive/data /201701_201912_주민등록인구기타현황(출생등록)_birth.csv', encoding='cp949')
tmp4 = preProcessing(tmp4)

tmp5 = pd.read_csv('/content/drive/MyDrive/data /202001_202111_주민등록인구기타현황(출생등록)_birth.csv', encoding='cp949')
tmp5 = preProcessing(tmp5)

rawData = pd.concat( [tmp1, tmp2] )
rawData = pd.concat( [rawData, tmp3] )
rawData = pd.concat( [rawData, tmp4] )
rawData = pd.concat( [rawData, tmp5] )
rawData

rawData.to_csv('/content/drive/MyDrive/data /total_population.csv')

rawData['서울특별시'].sum()
rawData['서울특별시'].cumsum()
rawData['서울특별시'].cumsum().diff()
rawData.sum()

total_population = rawData.sum().to_frame(name='전체 인구수')
total_population.drop(index='전국', inplace=True)
total_population

total_population.loc['서울특별시', '위도'] = 37.56667
total_population.loc['부산광역시', '위도'] = 35.17944
total_population.loc['대구광역시', '위도'] = 35.87222
total_population.loc['인천광역시', '위도'] = 37.45639
total_population.loc['광주광역시', '위도'] = 35.15972
total_population.loc['대전광역시', '위도'] = 36.35111
total_population.loc['울산광역시', '위도'] = 35.53889
total_population.loc['경기도', '위도'] = 37.26389
total_population.loc['강원도', '위도'] = 37.757687
total_population.loc['충청북도', '위도'] = 36.995972
total_population.loc['충청남도', '위도'] = 36.476515
total_population.loc['전라북도', '위도'] = 35.95133
total_population.loc['전라남도', '위도'] = 34.946739
total_population.loc['경상북도', '위도'] = 35.837855
total_population.loc['경상남도', '위도'] = 35.498692
total_population.loc['제주특별자치도', '위도'] = 35.958 
total_population.loc['세종특별자치시', '위도'] = 36.48750

total_population.loc['서울특별시', '경도'] = 126.97806
total_population.loc['부산광역시', '경도'] = 129.07556
total_population.loc['대구광역시', '경도'] = 128.60250
total_population.loc['인천광역시', '경도'] = 126.70528
total_population.loc['광주광역시', '경도'] = 126.85306
total_population.loc['대전광역시', '경도'] = 127.38500
total_population.loc['울산광역시', '경도'] = 129.31667
total_population.loc['경기도', '경도'] = 127.179108
total_population.loc['강원도', '경도'] = 128.873749
total_population.loc['충청북도', '경도'] = 127.926178
total_population.loc['충청남도', '경도'] = 127.082977
total_population.loc['전라북도', '경도'] = 126.951141
total_population.loc['전라남도', '경도'] = 127.698212
total_population.loc['경상북도', '경도'] = 129.173126
total_population.loc['경상남도', '경도'] = 128.747406
total_population.loc['제주특별자치도', '경도'] = 126.712189
total_population.loc['세종특별자치시', '경도'] = 127.28167

import json
geojson = json.load( open('/content/drive/MyDrive/data /HangJeongDong_ver20210701.geojson') )

for feature in geojson['features']:
  print( feature['properties']['sidonm'] )

import folium

map = folium.Map(location=[37,127], zoom_start=7)
map

for i in total_population.index:
  folium.Marker([total_population.loc[i,'위도'], total_population.loc[i,'경도']]).add_to(map)

!pip install geopandas
import geopandas as gp

geojson = json.load( open('/content/drive/MyDrive/data /sido.json') 

map = folium.Map( location = [37, 127], zoom_start=7 ,tiles="cartodbpositron")

folium.Choropleth(
  geo_data = geojson,
  data = total_population,
  columns = [total_population.index, '전체 인구수'],
  fill_color='YlOrRd',
  # fill_opacity = 0.7,
  # line_opacity=0.5,
  key_on = 'properties.CTP_KOR_NM'
).add_to(map)

!pip install -U plotly
import plotly.express as px

fig = px.choropleth(
  total_population,
  geojson = geojson, 
  locations=total_population.index,
  color = '전체 인구수',
  color_continuous_scale='Blues',
  featureidkey = 'properties.CTP_KOR_NM'
)

fig.update_geos(fitbounds='locations', visible=False)
fig.update_layout()

