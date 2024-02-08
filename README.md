# llm-coin-flip

# About
This project came about due to this question I had one day:
*How random can an LLM be when asked to flip a coin?*
Would the LLM produce weighted results, or would there be a fairly equal probability of getting heads or tails? I then started to wonder how different prompts would affect the results.

The program `coinflip.py` provides a command line interface to flip a coin once or multiple times in a row using OpenAI's GPT. All coin flips are independent of each other. In other words, GPT doesn't see the previous coin flip results.

In `statistics.py`, I provide a tool to measure the results of a large series of coin flips. This program also shows the "failure rate", or the percentage of times GPT produced a non heads or tails output. Different combinations of prompts, temperatures, and models can easily be run. To learn about  my findings, [click here](). 

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
- [tiktoken](https://github.com/openai/tiktoken)

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
