from getgithubrepourls import (
    FromCollections,
    FromTopics
)

fromCollections = FromCollections()
print(
    "fromCollections",
    fromCollections.urls,
    len(fromCollections.urls)
)

fromTopics = FromTopics()
print(
    "fromTopics",
    fromTopics.urls,
    len(fromTopics.urls)
)
