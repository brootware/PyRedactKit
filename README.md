# PyRedactKit 🔐📝

<p align="center">
  <img src="./images/asciiRedact.png" alt="Python Redactor Kit!"/>
<br />
<i>CLI tool to redact sensitive information like ip address, email and dns.</i>
</p>

## Features

Redacts the following from your text files. 📄 ✍️

- names 👤
- credit cards 🏧
- dns 🌐
- emails ✉️
- ipv4 📟
- ipv6 📟

## Pre-requisites

- [Python3](https://www.python.org/downloads/) installed
- [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed

## How to use

Demo:
![demo](./images/pyredact.gif)

Clone the repo

```bash
git clone https://github.com/brootware/PyRedactKit.git && cd PyRedactKit
```

Run as below to redact a single file

```bash
$ python pyredactkit.py test.txt
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
     
[ + ] Processing starts now. This may take some time depending on the file size. Monitor the redacted file size to monitor progress
[ + ] No option supplied, will be redacting all the sensitive data supported

[ + ] Redacted 36 targets...
[ + ] Took 0.0026597976684570312 seconds to execute
```

Sample Result:

```txt
████, please get that article on ████████████████ to me by 5:00PM on Jan 9th 2012. 4:00 would be ideal, actually. If you have any questions, You can reach me at(519)-236-2723 or get in touch with my associate at ██████████████████████
this is my IP: ██████████
My router is : ██████████
█████████████
█████████████
█████████████
█████████████

███████████████████

My email is ███████████████

this is my IP: ██████████
My router is: ██████████
█████████████
█████████████
█████████████
█████████████

Card_Number,Card_Family,Credit_Limit,Cust_ID
███████████████████,Premium,530000,CC67088
███████████████████,Gold,18000,CC12076
███████████████████,Premium,596000,CC97173
███████████████████,Gold,27000,CC55858
███████████████████,Platinum,142000,CC90518
███████████████████,Gold,50000,CC49168
███████████████████,Premium,781000,CC66746
```

To redact specific type of data. E.g (ipv4)

```bash
python pyredactkit.py test.txt -t ipv4
```

To redact multiple files from a directory and place it in a new directory

```bash
python pyredactkit.py to_test/ -d redacted_dir
```

## Optional Help Menu as below

```bash
usage: pyredactkit.py [-h] [-t REDACTIONTYPE] [-d DIROUT] [-r] [-e EXTENSION] path [path ...]

Read in a file or set of files, and return the result.

positional arguments:
  path                  Path of a file or a directory of files

optional arguments:
  -h, --help            show this help message and exit
  -t REDACTIONTYPE, --redactiontype REDACTIONTYPE
                        Type of data to redact. names, dns, emails, ipv4, ipv6, names (default:
                        None)
  -d DIROUT, --dirout DIROUT
                        Output directory of the file (default: None)
  -r, --recursive       Search through subfolders (default: True)
  -e EXTENSION, --extension EXTENSION
                        File extension to filter by. (default: )
```

## Sample files

- [All types of data](https://raw.githubusercontent.com/brootware/PyRedactKit/main/test/test2.txt)
- [itcont.txt - 4GB uncompressed](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/itcont.tar.gz)
- [test_sample2.txt - 10002 lines of IP addresses](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/test_sample2.txt)
