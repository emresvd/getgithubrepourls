from getgithubrepourls import (
    FromBaseURL,
    TopicUrls,
    FromExplore,
    CollectionUrls
)

fromBaseURL = FromBaseURL("https://github.com/topics/python")
print(
    "fromBaseURL",
    fromBaseURL.urls,
    len(fromBaseURL.urls)
)

topic_urls = TopicUrls()
print(
    "topic_urls",
    topic_urls.urls,
    len(topic_urls.urls)
)

fromExplore = FromExplore()
print(
    "fromExplore",
    fromExplore.urls,
    len(fromExplore.urls)
)

collectionUrls = CollectionUrls()
print(
    "collectionUrls",
    collectionUrls.urls,
    len(collectionUrls.urls)
)
