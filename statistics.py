import tiktoken
from coinflip import flip_a_coin

def estimate_token_usage(trials: int, prompt: str, model: str) -> int:
    encoding = tiktoken.encoding_for_model(model)

    system_tokens: int = len(encoding.encode('Reply with 1 word: heads or tails'))
    prompt_tokens: int = len(encoding.encode(prompt))
    response_tokens: int = len(encoding.encode('Heads'))    # Should be similar nummber of tokens in "Tails"

    total_tokens: int = trials * (system_tokens + prompt_tokens + response_tokens)
    return total_tokens

num_tokens: int = estimate_token_usage(10, 'Flip a coin', 'gpt-3.5-turbo')
print('Minimum number of tokens:', num_tokens)
