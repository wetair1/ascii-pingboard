#!/usr/bin/env python3
import curses, subprocess, sys, time

HOSTS = ['1.1.1.1', '8.8.8.8', 'github.com', 'notion.so']


def ping(host):
    try:
        p = subprocess.run(['ping', '-c', '1', '-W', '1', host], capture_output=True, text=True)
        if p.returncode != 0: return None
        out = p.stdout
        if 'time=' in out:
            return float(out.split('time=')[1].split()[0])
    except Exception:
        return None
    return None


def bar(ms, width=28):
    if ms is None: return 'x' * width
    fill = min(width, int(ms / 10))
    return '#' * fill + '-' * (width-fill)


def draw(stdscr):
    curses.curs_set(0)
    hosts = sys.argv[1:] or HOSTS
    hist = {h: [] for h in hosts}
    stdscr.nodelay(True)
    while True:
        for host in hosts:
            hist[host].append(ping(host))
            hist[host] = hist[host][-20:]
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(0, 2, 'ASCII PINGBOARD - q to quit')
        for i, host in enumerate(hosts[:h-3], 2):
            last = hist[host][-1]
            status = 'DOWN' if last is None else f'{last:.1f} ms'
            spark = ''.join('.' if v is None else ('#' if v < 80 else '*' if v < 200 else '!') for v in hist[host])
            stdscr.addstr(i, 2, f'{host:<22} {status:<10} [{bar(last, max(8, w-60))}] {spark}')
        for _ in range(10):
            if stdscr.getch() in (ord('q'), ord('Q')): return
            time.sleep(0.1)


if __name__ == '__main__':
    curses.wrapper(draw)
