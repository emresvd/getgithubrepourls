from getgithubrepourls import (
    FromBaseURL,
    TopicUrls
)

topic_urls = TopicUrls()

for url in topic_urls.urls:
    fromBaseURL = FromBaseURL(url)
    print(
        url.split("/")[-1],
        fromBaseURL.urls,
        len(fromBaseURL.urls)
    )
