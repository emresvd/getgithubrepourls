```python
from getgithubrepourls import FromBaseURL

fromBaseURL = FromBaseURL("https://github.com/topics/python")

print(fromBaseURL.urls)
print(len(fromBaseURL.urls))
```
```bash
['https://github.com/donnemartin/system-design-primer', 'https://github.com/tensorflow/tensorflow', 'https://github.com/CyC2018/CS-Notes', 'https://github.com/vinta/awesome-python', 'https://github.com/TheAlgorithms/Python', 'https://github.com/justjavac/free-programming-books-zh_CN', 'https://github.com/practical-tutorials/project-based-learning', 'https://github.com/huggingface/transformers', 'https://github.com/nvbn/thefuck', 'https://github.com/django/django', 'https://github.com/521xueweihan/HelloGitHub', 'https://github.com/pallets/flask', 'https://github.com/pytorch/pytorch', 'https://github.com/home-assistant/core', 'https://github.com/keras-team/keras', 'https://github.com/ansible/ansible', 'https://github.com/tiangolo/fastapi', 'https://github.com/scikit-learn/scikit-learn', 'https://github.com/azl397985856/leetcode', 'https://github.com/apache/superset']   
20
```