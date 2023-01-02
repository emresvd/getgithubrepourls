from getgithubrepourls import *

urls = AllUrlsWithMore()

print(urls.urls)
print(len(urls.urls))

with open("urls.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(urls.urls))
