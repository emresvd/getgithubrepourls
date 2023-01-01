```python
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
```
```python
['https://github.com/donnemartin/system-design-primer', 'https://github.com/tensorflow/tensorflow', 'https://github.com/CyC2018/CS-Notes', 'https://github.com/vinta/awesome-python', 'https://github.com/TheAlgorithms/Python', 'https://github.com/justjavac/free-programming-books-zh_CN', 'https://github.com/practical-tutorials/project-based-learning', 'https://github.com/huggingface/transformers', 'https://github.com/nvbn/thefuck', 'https://github.com/django/django', 'https://github.com/521xueweihan/HelloGitHub', 'https://github.com/pallets/flask', 'https://github.com/pytorch/pytorch', 'https://github.com/home-assistant/core', 'https://github.com/keras-team/keras', 'https://github.com/ansible/ansible', 'https://github.com/tiangolo/fastapi', 'https://github.com/scikit-learn/scikit-learn', 'https://github.com/azl397985856/leetcode', 'https://github.com/apache/superset']
20
['https://github.com/topics/phaser', 'https://github.com/topics/c', 'https://github.com/topics/raspberry-pi', 'https://github.com/topics/3d', 'https://github.com/topics/ajax', 'https://github.com/topics/algorithm', 'https://github.com/topics/amphp', 'https://github.com/topics/android', 'https://github.com/topics/angular', 'https://github.com/topics/ansible', 'https://github.com/topics/api', 'https://github.com/topics/arduino', 'https://github.com/topics/aspnet', 'https://github.com/topics/atom', 'https://github.com/topics/awesome', 'https://github.com/topics/aws', 'https://github.com/topics/azure', 'https://github.com/topics/babel', 'https://github.com/topics/bash', 'https://github.com/topics/bitcoin', 'https://github.com/topics/bootstrap', 'https://github.com/topics/bot', 'https://github.com/topics/chrome', 'https://github.com/topics/chrome-extension', 'https://github.com/topics/cli', 'https://github.com/topics/clojure', 'https://github.com/topics/code-quality', 'https://github.com/topics/code-review', 'https://github.com/topics/compiler', 'https://github.com/topics/continuous-integration', 'https://github.com/topics/covid-19', 'https://github.com/topics/cpp', 'https://github.com/topics/react', 'https://github.com/topics/nodejs', 'https://github.com/topics/javascript', 'https://github.com/topics/css', 'https://github.com/topics/config', 'https://github.com/topics/python', 'https://github.com/topics/html', 'https://github.com/topics/fsharp', 'https://github.com/topics/reactjs', 'https://github.com/topics/github-config']
42
```