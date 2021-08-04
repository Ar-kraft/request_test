import requests
from req import YaUploader
from req import token


token_v = "WRITE YOUR TOKEN HERE"
#service token to get access
version = 5.77
#actual version of API
owner_id = 552934290
album_id = 'profile'
photo_sizes  = 1
extended = 1
#identificator of donor user
#method of vk api - photos.get
response = requests.get('https://api.vk.com/method/photos.get/',
                        params={
                        'access_token': token_v,
                        'v': version,
                        'owner_id':owner_id,
                        'album_id':album_id,
                        'photo_sizes':photo_sizes,
                        'extended':extended
                        }
                        )
#new method open
data = response.json()['response']['items'][0]['sizes'][-1]['url']
dict_save = {}
data_raw= response.json()['response']
iii = range(0, data_raw['count'])
print('qqqqqqqqqqqqqqqqqqqqqqq')
for i in iii:
    url = response.json()['response']['items'][i]['sizes'][-1]['url']
    name_of_file = str(response.json()['response']['items'][i]['likes']['count']) + '.jpeg'
    rq = requests.get(url)
    with open(name_of_file, "wb") as code:
       code.write(rq.content)

    uploader = YaUploader(name_of_file, token)
    result = uploader.upload()
    print(name_of_file + ' ' + str(result) + '\n')



#
# #new method closed
#
# quan_of_img = data_raw['count'] #received quantity from json file
#
# #splitting of API request like string expression
# data_var = "data"
# data_str = " = response.json()['response']['items']"
# data_str_2 ="['sizes'][-1]['url']"
# data_str_3 = "['likes']['count']"
# #cycles for lists
# rangelist1=[]
# rangelist2=[]
# rangelist3=[]
#
# range = range(0, quan_of_img )
#
# counter = range
# for r in counter:
#     rangelist1.append(data_var+str(r))
#     rangelist1.append(data_var+str(r))
#
# numbers = range
# for n in numbers:
#     rangelist2.append(data_str+"["+str(n)+"]"+data_str_2)
# print(rangelist1)
#
# likes = range
# for u in likes:
#     rangelist3.append(data_str + "[" + str(u) + "]" + data_str_3)
#
#
# #merging two lists
# for i, j in zip(rangelist1, rangelist2):
#     exec(i+j)
#     print(i+j)
#
# list_val=[]
#
# # for v in rangelist1:
#     # exec('list_val.append('+(str(v))+')')
# # print(list_val)
#
#
# print("_________________________________________")
# #merging third list
# for i, j in zip(rangelist1, rangelist3):
#     exec(i+j)
#
# list_lik=[]
#
# for v in rangelist1:
#     exec('list_lik.append('+(str(v))+')')
# print(list_lik)
#
#
# print("_________________________________________")
#
#
#
#
#
# namej='.jpg'
# for j in list_lik:
#     jo = str(j) + namej
# list_lik.append(jo)
# print(list_lik)
#
# rq = requests.get(data)
# with open(nof, "wb") as code:
#     code.write(rq.content)

# data000 = response.json()['response']['items'][0]['likes']['count']

# print(data000)