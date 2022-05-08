# PyRedactKit 🔐📝

<p align="center">
  <img src="./images/asciiRedact.png" alt="Python Redactor Kit!"/>
<br />
<i>CLI tool to redact sensitive information like ip addresses, emails and domains.</i>
<br/>
<code>pip3 install pyredactkit && pyredactor</code>
</p>

<p align="center">
   <!-- <img alt="PyPI - Downloads" src="https://pepy.tech/badge/pyredactkit/month"> -->
   <img alt="PyPI - Downloads" src="https://pepy.tech/badge/pyredactkit">
   <a href="https://twitter.com/brootware"><img src="https://img.shields.io/twitter/follow/brootware?style=social" alt="Twitter Follow"></a>
   <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyredactkit"> <img alt="PyPI" src="https://img.shields.io/pypi/v/pyredactkit">
   <a href="https://sonarcloud.io/summary/new_code?id=brootware_PyRedactKit"><img src="https://sonarcloud.io/api/project_badges/measure?project=brootware_PyRedactKit&metric=reliability_rating" alt="reliability rating"></a>
   <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/brootware/pyredactkit/pylint?label=pylint">
</p>

## Features

Redacts the following from your text files. 📄 ✍️

- names 👤
- sg nric 🆔
- credit cards 🏧
- domain names 🌐
- emails ✉️
- ipv4 📟
- ipv6 📟

## Pre-requisites

- [Python3](https://www.python.org/downloads/) installed
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed

## How to use

Demo:
![demo](./images/pyredact.gif)

Quick install

```bash
python -m pip install pyredactkit
```

Redact a single file

```bash
pyredactkit ip_test.txt 
```

Install nltk data for redacting names

```bash
python -c "import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context =_create_unverified_https_context

nltk.download('popular')"
```

Redact names from text file

```bash
pyredactkit ip_test.txt -t name
```

### Use from github source

Clone the repo

```bash
git clone https://github.com/brootware/PyRedactKit.git && cd PyRedactKit
```

Install required dependencies via poetry and download nltk.

```bash
python -m pip install --user poetry
poetry install 
python -c "import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context =_create_unverified_https_context

nltk.download('popular')"
```

<!-- python -c "import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context =_create_unverified_https_context

nltk.download()" -->

Run as below to redact a single file

```bash
$ poetry run pyredactkit ip_test.txt 

    ______       ______         _            _     _   ___ _   
    | ___ \      | ___ \       | |          | |   | | / (_) |  
    | |_/ /   _  | |_/ /___  __| | __ _  ___| |_  | |/ / _| |_ 
    |  __/ | | | |    // _ \/ _` |/ _` |/ __| __| |    \| | __|
    | |  | |_| | | |\ \  __/ (_| | (_| | (__| |_  | |\  \ | |_ 
    \_|   \__, | \_| \_\___|\__,_|\__,_|\___|\__| \_| \_/_|\__|
           __/ |                                               
           |___/                                                                                                           
            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
            
    https://github.com/brootware
    https://brootware.github.io                                                                             
    
[ + ] Processing starts now. This may take some time depending on the file size. Monitor the redacted file size to monitor progress
[ + ] No option supplied, will be redacting all the sensitive data supported
[ + ] Redacted 10064 targets...
[ + ] Redacted results saved to ./redacted_ip_test.txt
```

Sample Result (Note that name is not redacted by default):

```txt
John, please get that article on ███████████████ to me by 5:00PM on Jan 9th 2012. 4:00 would be ideal, actually. If you have any questions, You can reach me at(519)-236-2723 or get in touch with my associate at ███████████████.
All rights reserved. Printed in the United States of America. No part of this book may be used or reproduced in any manner whatsoever without written permission except in the case of brief quotations embodied in critical articles and reviews. For information address HarperCollins Publishers, 10 East 53rd Street, New York, NY 10022. His name is David. I met him and John last week. Gowtham Teja Kanneganti is a good student. I was born on Oct 4, 1995. My Indian mobile number is +91-7761975545. After coming to USA I got a new number +1-405-413-5255. I live on 1003 E Brooks St, Norman, Ok, 73071. I met  a child, who is playing with josh.
this is my IP: ███████████████
My router is : ███████████████
███████████████
███████████████
███████████████
███████████████

███████████████

My email is ███████████████

this is my IP: ███████████████
My router is: ███████████████
███████████████
███████████████
███████████████
███████████████

Card_Number,Card_Family,Credit_Limit,Cust_ID
███████████████████,Premium,530000,CC67088
███████████████████,Gold,18000,CC12076
███████████████████,Premium,596000,CC97173
███████████████████,Gold,27000,CC55858
███████████████████,Platinum,142000,CC90518
███████████████████,Gold,50000,CC49168
███████████████████,Premium,781000,CC66746
```

To redact specific type of data. E.g (name)

```bash
poetry run pyredactkit test.txt -t name
```

Sample result:

```txt
███████████████, please get that article on www.linkedin.com to me by 5:00PM on Jan 9th 2012. 4:00 would be ideal, actually. If you have any questions, You can reach me at(519)-236-2723 or get in touch with my associate at harold.smith@gmail.com.
All rights reserved. Printed in the United States of America. No part of this book may be used or reproduced in any manner whatsoever without written permission except in the case of brief quotations embodied in critical articles and reviews. For information address HarperCollins Publishers, 10 East 53rd Street, New York, NY 10022. His name is ███████████████. I met him and ███████████████ last week. ███████████████ is a good student. I was born on Oct 4, 1995. My Indian mobile number is +91-7761975545. After coming to USA I got a new number +1-405-413-5255. I live on 1003 E ███████████████, Norman, Ok, 73071. I met  a child, who is playing with josh.
this is my IP: 102.23.5.1
My router is : 10.10.10.1
71.159.188.33
81.141.167.45
165.65.59.139
64.248.67.225
```

To redact multiple files from a directory and place it in a new directory

```bash
poetry run pyredactkit to_test/ -d redacted_dir
```

## Optional Help Menu as below

```bash
usage: pyredactkit [-h] [-t REDACTIONTYPE] [-d DIROUT] [-r] [-e EXTENSION] file [file ...]

Read in a file or set of files, and return the result.

positional arguments:
  file                  Path of a file or a directory of files

optional arguments:
  -h, --help            show this help message and exit
  -t REDACTIONTYPE, --redactiontype REDACTIONTYPE
                        Type of data to redact. names, nric, dns, emails, ipv4, ipv6 (default:
                        None)
  -d DIROUT, --dirout DIROUT
                        Output directory of the file (default: None)
  -r, --recursive       Search through subfolders (default: True)
  -e EXTENSION, --extension EXTENSION
                        File extension to filter by. (default: )
```

## Sample files

- [All types of data](https://raw.githubusercontent.com/brootware/PyRedactKit/main/test/test.txt)
- [itcont.txt - 4GB uncompressed](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/itcont.tar.gz)
- [test_sample2.txt - 10002 lines of IP addresses](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/test_sample2.txt)
