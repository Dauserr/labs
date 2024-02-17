import json

jsonfile = open('labs/tsis 4\json\sample-data.json')

data = json.load(jsonfile)
print("Interface Status")
print("================================================================================")
print("DN                                  x.                Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print(dn,"\t\t\t\t" ,speed," ",mtu)
