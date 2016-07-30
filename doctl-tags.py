#!/usr/bin/env python

import os
import subprocess
import json

def droplet_ip(droplet):
    for interface in droplet['networks']['v4']:
        if interface['type'] == 'public':
            return interface['ip_address']

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

groups = {}
ns = os.environ.get('DOCTL_INVENTORY_NAMESPACE')

for droplet in droplets:
    if ns and not droplet['name'].startswith(ns + '-'):
        continue
    for tag in droplet['tags'] + ['all']:
        if groups.get(tag):
            groups[tag]['hosts'].append(droplet_ip(droplet))
        else:
            groups[tag] = {}
            groups[tag]['hosts'] = [droplet_ip(droplet)]
            groups[tag]['vars'] = {}

print(json.dumps(groups))
