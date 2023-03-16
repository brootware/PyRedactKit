<br>
<h1 align="center">PyRedactKit 🔐📝</h1>

<p align="center">
  <img src="./images/pyredacthead.gif" alt="Python Redactor Kit!" width="300" height="300"/>
<br />
<i>CLI tool to redact and unredact sensitive information like ip addresses, emails and domains.</i>
<br/>
<code>pip install --upgrade pyredactkit && prk</code>
</p>

<p align="center">
   <img alt="PyPI - Downloads" src="https://pepy.tech/badge/pyredactkit/month">
   <!-- <img alt="PyPI - Downloads" src="https://pepy.tech/badge/pyredactkit"> -->
   <a href="https://twitter.com/brootware"><img src="https://img.shields.io/twitter/follow/brootware?style=social" alt="Twitter Follow"></a>
   <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyredactkit"> <img alt="PyPI" src="https://img.shields.io/pypi/v/pyredactkit">
   <a href="https://sonarcloud.io/summary/new_code?id=brootware_PyRedactKit"><img src="https://sonarcloud.io/api/project_badges/measure?project=brootware_PyRedactKit&metric=alert_status" alt="reliability rating"></a>
   <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/brootware/pyredactkit/ci.yml?branch=main">
</p>

## Features

Redacts and Unredacts the following from your text files. 📄 ✍️

- sg nric 🆔
- credit cards 🏧
- domain names 🌐
- emails ✉️
- ipv4 📟
- ipv6 📟
- base64 🅱️

## Pre-requisites

