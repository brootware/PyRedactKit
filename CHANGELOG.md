# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The Changelog starts with v0.3.3, because we did not keep one before that,
and simply didn't have the time to go back and retroactively create one.

## [Unreleased]

### Fixed

- Fixed `shlex.join` use with non-str type objects (e.g. `RemotePath`)
- Fixed `set` command use with incorrect keys (e.g. `set invalid value`)

### Added

- Added missed `PlatformError` for `upload` command (e.g. "no gtfobins writers available")

## [0.3.3] - 2022-07-24

Started automating Pypi publishing via github actions.

### Changed

- No notable changes.
