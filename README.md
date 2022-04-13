# PyRedactKit 🔐📝

<p align="center">
  <img src="./asciiRedact.png" alt="Python Redactor Kit!"/>
<br />
<i>CLI tool to redact sensitive information like ip address, email and dns.</i>
</p>

## Features

Redacts the following from your text files. 📄 ✍️

- dns 🌐
- emails ✉️
- ipv4 📟
- ipv6 📟

## Pre-requisites

- [Python3](https://www.python.org/downloads/) installed
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed

## How to use

Clone the repo

```
git clone https://github.com/brootware/PyRedactKit.git && cd PyRedactKit
```

Run as below to redact a single file

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

Help Menu as below

```
usage: pyredactkit.py [-h] [-t REDACTIONTYPE] [-o OUTDIR] [-r] [-e EXTENSION] path [path ...]

Read in a file or set of files, and return the result.

positional arguments:
  path                  Path of a file or a directory of files

optional arguments:
  -h, --help            show this help message and exit
  -t REDACTIONTYPE, --redactiontype REDACTIONTYPE
                        Type of data to redact. dns, emails, ipv4, ipv6 (default: None)
  -o OUTDIR, --outdir OUTDIR
                        Output directory of the file (default: None)
  -r, --recursive       Search through subfolders (default: True)
  -e EXTENSION, --extension EXTENSION
                        File extension to filter by. (default: )
```

## TODO

Unredact part is currently in development
