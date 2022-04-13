# PyRedactKit

<p align="center">
  <img src="./asciiRedact.png" alt="Python Redactor Kit!"/>
</p>

CLI tool to redact sensitive information like ip address, email and dns names.

## Features

- [ ] To add features

## Pre-requisites

- [Python3](https://www.python.org/downloads/) installed
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed

## How to use

- [ ] To add instructions

Clone the repo

```
git clone https://github.com/brootware/PyRedactKit.git && cd PyRedactKit
```

Run as below

```
python pyredactkit.py test.txt
```

To redact specific type of data. E.g (ipv4)

```
python pyredactkit.py test.txt -t ipv4
```

To redact multiple files from a directory and place it in a new directory

```
python pyredactkit.py to_test/ -o redacted_dir
```

## TODO

Unredact part is currently in development
