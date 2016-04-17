#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
cfg = CiscoConfParse ("cisco_ipsec.txt")
crypto_maps = cfg.find_objects("^crypto map CRYPTO")

#Excercise 8, part1
#find all lines that begin with 'crypto map CRYPTO'& for each crypto map entry print out its children
print "These are cryto map lines"
for crypto in crypto_maps:
  print crypto.text
  for child in crypto.children:
   print child.text

#Excercise 8, part2:show crypto maps that have pfs group 2
print "These Crypto maps have pfs group 2"
pfs2 = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")
for i in pfs2:
  print i.text

#Excercise 8, part2:show crypto maps that aren't using AES and also print transform set
print "Find MAPS not using AES"
#aes = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-SHA")
aes = cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec="set transform-set AES-SHA")
for each in aes:
  print each.text
  for child in each.children:
    print child.text
