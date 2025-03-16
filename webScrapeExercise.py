# Write a program that grabs the full HTML from the following URL: "http://olympus.realpython.org/profiles/dionysus"

import re
from urllib.request import urlopen
page = urlopen("http://olympus.realpython.org/profiles/dionysus")
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
string_to_find = "Name"
string_start_index = html.find(string_to_find)
string_end_index = string_start_index + len(string_to_find)
print(f"{string_to_find} starts at {string_start_index} and ends at {string_end_index}")
print(html[string_start_index:string_end_index])