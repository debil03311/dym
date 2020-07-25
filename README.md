# dym
A tool that logs things like online players and chat messages sent on certain Minecraft servers by scraping their respective online [dynmaps](https://github.com/webbukkit/dynmap/wiki) at certain specified intervals. Dym was created with small servers in mind, so trying it on large servers might not work out too well since there's a large amount of stuff to constantly log.

[Selenium](https://pypi.org/project/selenium/) is the only dependency so far.

## How it works
Dym uses selenium to create a headless browser instance (i.e. no GUI), opens the desired dynmap webpage, waits for everything on the page to load and then looks for text to log down on your machine.

It's really barebones as of right now, only logging online players. If you want to have it use a browser other than Firefox you'll have to modify some of the code yourself.

## Planned features
- Log chat
- Take map screenshots at specified interval(s)
- Error/exception handling
- TUI (GUI?)
- Initial configuration wizard
- Modifiable variables (e.g. intervals for checking)
- Select other worlds present on the server
- Clean up the logging feed (so no dupes)

## Known issues
- Browser instances don't ever get closed, so they keep running in the background even in the event of a crash or when you terminate the script manually. You'll have to kill them manually for now (in Task Manager or by pid)
