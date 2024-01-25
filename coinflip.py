import time
import argparse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def flip_a_coin(model: str='gpt-3.5-turbo', temperature: float=1.5) -> str:
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages = [
            {'role' : 'system', 'content' : 'Reply with 1 word: heads or tails'},
            {'role' : 'user', 'content' : 'Flip a coin'}
        ]
    )

    return response.choices[0].message.content


def main(trials: int, model: str, temperature: float) -> None:
    for trial in range(1, trials + 1):
        print(f'Trial {trial}')
        result: str = flip_a_coin(model, temperature)
        print(f'\t{result}')
        time.sleep(5)


if __name__ == '__main__':
    trials: int = 10
    model: str = 'gpt-3.5-turbo'
    temperature: float = 1.5
    main(trials, model, temperature)
