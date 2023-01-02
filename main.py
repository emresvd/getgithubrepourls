from getgithubrepourls import *

urls = AllUrls()
print("\n".join(urls.urls))
print(len(urls.urls))

print("-"*100)

user = UserUrls()
print(user.urls, len(user.urls))
user.more_users(urls.urls)
print(user.urls, len(user.urls))
