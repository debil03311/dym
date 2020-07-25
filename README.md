# dym
A tool that logs things like online players and chat messages sent on certain Minecraft servers by scraping their respective online [dymaps](https://github.com/webbukkit/dynmap/wiki). Dym was created with small servers in mind, so trying it on large servers might not work out too well since there's a large amount of stuff to log.

[Selenium](https://pypi.org/project/selenium/) is the only dependency so far.

## How it works
Dym uses selenium to create a headless browser instance (i.e. no GUI) to open the desired dynmap webpage, waits for everything on the page to load and then looks for text to log down on your local machine.

As of right now it's quite barebones, it only logs online players and if you want it to use a browser other than Firefox you'll have to modify some of the code yourself.

## Planned features
- Log chat
- Take map screenshots at specified interval(s)
- Error/exception handling
- TUI
- Initial configuration wizard
- Select other worlds present on the server
- Modifiable variables (e.g. checking intervals)

## Known issues
- Browser instances don't ever get closed, so they keeps running in the background even in the event of a crash or when you terminate the script manually. You'll have to kill them manually for now (in Task Manager or by pid)
