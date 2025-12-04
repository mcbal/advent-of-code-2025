# advent-of-code-2025

On Mac OS, paste puzzle inputs from clipboard to `stdin` using `pbpaste`:

```
pbpaste | uv run day01_1.py
```

On Linux, an alternative tool can be used:

```
sudo apt-get install -y xclip
alias pbpaste='xclip -selection clipboard -o'
```

Or pipe inputs directly, for example:

```
echo -e 'L49\nL1' | uv run day01_1.py
```
