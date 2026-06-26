# ascii-pingboard

ASCII curses ping dashboard for checking host availability.

## Features

- Pings multiple hosts
- Shows up/down status
- Shows latest latency
- Keeps a small ASCII history line
- Pure Python stdlib

## Usage

```bash
python3 main.py
python3 main.py 1.1.1.1 8.8.8.8 github.com
```

Press `q` to quit.

## Notes

Uses the system `ping` command.
