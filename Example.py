#author Dichill

import importlib
api = importlib.import_module('mcsrvstatAPI')

mcsrv = api.mcserverstatus()
server = "mc.hypixel.net"

print("Server: " + server)
print("IP: " + mcsrv.getIP(server))
if mcsrv.getStatus(server) == True:
    print("Status: Online")
elif mcsrv.getStatus(server) == False:
    print("Status: Offline")
else:
    print("Error")

print("MOTD: " + mcsrv.getMotd(server, 'html'))
print("Players: "+ str(mcsrv.getPlayers(server, 'online')) + "/" + str(mcsrv.getPlayers(server, 'max')))
print("Hostname: " + mcsrv.getHostname(server))
