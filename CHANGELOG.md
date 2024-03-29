# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The Changelog starts with v0.3.3, because we did not keep one before that,
and simply didn't have the time to go back and retroactively create one.

## [Unreleased]

### Fixed

- None at the moment.

### Added

- Added in redaction support from linux piped input.
  - echo 'This is my ip: 127.0.0.1. My email is brute@gmail.com. My favorite secret link is github.com' | prk
- Added docker support to run the app from docker.

## [1.0.2] - 2022-08-11

- testing docker build and push action from github.

## [1.0.1] - 2022-08-11

- testing docker build and push action from github.

## [1.0.0] - 2022-08-11

- Added in redaction support from linux piped input.
  - `echo 'This is my ip: 127.0.0.1. My email is brute@gmail.com. My favorite secret link is github.com' | prk`
- Added docker support to run the app from docker.
  - `docker run -v "$(pwd):/home/nonroot/workdir" brootware/pyredactkit 'This is my ip: 127.0.0.1. My email is brute@gmail.com. My favorite secret link is github.com'`

## [0.4.0] - 2022-07-27

Making sure only sensitive string is in the api detection

### Changed

- Making sure only sensitive string is in the api detection

## [0.3.9] - 2022-07-27

Fixed the api from not identifying base64 text.

### Changed

- Fixed the api from not identifying base64 text.

## [0.3.8] - 2022-07-26

PyRedactKit can now smartly detect if your input is a text sentence or a file thanks to the latest AI based on 'If,else' implemented by the author. :D

### Changed

- No need to use -f switch to redact file anymore. `prk [file/directory_with_files]` will redact the file just fine.

## [0.3.7] - 2022-07-24

Credit card redaction should be working properly now.

### Changed

- Credit card redaction should be working properly now.

## [0.3.6] - 2022-07-24

Noticed cli breaking changes in 0.3.5. Fixed in 0.3.6.

### Changed

- Noticed cli breaking changes in 0.3.5. Fixed in 0.3.6.

## [0.3.5] - 2022-07-24

Made fixes to the api, refactored pyredactkit to runner.

### Changed

- No notable changes in this version.

## [0.3.4] - 2022-07-24

Added API support to identify core redaction patterns.

### Changed

- No notable changes in CLI functionality

## [0.3.3] - 2022-07-24

Started automating Pypi publishing via github actions.

### Changed

- No notable changes.
