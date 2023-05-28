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

def main():
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


if __name__ == '__main__':
    main()
