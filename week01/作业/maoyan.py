
import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装
from time import sleep
import pandas as pd
import random

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

USER_AGENT = random.choice(USER_AGENT_LIST)
header = {'user-agent': USER_AGENT}  # 模型行为


myurl = 'https://maoyan.com/films?showType=3&sortId=3'  # 爬取的网页

response = requests.get(myurl, headers=header)

# print(response.text)
print(f'返回码是: {response.status_code}')

bs_info = bs(response.text, 'html.parser')  # requests抓取网页内容赋值


# data_list = [['电影名', '类型', '上映时间']]
# times = 0
# for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
#     movie_name = tags.find('span', class_='name').text
#     # print(movie_name)
#     movie_type = tags.find_all(
#         'div',
#         attrs={
#             'class': 'movie-hover-title'},
#         limit=2)[1].text .replace(
#             ' ',
#             '').replace(
#                 '\n',
#                 '').replace(
#                     '类型:',
#         '')
#     # print(movie_type)
#     movie_date = tags.find_next(
#         'div', attrs={
#             'class': 'movie-hover-title movie-hover-brief'}).text .replace(
#         ' ', '').replace(
#                 '\n', '').replace(
#                     '上映时间:', '')
#     # print(movie_date)
#
#     print('%s %s %s' % (movie_name, movie_type, movie_date))
#     data_list.append([movie_name, movie_type, movie_date])
#     times  += 1
#     if times >= 10:
#         break
#     sleep(random.randrange(1, 3))
# data = pd.DataFrame(data=data_list)
# data.to_csv('./movie2.csv', encoding='utf8', header=False)
# #data[0:10].to_csv('./movie1.csv', encoding='utf8', index=False, header=False)


movie_list = []
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[0:10]:
    sub_tag = tag.find_all('div', attrs={'class': 'movie-hover-title'})
    movie_name = sub_tag[0].find('span', attrs={'class': 'name'}).text
    movie_type = sub_tag[1].text.replace("\n", "").split(":")[1].strip()
    release_time = sub_tag[3].text.replace("\n", "").split(":")[1].strip()

    movie_list.append({
        "name": movie_name,
        "type": movie_type,
        "time": release_time,
    })

movie = pd.DataFrame(data=movie_list)
movie.to_csv('./movie00.csv', encoding='utf8', header=False)
