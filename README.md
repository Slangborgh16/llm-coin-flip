# llm-coin-flip

# About
Instead of using a boring old quarter for a coin flip, why not use a multi-million dollar large language model like OpenAI's GPT?

# Setup
```bash
git clone https://github.com/Slangborgh16/llm-coin-flip.git
cd llm-coin-flip
```

## Requirements
This project uses **Python 3.11** and requires the following libraries:
- [openai](https://github.com/openai/openai-python)
- [dotenv](https://github.com/theskumar/python-dotenv)
- [matplotlib](https://github.com/matplotlib/matplotlib)

Run the following command to install the dependencies.
```bash
pip install -r requirements.txt
```

## OpenAI API Key
You will need to have an OpenAI API key to use this project. Check out the [OpenAI Website](https://platform.openai.com/api-keys) to set one up. Next, follow one of the two methods below.

### Method 1: Project `.env` File
Create a file in the project directory called `.env`.
```bash
touch .env
```
Using Vim (or your favorite text editor, I guess), add the following line to `.env`. Replace the placeholder text with your API secret key.
```bash
OPENAI_API_KEY=YOUR_SECRET_KEY_GOES_HERE
```

### Method 2: Set an Environment Variable
In your `.bashrc` file or the equivalent for your system, add the following line. Replace the placeholder text with your API secret key.
```bash
export OPENAI_API_KEY="YOUR_SECRET_KEY_GOES_HERE"
```
Then run `source ~/.bashrc`.

# Positional Arguments
|**Argument**|**Description**|**Required**|
|---|---|---|
|Trials|Number of coin flips to run (Default: 1)|No|

# Options
|**Option**|**Description**|**Required**|
|---|---|---|
|-m, --model|[GPT model](https://platform.openai.com/docs/models/gpt-3-5) to use (Default: gpt-3.5-turbo)|No|
|-t, --temperature|LLM temperature to use (Default: 1.5)|No|
|-h, --help|Display the help message|No|

# Usage Examples
```bash
python3 coinflip.py
```
