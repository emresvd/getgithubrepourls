from getgithubrepourls import (
    FromBaseURL,
    TopicUrls
)

fromBaseURL = FromBaseURL("https://github.com/topics/python")

print(fromBaseURL.urls)
print(len(fromBaseURL.urls))

topic_urls = TopicUrls()
print(topic_urls.urls)
print(len(topic_urls.urls))
