
# First example with clean html:

from urllib.request import urlopen
import re
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# print(start_index)
# end_index = html.find("</title>")
# print(end_index)
# title = html[start_index:end_index]
# print(title)

# # review

# # import module from library
# from urllib.request import urlopen
# # name the url
# url = "...com"
# # open the page
# page = urlopen(url)
# # read the page and call it html_bytes
# html_bytes = page.read()
# # decode the page as utf8 and call it html
# html = html_bytes.decode("utf-8")
# #find the index of the title and call it title_index
# print(html)
# title_index = html.find("<title>")
# # find the start index of the title and call it start_index
# start_index = title_index + len("<title>")
# # find the end index of the title and call it end_index
# end_index = html.find("</title")
# # make a new variable called title
# title = html[start_index:end_index]

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title) # returns everything from start of html up to </title> because <title> doesn't exist

# * means 0 or more of letter before astrix 
pattern = "ab*c"
strings = ["ac","abc","ab", "abbbbbbbbbc", "abcccccc", "abcd", "ABC"]
for string in strings:
    print(re.findall(pattern, string,re.IGNORECASE))

