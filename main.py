from getgithubrepourls import *

a = FromBaseURL("https://github.com/gvanrossum?tab=repositories")
print("\n".join(a.urls))
print(len(a.urls))
