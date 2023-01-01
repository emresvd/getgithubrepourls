```python
from getgithubrepourls import FromBaseURL

fromBaseURL = FromBaseURL("https://github.com/topics/python")

print(fromBaseURL.urls)
print(len(fromBaseURL.urls))
```