#!/usr/bin/env python
import yaml
import json
list = [1,3,7,11,{'fullname':'Kevin Gee','forename':'Kevin','surname':'Gee'}]

#print list[4]['surname'] 
#print list

print yaml.dump(list, default_flow_style=False)
print json.dumps(list)

with open("list.yml", "w") as f:
    f.write(yaml.dump(list, default_flow_style=False))
with open("list.jsn", "w") as f:
#    f.write(json.dump(list,f))
    json.dump(list,f)
