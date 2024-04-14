# [RTFM](../README.md) - Calculator
A series of rather easy CTFs


## Calculator 1 - VERY EASY

An easy calculator with Python. It's hosted on our private server, but this shouldn't be a problem.\
Of course, it's [open source](./calculator1/files/challenge.py).

## Calculator 2 - VERY EASY

We discovered, that our first version had some issues with the security and exploitability. This version should have fixed this.\
[Source code](./calculator2/files/challenge.py)

## Calculator 3 - EASY

Due to further security risks, we expanded the blacklist. Now our calculator should be completely safe.\
[Source code](./calculator3/files/challenge.py)

## Usage & Dependencies

The scripts are executed within seperate Docker containers. Therefore, the following ports are exposed:

|  Challenge   | Port |
|:------------:|:----:|
| Calculator 1 | 6001 |
| Calculator 2 | 6002 |
| Calculator 3 | 6003 |


## Credits
These challenges were inspired by [HTB Cyber Apocalypse 2024](https://ctf.hackthebox.com/event/details/cyber-apocalypse-2024-hacker-royale-1386)