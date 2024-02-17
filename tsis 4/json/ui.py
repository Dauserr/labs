import json
import pandas

jsonfile = open('labs/tsis 4\json\sample-data.json')

data = json.load(jsonfile)

pandas.json_normalize(data)

dframes = []

for indice in data["imdata"]:
    basa = pandas.DataFrame.from_dict(indice["l1PhysIf"], orient='index')
    dframes.append(basa)

result = pandas.concat(dframes)

print(result)
