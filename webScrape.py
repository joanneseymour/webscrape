

from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode()

title_index = html.find("<title>")
start_index = title_index + len("<title>")
print(start_index)
end_index = html.find("</title>")
print(end_index)
title = html[start_index:end_index]
print(title)

# review

# import module from library
from urllib.request import urlopen
# name the url
url = "...com"
# open the page
page = urlopen(url)
# read the page and call it html_bytes
html_bytes = page.read()
# decode the page and call it html
html = html_bytes.decode()
#find the index of the title and call it title_index
title_index = html.find("<title>")
# find the start index of the title and call it start_index
start_index = title_index + len("<title>")
# find the end index of the title and call it end_index
end_index = html.find("</title")



