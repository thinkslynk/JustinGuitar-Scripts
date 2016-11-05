# JustinGuitar-Scripts
Scripts to automate various tasks for justinguitar.com products

## extractFromISO.py

A script to export your iso as mp4s. You can purchase justinguitar isos here:

http://www.justinguitar.com/en/PR-667-ISO-files.php

### Setup
First ensure that you have handbrake and handbrake cli installed:

Handbrake -- https://handbrake.fr/ 

Handbrake CLI -- https://handbrake.fr/downloads2.php

You can double check by opening your terminal / command prompt and typing:

```
handbrakecli --help
```

Which should present you with a wall of text.

Next ensure you have python installed (3.x should work, but I've only tested with 2.x):

Python -- https://wiki.python.org/moin/BeginnersGuide/Download

You can double check by opening your terminal / command prompt and typing:

```
python -h
```

### Usage
Simply mount the iso and call the script as follows:

```
./extractFromISO.py /path/to/the/dvd/ /path/to/save/files/
```

Follow the on screen prompts for choosing the which product the iso is, which disc you're using, and what quality you want to expor to. Note that transcoding files may take upwards of a few hours on slow computers. So if the script looks like it's frozen, just give it some time.
