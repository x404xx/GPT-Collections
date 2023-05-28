from json import loads

from httpx import stream as _stream


class Completion:
    @classmethod
    def create(
        cls,
        url: str = '',
        prompt: str = '',
        parent_message_id: str = '',
        system_message: str = 'You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using markdown.',
        temperature: float = 0.8,
        top_p: float = 1,
        ):

        with _stream(
            'POST',
            url=f'{url}/api/chat-process',
            json={
                'prompt': prompt,
                'options': {'parentMessageId': parent_message_id},
                'systemMessage': system_message,
                'temperature': temperature,
                'top_p': top_p
            },
            timeout=30
        ) as response:
            yield from cls.handle_response(response)

    @staticmethod
    def handle_response(response):
        for line in response.iter_lines():
            if line:
                parsed_line = loads(line)
                choices = parsed_line.get('detail', {}).get('choices', [])
                for choice in choices:
                    content = choice.get('delta', {}).get('content')
                    if content:
                        yield parsed_line['parentMessageId'], content


