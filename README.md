## SDHacks2016

Ismail Alam

Eric Chen

Son Tang

Jeffrey Phung

# Description: 
This is a Twitch chat bot that parses incoming Twitch messages and uses that to create Mad Lib styled sentences that will display in Twitch chat. In addition to this, we have utilized the default Twitch emotes keywords. So if whenever a keyword is typed, the respective emote will display in the Mad Lib sentences.

[List of default Twitch emotes](https://twitchemotes.com/)

# Overview:

Def.py - Handles all the logic to parse Twitch messages
Initialize.py - Connects to channel room
Settings.py - Twitch IRC Authentication
Socket.py - Python Socket Connections
templates.py - Default Mad lib sentences

# Prerequites:
-Python 2.7.*

**REMEMBER TO**: change the pass, ident, and channel values in
settings.py!

