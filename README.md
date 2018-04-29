# netmon

Command line network monitor for linux. Written in python.

[![asciicast](https://asciinema.org/a/178907.png)](https://asciinema.org/a/178907)

## Install

`pip install netmon`

## Run

`$ netmon`

By default `netmon` will try to detect your network device. If it fails, you can specify the network device, e.g., `netmon wlan1`

## Development

* PRs are more than welcome
* Building—`make build`
* Publishing—`make publish`
* Converting the markdown readme to `rst`—`make convert`
* `make clean`—a simple `git clean -fdx`