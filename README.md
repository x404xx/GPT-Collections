<div align="center">

  # GPT4FREE <img src="https://github.com/x404xx/GPT-Collections/assets/114883816/2d913459-7def-4744-8aea-201c6912f217" width="35px">

  A command-line tool for interacting with ChatGPT chatbot.

<img src="https://github.com/x404xx/GPT-Collections/assets/114883816/6769d182-7128-4690-bb25-e097dbd9c615" width="auto" height="auto">

## **"This is not an official API"**

> **Note**
> It's reversed. Created for [gpt4free](https://github.com/xtekky/gpt4free), the website originated from user suggestions.

</div>

## **Available Websites**

```
http://lifan.asia
http://liwp.asia
http://huangzp.asia
http://wupc.asia
http://lijy.asia
http://caifl.asia
http://huangkz.asia
http://huirui.work
http://aiassist.art
http://aiassist.love
```

## **Requirements**

```
pip install httpx
```

## **Usage**

You can find an example of how to use this API in the example.py file or you can do like the following code

```python
from os import name, system
from random import choice

from api import Completion


urls = [
    "http://lifan.asia",
    "http://liwp.asia",
    "http://huangzp.asia",
    "http://wupc.asia",
    "http://lijy.asia",
    "http://caifl.asia",
    "http://huangkz.asia",
    "http://huirui.work",
    "http://aiassist.art",
    "http://aiassist.love"
]

clear_console = lambda: system('cls' if name == 'nt' else 'clear')
clear_console()

parent_message_id = ''
random_url = choice(urls)
print(random_url)

while True:
    prompt = input('\n\033[38;5;121mYou\033[0m : ').lower()
    print()
    if prompt == '!exit':
        break
    elif prompt == '!clear':
        clear_console()
    elif prompt == '!new':
        clear_console()
        parent_message_id = ''
    else:
        completion = Completion.create(random_url, prompt=prompt, parent_message_id=parent_message_id)
        for message_id, chunk in completion:
            print(f'\033[38;5;20m{chunk}\033[0m', end='', flush=True)
            parent_message_id = message_id
        print()

```

## **Legal Disclaimer**

> **Note**
> This was made for educational purposes only, nobody which directly involved in this project is responsible for any damages caused. **_You are responsible for your actions._**
