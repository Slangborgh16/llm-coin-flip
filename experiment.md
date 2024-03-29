# Experiment

> To run your own experiment, please see [this section](#running-your-own-experiment).

In this experiment, I ran a series of coin flip trials using `gpt-3.5-turbo`.
The goal was to compare how different prompts and temperatures affect the results of the LLM.
All coin flips were independent of each other.
In other words, GPT doesn't get to see the results of previous coin flips.
I ran 1000 trials for each combination of prompt and temperature.

The prompts I used were:
- `Flip a coin`
- `Flip a random coin`
- `Flip a weighted coin`

GPT likes to complain about being unable to physically flip a coin.
I found that using the system prompt `Reply with 1 word: heads or tails` usually fixes this issue.
This is the default system prompt of `coinflip.py`.

However, GPT sometimes outputs random nonsense anyway,
especially at higher temperatures (see image below).
When this happens, the coin gets flipped again so that we still get the desired number of trials.
The percentage of failed trials is reported as the "failure rate" once the program finishes.

<p align="center">
    <img src="extras/nonsense_output.png" alt="Broken GPT output example" width="50%">
</p>

# Results

![Bar graphs of the heads vs. tails probability for each prompt/temperature](extras/matrix.png)

|Prompt|Temperature|Heads|Tails|Failure Rate|
|---|:---:|:---:|:---:|:---:|
|Flip a coin|1.0|692|308|0.40%|
|Flip a random coin|1.0|733|267|0.60%|
|Flip a weighted coin|1.0|923|77|4.12%|
|Flip a coin|1.5|636|364|5.39%|
|Flip a random coin|1.5|662|338|5.93%|
|Flip a weighted coin|1.5|752|248|20.19%|

In all trials, the coin was weighted in favor of heads.
For both temperatures tested, the prompt `Flip a coin` produced the least biased results,
followed by `Flip a random coin` and finally `Flip a weighted coin`.
A higher temperature seems to improve the randomness of the LLM output,
but it also increases the failure rate. 
Notably, the prompt `Flip a weighted coin` with a temperature of 1.5 had a failure rate of 20.19%.
This means that an additional 253 trials had to be run to make up for the unusable data.

# Discussion

I find it interesting that asking GPT to flip a random coin makes the output even more biased.
I'm not sure why this happens.
When it comes to the increased failure rates at high temperatures,
maybe an improved system prompt would reduce the failure rate at the expense of using more tokens.

An expansion of this experiment would be to let GPT see its previous output.
Would it try to balance the number of heads and tails it produces?
With a large number of trials, including all previous output in a single API request would
likely exceed the context window of the model.
Perhaps a better idea would be to send only the N most recent outputs.
The value of N could be a new parameter to play around with, too.

---

# Running Your Own Experiment

The installation and setup process is the same as for `coinflip.py`, and only needs to be done once.
It can be found [here](README.md#setup).

By default, the program tries to estimate the **minimum** number of tokens that will be used.
This warning can be disabled with the `-i` or `--ignore` flag.
Please note that these estimates are often way off due to repeat trials from failures,
unexpected GPT output, etc.

## Positional Arguments
|**Argument**|**Description**|**Required**|
|---|---|---|
|Trials|Number of coin flips to run|Yes|

## Options
|**Option**|**Description**|**Required**|
|---|---|---|
|-m MODEL, --model MODEL|[GPT model](https://platform.openai.com/docs/models/gpt-3-5) to use (Default: gpt-3.5-turbo)|No|
|-t TEMP, --temperature TEMP|LLM temperature to use (Default: 1.5)|No|
|-p PROMPT, --prompt PROMPT|Prompt to use (Default: `Flip a coin`)|No|
|-i, --ignore|Ignore warning about token usage|No|
|-h, --help|Display the help message|No|

## Usage Examples
Run 100 trials using `gpt-4` with the prompt `Flip a weighted coin`.
```bash
python3 experiment.py -m gpt-4 -p "Flip a weighted coin" 100
```

Run 1000 trials using the default model, temperature, and prompt.
```bash
python3 experiment.py 1000
```

## Example Output
```
Model: gpt-3.5-turbo    Temperature: 1.5
Prompt: "Flip a coin"   Trials: 1000
----------------------------------------
Trial: 1000     Heads: 636      Tails: 364
Total trials (including fails): 1057    Failure rate: 5.39%
```
