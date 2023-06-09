#!/usr/bin/env python
# Quick and dirty script to generate all console proxy dns mappings to append to
# the host file used for all cloudstack nodes
#
# usage: ./generate-consoleproxy-hosts.py >> hosts.j2

print("")
print("# ip address mappings for ssl console proxies")

ip_pre="192.168.0"
dash_pre="192-168-0"
for addr in range(1, 255):
    print("%s.%d %s-%d %s-%d.harter.priv %s-%d.consoleproxy.harter.priv" % (ip_pre, addr, dash_pre, addr, dash_pre, addr, dash_pre, addr))
