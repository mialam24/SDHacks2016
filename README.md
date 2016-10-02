# SDHacks2016

Ismail Alam

Eric Chen

Son Tang

Jeffrey Phung

## Description: 
This is a Twitch chat bot that parses incoming Twitch messages and uses that to create Mad Lib styled sentences that will display in Twitch chat. In addition to this, we have utilized the default Twitch emotes keywords. So if whenever a keyword is typed, the respective emote will display in the Mad Lib sentences.

<a href="https://twitchemotes.com/" target="_blank">[List of default Twitch emotes]</a>

Another feature of this bot is the ability to record the number of messages in chat in certain time intervals. This can than be used to determine when the stream is popping off: to record and find highlights quicker and easier.

## Overview:

Def.py - Handles all the logic to parse Twitch messages

Run.py - the driver

Initialize.py - Connects to channel room

Settings.py - Twitch IRC Authentication

Socket.py - Python Socket Connections

templates.py - Default Mad lib sentences

## Prerequites:
-Python 2.7.*

## How to run:
`python Run.py`

## Commands list:

`*liquidslam - generates Mad Lib`

`*restart - restarts bot`

`*ping - returns PONG`

`*shutdown - shutdowns bot`

`*msgrecord - records frequency of messages in a given interval (seconds)`

**REMEMBER TO**: change the pass, ident, and channel values in
settings.py!

