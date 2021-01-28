[![CircleCI](https://circleci.com/gh/cambackup/m3u8-generator.svg?style=svg)](https://circleci.com/gh/cambackup/m3u8-generator)

A Very simple m3u8 generator
============================

This is a simple m3u8 generator, it takes start, end, and duration and outputs a m3u8 (HLS)

Tested on :
Python 2.7.5 & 3.5

### Install
pip :
`pip install m3u8-generator`

clone this repo:
`git clone git@github.com:cambackup/m3u8-generator.git`

This is made using the draft [https://tools.ietf.org/html/draft-pantos-http-live-streaming-08](https://tools.ietf.org/html/draft-pantos-http-live-streaming-08)

### How to use
Let's say you have some video you want to serve

You will need :

- the path to the media (can be relative depending how you serve it)
- duration

You need to create a list containing one or more dictionaries :

```
from m3u8_generator import PlaylistGenerator
playlist_entries = [
                        {
                        'name':  "Awesomevideo_001.mp4",
                        'duration' : '10.04',
                        }

        ]

playlist = PlaylistGenerator(playlist_entries).generate()
```

The idea of this is to use no dependecy and be as fast as possible,
here at [cambackup.com](https://www.cambackup.com) we generate a lot of playlist, they need to be as fast as it can be.
any suggestion please let us know.
