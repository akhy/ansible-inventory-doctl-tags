#!/usr/bin/env python

import os
import subprocess
import json

# helper: get public IPv4 of droplet
def droplet_ip(droplet):
    for interface in droplet['networks']['v4']:
        if interface['type'] == 'public':
            return interface['ip_address']


# decode output from `doctl compute droplet list --output json`
droplets = json.loads(
    subprocess.check_output([
        'doctl',
        'compute',
        'droplet',
        'list',
        '--output',
        'json',
    ])
)


# prepare the extraction*
groups = {}
ns = os.environ.get('DOCTL_INVENTORY_NAMESPACE')

# Ansible is expecting JSON input in the following format:
# {
#   "group": {
#     "hosts": [
#       "123.234.56.78",
#       ...
#     ],
#     "vars": {
#       ... (we don't add vars)
#     }
#   }
# }

for droplet in droplets:

    # if using DOCTL_INVENTORY_NAMESPACE, reject droplets whose names don't
    # start with '<NAMESPACE>-'
    if ns and not droplet['name'].startswith(ns + '-'):
        continue

    # ensure all droplets are included in 'all' group
    for tag in droplet['tags'] + ['all']:
        if groups.get(tag):
            # group already exists, append IP
            groups[tag]['hosts'].append(droplet_ip(droplet))
        else:
            # group doesn't exist, create it and add this droplet's IP to it
            groups[tag] = {}
            groups[tag]['hosts'] = [droplet_ip(droplet)]
            groups[tag]['vars'] = {}


# sorted mate
print(json.dumps(groups))


# *sounds pretty evil right
# **it's not, promise
