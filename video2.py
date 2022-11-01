from bs4 import BeautifulSoup
with open('website.html',encoding='utf-8') as file:
    contents=file.read()

soup=BeautifulSoup(contents,'html.parser')




#To get all the para/anchor/li
all_anchor_tags=(soup.find_all(name='a'))

for tag in all_anchor_tags:
    print(tag)

#To just get the href
for tag in all_anchor_tags:
    print(tag.get('href'))

#To get particular heading
heading=soup.find(name='h1',id='name')
print(heading)


#in order to not clash with the class keyword which is a reserved word in python we use another keyword class_
section_heading=soup.find(name='h3',class_='heading')
print(section_heading.string)

#Select will give us all the matching items and select one will give us one matching item
company_url=soup.select_one(selector='p a')
print(company_url)

#To select of ID we use '#' sign
name=soup.select_one(selector='#name')
print(name)

#To select class_ we use '.' sign
headd=soup.select('.heading')
print(headd)
#
# select finds multiple instances and returns a list, find finds the first, so they don't do the same thing. select_one would be the equivalent to find.
# I almost always use css selectors when chaining tags or using tag.classname, if looking for a single element without a class I use find. Essentially it comes down to the use case and personal preference.
# As far as flexibility goes I think you know the answer, soup.select("div[id=foo] > div > div > div[class=fee] > span > span > a") would look pretty ugly using multiple chained find/find_all calls.
# The only issue with the css selectors in bs4 is the very limited support, nth-of-type is the only pseudo class implemented and chaining attributes like a[href][src] is also not supported as are many other parts of css selectors. But things like a[href=..]* , a[href^=], a[href$=] etc.. are I think much nicer than find("a", href=re.compile(....)) but again that is personal preference.