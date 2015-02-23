# -*- coding: utf-8 -*-
from yaml import load, dump

from Consts import *


# datamap
dataMap = dict()
try:
    f = open(GLOBAL_CONFIG_FILE)
    dataMap = load(f)
    f.close()
except Exception, e:
    print "config.yaml : Error %d: %s" % (e.args[0], e.args[1])

# 1. MySql
MYSQL_CONFIG.set_config(dataMap)

# 2. GetFollow
GET_FOLLOW_CONFIG.set_config(dataMap)

# 10. save yaml
f = open(GLOBAL_CONFIG_FILE, "w")
dump(dataMap, f, default_flow_style=False)
f.close()

print "dataMap:", dataMap