- [Python3](https://www.python.org/downloads/) installed
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed

## How to use

Demo:
![demo](./images/pyredactdemo.gif)

## [Usage Guide](https://github.com/brootware/PyRedactKit/wiki/Usage)

| <p align="center"><a href="https://pypi.org/project/pyredactkit">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/brootware/pyredactkit">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/pyredactkit/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/pyredactkit">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/brootware/PyRedactKit/blob/main/images/python.png?raw=true" /></p>    | <p align="center"><img src="https://github.com/brootware/PyRedactKit/blob/main/images/docker.png?raw=true" /></p> | <p align="center"><img src="https://github.com/brootware/PyRedactKit/blob/main/images/macports.png?raw=true" /></p> | <p align="center"><img src="https://github.com/brootware/PyRedactKit/blob/main/images/homebrew.png?raw=true" /></p> |
| `python3 -m pip install pyredactkit --upgrade prk` | `docker run -it --rm brootware/pyredactkit` | Coming soon | Coming soon |

<hr>

To use via docker

```bash
docker run -v "$(pwd):/workdir" brootware/pyredactkit 'This is my ip: 127.0.0.1. My email is brute@gmail.com. My favorite secret link is github.com'
```

Quick install

```bash
python -m pip install --upgrade pyredactkit
```

**For more elaborate usage, please [refer to the docs](https://github.com/brootware/PyRedactKit/wiki/Usage).**

Redact from terminal

```bash
prk 'this is my ip:127.0.0.1. my email is broot@outlook.com. secret link is github.com'
```

Redact a single file.

```bash
prk test.txt 
```

Un-redact the file with redacted data

```bash
prk redacted_test.txt -u .hashshadow_test.txt.json 
```

Redact using custom regex pattern

```bash
prk file -c custom.json
```

### Use from github source

Clone the repo

```bash
git clone https://github.com/brootware/PyRedactKit.git && cd PyRedactKit
```

Activate a virtual environment and install required dependencies

```bash
python -m venv venv
source ./venv/bin/activate
python -m pip install pyproject.toml
```

<!-- poetry install 
python -c "import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context =_create_unverified_https_context

nltk.download('popular')" -->

Run as below to redact a single file

```bash
$ prk logdata/test.txt                                    

__________         __________           .___              __     ____  __.__  __   
\______   \___.__. \______   \ ____   __| _/____    _____/  |_  |    |/ _|__|/  |_ 
 |     ___<   |  |  |       _// __ \ / __ |\__  \ _/ ___\   __\ |      < |  \   __\
 |    |    \___  |  |    |   \  ___// /_/ | / __ \\  \___|  |   |    |  \|  ||  |  
 |____|    / ____|  |____|_  /\___  >____ |(____  /\___  >__|   |____|__ \__||__|  
           \/              \/     \/     \/     \/     \/               \/                                                                                                                 
                    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
                    |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
                    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            
    https://github.com/brootware
    https://brootware.github.io     
    https://twitter.com/brootware                                                                        
    
[+] Processing starts now. This may take some time depending on the file size. Monitor the redacted file size to monitor progress
[+] No custom regex pattern supplied, will be redacting all the core sensitive data supported
[+] .hashshadow_test.txt.json file generated. Keep this safe if you need to undo the redaction.
[+] Redacted 10068 targets...
[+] Redacted results saved to ./redacted_test.txt
[+] Estimated total words : 30316
[+] Estimated total minutes saved : 405
[+] Estimated total man hours saved : 6
```

Sample Result:

```txt
John, please get that article on b8bd54d3-34ee-4f31-8b2b-0d729929e8aa to me by 5:00PM on Jan 9th 2012. 4:00 would be ideal, actually. If you have any questions, You can reach me at(519)-236-2723 or get in touch with my associate at 7b3c7641-4b09-4e00-8e02-0e68e47b0ded.
All rights reserved. Printed in the United States of America. No part of this book may be used or reproduced in any manner whatsoever without written permission except in the case of brief quotations embodied in critical articles and reviews. For information address HarperCollins Publishers, 10 East 53rd Street, New York, NY 10022. His name is David. I met him and John last week. Gowtham Teja Kanneganti is a good student. I was born on Oct 4, 1995. My Indian mobile number is +91-7761975545. After coming to USA I got a new number +1-405-413-5255. I live on 1003 E Brooks St, Norman, Ok, 73071. I met  a child, who is playing with josh.
this is my IP: 49f62b69-98c1-4f7b-87d1-8f7f6723f44e
My router is : e83747e7-521f-4f44-982f-0de1b2be4d19
1d6716c8-1f1b-4e90-a62e-a0be14417e78
0a5671c0-5de9-4198-a731-aff33e22a653
ce336df7-e58e-4297-9644-c8199f5e38cf
020fc1b6-6035-474b-8f6d-7c0890e94e6b
c0f238ef-cc94-48e7-9c98-e8883d9dd947
63d76480-e7d4-4ebf-9101-04b9e70ddd8d
c33d0c2a-8d87-48c7-b846-20f938a8f902
My email is c1f04434-c7e9-4d9a-a0a9-7a0651a046cd
a36aab91-9c25-4221-a7a4-a0ff01c8d752
this is my IP: 0c15d46a-67e7-4906-9dd4-ee520ab91b47
My router is: ca00a810-4ff8-4880-8983-9b6dbbeb06f8
12830911-20a9-45f8-ae04-9a4f807ee3b8
6b042458-83a2-4ce9-b029-c62e83180719
e1e8c2f3-5a9f-49ff-bc3e-cefe0f842274
611ccb57-ea69-41b6-946d-1284a1a345d0
492b72d2-cf23-477f-a02e-78bb04ad13ab
Base64 data
dd4e5123-c87a-4ff0-ba40-f7f601270484
d660b76c-c2ce-4401-90a6-35277a2def23
bbde787d-f515-4fcb-a583-e4d3d8185ca3
10c5d831-2728-45d0-8810-c0e6bb40a4c9
a5bac8dd-bd89-4bc8-94a9-b510beb88d6a
Singapore NRIC
c9a85803-e706-4322-99a0-e1c76705c4e8
05759c8a-a2e7-46d8-8739-bb6c97fb8117
0b29e289-a3af-4cbc-92d6-d044601a2458
be05fce6-7464-43cb-9164-914f8e63ff5c
b857a0c2-b108-44d5-b3ea-f0bc05e36dee
5eccbebc-f2a9-4420-a436-66f08a6f63c5
Card_Number,Card_Family,Credit_Limit,Cust_ID
b35843a8-6483-44ec-884c-868dd3296d34,Premium,530000,CC67088
d392cc27-d20b-4876-ae64-4196c5b05dd3,Gold,18000,CC12076
acb4d6d7-1c7c-42d1-a02c-6b229e2a9e4a,Premium,596000,CC97173
b92d943a-73d8-4318-955d-2e364836f641,Gold,27000,CC55858
e0b66cbd-6174-4491-b938-408a47d38fb9,Platinum,142000,CC90518
6b73619c-bcbf-4509-a064-1fb110f5dd45,Gold,50000,CC49168
24f31233-cba6-4f6a-a2d6-0ce49952b2cb,Premium,781000,CC66746
```

## Optional Help Menu as below

```bash
usage: prk [-h] [-u UNREDACT] [-d DIROUT] [-c CUSTOMFILE] [-r] [-e EXTENSION] [text ...]

Supply either a text chunk or file name path to redact sensitive data from it.

positional arguments:
  text                  Supply either a text chunk or file name path to redact sensitive data from command prompt. (default: <_io.TextIOWrapper name='<stdin>'
                        mode='r' encoding='utf-8'>)

options:
  -h, --help            show this help message and exit
  -u UNREDACT, --unredact UNREDACT
                        Option to unredact masked data. Usage: pyredactkit [redacted_file] -u [.hashshadow.json] (default: None)
  -d DIROUT, --dirout DIROUT
                        Output directory of the file. Usage: pyredactkit [file/filestoredact] -d [redacted_dir] (default: None)
  -c CUSTOMFILE, --customfile CUSTOMFILE
                        User defined custom regex pattern for redaction. Usage: pyredactkit [file/filestoredact] -c [customfile.json] (default: None)
  -r, --recursive       Search through subfolders (default: True)
  -e EXTENSION, --extension EXTENSION
                        File extension to filter by. (default: )
```

## Sample log files

- [All types of data](./logdata/test.txt)
- [Different log file types](./logdata/)
- [test_sample2.txt - 10002 lines of IP addresses](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/test_sample2.txt)

## Contributing 💡

Please read the [contributing guide](https://github.com/brootware/PyRedactKit/wiki/Contributing). You can propose a feature request opening an issue or a pull request.

<a href="https://github.com/brootware/PyRedactKit/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brootware/PyRedactKit" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
