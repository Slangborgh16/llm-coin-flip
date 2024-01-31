import sys
import time
import random
import argparse
import tiktoken
import matplotlib.pyplot as plt

from coinflip import flip_a_coin


def estimate_token_usage(trials: int, prompt: str, model: str) -> tuple[int, int]:
    encoding = tiktoken.encoding_for_model(model)

    system_tokens: int = len(encoding.encode('Reply with 1 word: heads or tails'))
    prompt_tokens: int = len(encoding.encode(prompt))
    response_tokens: int = len(encoding.encode('Heads'))    # Should be similar number of tokens in "Tails"

    input_tokens: int = trials * (system_tokens + prompt_tokens)
    output_tokens: int = trials * response_tokens
    return input_tokens, output_tokens


# Placeholder function so I can run tests without calling the API
# *args lets the function be a drop-in replacement for flip_a_coin()
def test_flip(*args) -> str:
    return random.choice(('heads', 'tails'))


if __name__ == '__main__':
    description: str = 'Estimate the probability of getting heads for a given prompt, temperature, and model'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('trials', type=int, help='Number of trials to run.')
    parser.add_argument('-m', '--model', default='gpt-3.5-turbo', type=str, \
            help='GPT model to use. Default: gpt-3.5-turbo')
    parser.add_argument('-t', '--temperature', default=1.5, type=float, \
            help='LLM temperature. Default: 1.5')
    args = parser.parse_args()

    trials: int = args.trials
    model: str = args.model
    temperature = args.temperature

    token_estimate: tuple[int, int] = estimate_token_usage(trials, 'Flip a coin', model)
    print('Estimated minimum token usage')
    print('-' * 30)
    print('Input tokens:', token_estimate[0])
    print('Output tokens:', token_estimate[1])
    print(f'\nCheck https://openai.com/pricing to estimate the price for {model}')
    
    run_trials: str = input(f'Are you sure you want to run {trials} trials with {model}? [y/N] ').lower()
    if run_trials not in ('y', 'yes'):
       print('Quitting')
       sys.exit(0)

    print('Running trials')
