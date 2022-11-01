from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

list_of_movies = list(soup.find_all(name='h3', class_='title'))
ol = []
for movie in list_of_movies:
    ol.insert(0, (movie.get_text()))
print(ol)


with open('top100movies.txt','w',encoding='utf-8') as fp:
    for item in ol:
        fp.write("%s\n"%item)
print("Done")

# for movie in reversed:
#     print(movie)

# for movie in ol:
#     print(movie.get_text())
