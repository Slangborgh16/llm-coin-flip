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


def confirm_run(trials, prompt, model) -> bool:
    # token_estimate: tuple[int, int] = estimate_token_usage(trials, 'Flip a coin', model)
    token_estimate: tuple[int, int] = estimate_token_usage(trials, prompt, model)
    print('Estimated minimum token usage')
    print('-' * 30)
    print('Input tokens:', token_estimate[0])
    print('Output tokens:', token_estimate[1])
    print(f'\nCheck https://openai.com/pricing to estimate the price for {model}')
    
    run_trials: str = input(f'Are you sure you want to run {trials} trials with {model}? [y/N] ')
    if run_trials.lower() not in ('y', 'yes'):
        return False

    return True


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
    parser.add_argument('-w', '--warn', action='store_true', \
            help='Enable warning about token usage.')
    args = parser.parse_args()

    trials: int = args.trials
    model: str = args.model
    temperature: float = args.temperature
    warn: bool = args.warn

    if warn and not confirm_run(trials, 'Flip a coin', model):
       print('Quitting')
       sys.exit(0)

    total_trials: int = 0
    heads_count: int = 0
    tails_count: int = 0
    fail_count: int = 0

    print()

    for trial in range(1, trials + 1):
        result: str = test_flip()

        while result is None:
            total_trials += 1
            fail_count += 1
            result = test_flip()

        total_trials += 1

        if result == 'heads':
            heads_count += 1
        elif result == 'tails':
            tails_count += 1

        print(f'Trial: {trial}\tHeads: {heads_count}\tTails: {tails_count}', end='')

        if trial != trials:
            print('\r', end='')
            time.sleep(1)

    print(f'\nTotal trials (including fails): {total_trials}\tFailure rate: {float(fail_count / total_trials) * 100.0}%')
