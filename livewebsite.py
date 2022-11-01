from bs4 import BeautifulSoup

import requests

response = requests.get('https://news.ycombinator.com/')
contents = response.text
# response.text returns the content of the response
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.find_all('a'))
# Self Solution
# list_of_titles=(soup.select(selector='.titlelink'))
# for title in list_of_titles:
#     print(title.text)

# Angela Solution using find
# and to get list change it to find all aur phir for loop laga k individual print kara sakte

titles = soup.find_all(name='a', class_='titlelink')
title_list=[]
for title in titles:
    title_list.append(title)



hreflist=[]
for title in titles:
    hreflist.append( (title.get('href')))

upvote = soup.find_all(name='span', class_='score')
a = []
for up in upvote:
    a.append(int(up.get_text().split()[0]))

max = a[0]

for i in a:
    # print(i)
    if i > max:
        max = i

print(max)
index = (a.index(max))
print(hreflist[index])
print(title_list[index])
# actual_link = article_link.get('href')
# upvote=soup.find_all(name='span',class_='score')


# print(actual_link)

# print(upvote)
