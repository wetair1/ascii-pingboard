# Contributing

Thanks for improving ascii-pingboard.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-pingboard.git
cd ascii-pingboard
python3 main.py
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Keep host checks bounded with timeouts.
- Keep the dashboard readable on small terminals.
- Avoid hiding network errors silently.
- Document new controls and arguments.

## Checks

```bash
python3 -m py_compile main.py
python3 main.py 1.1.1.1
```

## Commit style

Use short imperative messages, for example:

- `Add host history`
- `Improve latency display`
- `Document controls`
