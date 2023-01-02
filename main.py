from getgithubrepourls import *

a = FromUser("gvanrossum")
print("\n".join(a.urls))
print(len(a.urls))
