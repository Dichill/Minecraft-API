# Author Dichill

import requests

class mcserverstatus:
    def __init__(self):
        self.api_url = 'https://api.mcsrvstat.us/2/'

    def __repr__(self):
        return 'Object: mcsrvstat ({})'.format('api.mcsrvstat.us')
    def isUp(self):
        res = requests.get("https://mcsrvstat.us/")
        if res.status_code == 200:
            return True
        else:
            return False

    def getRequest(self, server):
        r = requests.get(self.api_url + server)
        return r.json()

    def api(self, server):
        return self.getRequest(server)

    # Commands
    def getStatus(self, server):
        a = self.api(server)['online']
        if a == True:
            return True
        elif a == False:
            return False
        else:
            return print("Error")

    def getMotd(self, server, option):
        a = self.api(server)['motd']
        if option.casefold() == "raw"
            return str(a['raw'])
        elif option.casefold() == "clean":
            return str(a['clean'])
        elif option.casefold() == "html":
            return str(a['html'])
        else:
            return print("Error | Format must be getMotd(server, option) e.g getMotd('invadedlands.net', 'raw') gets the motd in raw text | getMotd('invadedlands.net', 'clean') gets the motd in clean text | getMotd('invadedlands.net', 'html') gets the motd in html format")

    def getPlayers(self, server, option):
        a = self.api(server)['players']
        if option.casefold() == "online":
            return a['online']
        elif option.casefold() == "max":
            return a['max']
        else:
            return print("Error | Format must be getPlayers(server, option) e.g getPlayers('invadedlands.net', 'max') gets the max numbers of allowed players in a server, getPlayers('invadedlands.net', 'online') gets the online numbers of players in the server")

    def getVersion(self, server):
        a = self.api(server)['version']
        return a

    def getHostname(self, server):
        a = self.api(server)['hostname']
        return a

    def getSoftware(self, server):
        a = self.api(server)['software']
        return a

    def getIP(self, server):
        a = self.api(server)['ip']
        return str(a)
