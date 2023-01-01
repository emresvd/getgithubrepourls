from getgithubrepourls import (
    FromBaseURL,
    TopicUrls,
    FromExplore
)

fromBaseURL = FromBaseURL("https://github.com/topics/python")
print(fromBaseURL.urls)
print(len(fromBaseURL.urls))

topic_urls = TopicUrls()
print(topic_urls.urls)
print(len(topic_urls.urls))

fromExplore = FromExplore()
print(fromExplore.urls)
print(len(fromExplore.urls))
