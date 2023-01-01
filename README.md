```python
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
```
```python
['https://github.com/donnemartin/system-design-primer', 'https://github.com/tensorflow/tensorflow', 'https://github.com/CyC2018/CS-Notes', 'https://github.com/vinta/awesome-python', 'https://github.com/TheAlgorithms/Python', 'https://github.com/justjavac/free-programming-books-zh_CN', 'https://github.com/practical-tutorials/project-based-learning', 'https://github.com/huggingface/transformers', 'https://github.com/nvbn/thefuck', 'https://github.com/django/django', 'https://github.com/521xueweihan/HelloGitHub', 'https://github.com/pallets/flask', 'https://github.com/pytorch/pytorch', 'https://github.com/home-assistant/core', 'https://github.com/keras-team/keras', 'https://github.com/ansible/ansible', 'https://github.com/tiangolo/fastapi', 'https://github.com/scikit-learn/scikit-learn', 'https://github.com/azl397985856/leetcode', 'https://github.com/apache/superset']
20
['https://github.com/topics/react', 'https://github.com/topics/redux', 'https://github.com/topics/ethereum', 'https://github.com/topics/3d', 'https://github.com/topics/ajax', 'https://github.com/topics/algorithm', 'https://github.com/topics/amphp', 'https://github.com/topics/android', 'https://github.com/topics/angular', 'https://github.com/topics/ansible', 'https://github.com/topics/api', 'https://github.com/topics/arduino', 'https://github.com/topics/aspnet', 'https://github.com/topics/atom', 'https://github.com/topics/awesome', 'https://github.com/topics/aws', 'https://github.com/topics/azure', 'https://github.com/topics/babel', 'https://github.com/topics/bash', 'https://github.com/topics/bitcoin', 'https://github.com/topics/bootstrap', 'https://github.com/topics/bot', 'https://github.com/topics/c', 'https://github.com/topics/chrome', 'https://github.com/topics/chrome-extension', 'https://github.com/topics/cli', 'https://github.com/topics/clojure', 'https://github.com/topics/code-quality', 'https://github.com/topics/code-review', 'https://github.com/topics/compiler', 'https://github.com/topics/continuous-integration', 'https://github.com/topics/covid-19', 'https://github.com/topics/cpp', 'https://github.com/topics/nodejs', 'https://github.com/topics/javascript', 'https://github.com/topics/css', 'https://github.com/topics/config', 'https://github.com/topics/python', 'https://github.com/topics/java', 'https://github.com/topics/html', 'https://github.com/topics/reactjs', 'https://github.com/topics/github-config']
42
['https://github.com/LAION-AI/Open-Assistant', 'https://github.com/karpathy/nanoGPT', 'https://github.com/sczhou/CodeFormer', 'https://github.com/DarkFlippers/unleashed-firmware', 'https://github.com/ytdl-org/youtube-dl', 'https://github.com/google/osv-scanner', 'https://github.com/collections/game-engines', 'https://github.com/pola-rs/polars', 'https://github.com/neonbjb/tortoise-tts', 'https://github.com/Developer-Y/cs-video-courses', 'https://github.com/dair-ai/Prompt-Engineering-Guide', 'https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes', 'https://github.com/ocornut/imgui', 'https://github.com/AmruthPillai/Reactive-Resume', 'https://github.com/PRQL/prql', 'https://github.com/A-poc/RedTeam-Tools', 'https://github.com/jerryjliu/gpt_index', 'https://github.com/imDazui/Tvlist-awesome-m3u-m3u8', 'https://github.com/aurae-runtime/aurae', 'https://github.com/zlib-searcher/zlib-searcher', 'https://github.com/BrunoLevy/learn-fpga', 'https://github.com/alist-org/alist', 'https://github.com/freeCodeCamp/freeCodeCamp', 'https://github.com/Atlas-OS/Atlas', 'https://github.com/SheerSt/pokewilds', 'https://github.com/jwasham/coding-interview-university', 'https://github.com/trending/developers', 'https://github.com/charliermarsh/ruff', 'https://github.com/parrt/dtreeviz', 'https://github.com/earlephilhower/arduino-pico', 'https://github.com/wong2/chat-gpt-google-extension']
31
```