from bs4 import BeautifulSoup

with open('website.html', encoding='utf-8') as file:
    contents = file.read()
    #without encoding it was throwing an error
    #I do no know the original file format, but adding to open , encoding='utf-8' is usually a good thing (and it is the default in Linux and MacOs).
    # sometimes we can use lxm parser instead of htmlparses ... if html parser doesn't work

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)

#To get name of the title
print(soup.title.name)

#To get string contained in the title tag
print(soup.title.string)


#To print entire soup object
print(soup)

#To get the entire soup object with indentation
print(soup.prettify())

#To get the first anchor tag/li/anchor tag in the website
print(soup.li)
print(soup.a)
print(soup.p)

