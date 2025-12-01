# advent-of-code-2025

## Setup

```
sudo apt-get install xclip -y
alias pbpaste='xclip -selection clipboard -o'
```

Then you can paste puzzle inputs from clipboard to `stdin`, e.g.:

```
pbpaste | uv run day01_1.py
```

or easily test manual inputs by piping.
