# Minecraft API

## Features

* **Get Fulltime Status of Servers**
* **No API Keys needed**
* **Get Information in just seconds!**

## How to Use

```python
import mcsvrstatAPI # if this does not work, please check sol#1

# sol#1
import importlib
api = importlib.import_module('mcsvrstatAPI') # msut be in the same directory!

# create mcsvrstatAPI object
mcsrv = api.mcserverstatus()

server = "mc.hypixel.net"

# get Status
if mcsrv.getStatus(server) == True:
    print("Status: Online")
elif mcsrv.getStatus(server) == False:
    print("Status: Offline")
else:
    print("Error")

# Get the min/max players in the server
print("Players: "+ str(mcsrv.getPlayers(server, 'online')) + "/" + str(mcsrv.getPlayers(server, 'max')))

# Get the MOTD of the server
print("MOTD: " + mcsrv.getMotd(server, 'html'))
```
