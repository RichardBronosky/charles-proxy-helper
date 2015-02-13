#! /usr/bin/env python
"""
This is a simple script intended to allow you to quickly update a PAC file for use with
http://www.charlesproxy.com/ on a mobile device. Place this script in a Publicly accessible
location (like on Dropbox) and run it. It will create/update proxy.pac which you can then
set up as the "HTTP Proxy : Auto : URL" on iPhone or "Proxy Auto-Config : PAC URL" on Android. 
NOTES:
1. For convenience I suggest creating a j.mp aka: bit.ly custom URL bease redirects are respected.
2. The mobile device has to be on the same WiFi network as the computer in order for this to work.
3. No need to remove the configuration because it fails gracefully if the proxy isn't available.
"""

import socket
from contextlib import closing

pac_file = 'proxy.pac'

with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as s:
  # making a connection to the oytside world is the most reliable way to know what interface to get the ip address from
  s.connect(('8.8.8.8', 80))
  proxy_ip = s.getsockname()[0]

with open(pac_file, 'w') as f:
  f.write("""
function FindProxyForURL(url, host)
{{
    return "PROXY {proxy_ip}:8888; DIRECT";
}}
""".format(proxy_ip=proxy_ip))

print "Updated {pac_file} with {proxy_ip}".format(pac_file=pac_file, proxy_ip=proxy_ip)
print "Recommended ACL CIDR: {a}.{b}.0.0/16".format(**dict(zip(('a','b'),proxy_ip.split('.'))))
