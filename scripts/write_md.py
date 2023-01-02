import os

with open("main.py", "r", encoding="utf-8") as f:
    main_py = f.read().strip()

# output = os.popen("python main.py").read().strip()

# data = """
# ```python
# {}
# ```
# ```python
# {}
# ```
# """.format(main_py, output).strip()

data = """
```python
{}
```
""".format(main_py).strip()

with open("README.md", "w", encoding="utf-8") as f:
    f.write(data)
