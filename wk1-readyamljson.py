#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp
with open("list.yml") as f:
    yaml_list = yaml.load(f)
print "YAML format is:"
print yaml.dump(yaml_list,default_flow_style=False)
with open("list.jsn") as f:
    json_list = json.load(f)
#print(json_list)
print "JSON format is"
pp(json_list)
