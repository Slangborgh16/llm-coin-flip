import time
import argparse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def flip_a_coin(model: str='gpt-3.5-turbo', temperature: float=1.5, prompt: str='Flip a coin') -> str:
    api_response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages = [
            # System message keeps GPT from rambling about how it can't physically flip a coin
            {'role' : 'system', 'content' : 'Reply with 1 word: heads or tails'},
            {'role' : 'user', 'content' : prompt}
        ]
    )

    completion_response: str = api_response.choices[0].message.content.strip('.')
    response_length: int = len(completion_response)

    # If the response is longer than 5, the LLM gave bad output (len("heads") == 5)
    if response_length > 5:
        return None

    completion_response = completion_response[:response_length].lower()
    
    # Sometimes GPT likes to say "head" and "tail" instead of "heads" and "tails"
    if 'head' in completion_response:
        return 'heads'
    elif 'tail' in completion_response:
        return 'tails'
    else:
        return None


if __name__ == '__main__':
    description: str = 'A slightly overkill way to flip a coin using GPT'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('trials', default=1, type=int, nargs='?', \
            help='Number of trials to run. Default: 1')
    parser.add_argument('-m', '--model', default='gpt-3.5-turbo', type=str, \
            help='GPT model to use. Default: gpt-3.5-turbo')
    parser.add_argument('-t', '--temperature', default=1.5, type=float, \
            help='LLM temperature. Default: 1.5')
    args = parser.parse_args()

    trials: int = args.trials
    model: str = args.model
    temperature = args.temperature
    show_plot: bool = args.plot

    if trials > 1:
        for trial in range(1, trials + 1):
            print(f'Trial {trial}: ', end='')
            result: str = None

            # If the LLM produces bad output, continue to flip until we get either heads or tails
            while result is None:
                result = flip_a_coin(model, temperature)

            print(result)

            if trial != trials:
                time.sleep(1)
    else:
        result: str = None

        # If the LLM produces bad output, continue to flip until we get either heads or tails
        while result is None:
            result = flip_a_coin(model, temperature)

        print(result)
