# Architecture

ascii-pingboard is a small curses ping dashboard built with only the Python standard library.

## Runtime flow

1. Hosts are read from command-line arguments or default values.
2. Each host is checked with the system `ping` command.
3. The latest status and latency are stored in a short in-memory history.
4. The curses UI redraws host status, latency and ASCII history.
5. Pressing `q` exits the app.

## Main parts

- `ping()` runs one bounded host check and returns latency data.
- `bar()` renders latency as a compact ASCII indicator.
- `draw()` owns the refresh loop, history storage and keyboard handling.

## Design rules

- Keep dependencies at zero.
- Keep host checks bounded with timeouts.
- Keep the dashboard readable on small terminals.
- Avoid hiding network failures.
- Prefer simple polling over background workers.
