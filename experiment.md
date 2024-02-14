# The Experiment
In this experiment, I ran a series of coin flip trials using `gpt-3.5-turbo`.
The goal was to compare how different prompts and temperatures affect the results of the LLM.
All coin flips were independent of each other.
In other words, GPT doesn't get to see the results of previous coin flips.
I ran 1000 trials for each combination of prompt and temperature.

The prompts were:
- `Flip a coin`
- `Flip a random coin`
- `Flip a weighted coin`

In order to keep GPT from complaining about being unable to physically flip a coin,
I found that using the system prompt `Reply with 1 word: heads or tails` usually fixes this.
This is the default system prompt of `coinflip.py`.

However, GPT sometimes outputs random nonsense anyway, especially at higher temperatures (see image below).
When this happens, the coin gets flipped again so that we get the desired number of trials.
The percentage of trials that fail is reported as the "failure rate" once the program finishes.

<img src="extras/nonsense_output.png" alt="Broken GPT output example" width="50%">

 # Results

 ![Bar graphs showing the heads vs. tails probability for each prompt/temperature](extras/matrix.png)
