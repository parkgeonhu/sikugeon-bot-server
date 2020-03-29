import requests
import json
import os
##input_place=input('입력하실 태그? ')


#키워드 장소 검색 (ex. 정통집 건대)
def get_store_info(query):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query='+query
    headers = {'Authorization':'KakaoAK '+os.environ['kakaotoken']}
    response = requests.get(url, headers = headers)
    info = json.loads(response.text)
    return info

#지역 검색 (ex. 하계동) 
def get_location_info(query):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+query
    headers = {'Authorization':'KakaoAK '+os.environ['kakaotoken']}
    response = requests.get(url, headers = headers)
    result = json.loads(response.text)
    return result

def get_location_x(info):
    return info["documents"][0]['x']

def get_location_y(info):
    return info["documents"][0]['y']


    