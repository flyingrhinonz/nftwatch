
nftwatch
========

![](nftwatch.png)

Copyright (C) 2021-2022 Kenneth Aaron.

flyingrhino AT orcon DOT net DOT nz

Freedom makes a better world: released under GNU GPLv3.

https://www.gnu.org/licenses/gpl-3.0.en.html

This software can be used by anyone at no cost, however,
if you like using my software and can support - please
donate money to a children's hospital of your choice.

This program is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation:
GNU GPLv3. You must include this entire text with your
distribution.

This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.
See the GNU General Public License for more details.


About nftwatch
--------------

* Shows nftables policy in a more readable format.
* Live counters table.
* User-configurable refresh speed
* Pause display refresh


Manual install instructions
---------------------------

* Clone/download the project from the git repository.
* Copy:  /etc/nftwatch.yml
* Copy:  /usr/local/bin/nftwatch  and:  +x  it.
* nftwatch  with no args to run it.
* nftwatch -m  for this man page.


Configuring nftwatch
--------------------

Some configs are in:  nftwatch.yml
Others are hardcoded into the code - subject to improvement.
Config file will be loaded from these paths - whichever
is found first. If no config file is found - builtin
defaults will be used.

* ~/.config/nftwatch/nftwatch.yml
* ~/.nftwatch.yml
* ~/nftwatch.yml
* /etc/nftwatch.yml


Controls
--------

nftwatch is designed for interactive use. Simply run it
and it will start displaying your nftables stats.

The following keyboard controls are available:

- f:                Speed up the display refresh
- s:                Slow down the display refresh
- p:                Pause the display refresh
- Up/Down arrows:   Scroll the table up/down
- Home/End:         Jump to table top/bottom
- PgUp/PgDn:        Page up/down in the table
- Space:            Same as page down
- Ctrl-q or q:      Quit


Man page
--------

* nftwatch -m  for this man page.


Troubleshooting
---------------

Increase the logging verbosity with:  nftwatch -d
or permanently increase it in the code by changing this
line:  LogLevel = logging.DEBUG
Check journalctl for nftwatch logs.


Limitations
-----------

- This is the first release of nftwatch.
- There could be bugs.
- It can be improved.
- Features can be added.
- nftwatch is tied to the nft output. Any changes in nft
output will break nftwatch.
- Supports up to 9999 lines and handles before display may
get messed up. Should be enough for most use cases though.

I initially wrote nftwatch because I wanted a realtime
running output from nftables that was better than simply
looping it through:  `watch`. As of now - nftwatch serves
its purpose. Let's see what feature requests I receive and
if nftwatch can be improved for more use cases.


