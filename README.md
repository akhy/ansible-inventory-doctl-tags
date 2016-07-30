# ansible-inventory-doctl-tags

Ansible dynamic inventory script which groups DigitalOcean droplets by tag.

- Uses [doctl](https://github.com/digitalocean/doctl) (clue's in the name).
- Works well with [dobro](https://github.com/snoopdouglas/dobro), my
  'tag-centric' droplet manager. (let's be honest - dobro is why I wrote this)

## Usage

As with any other dynamic inventory script, just copy `doctl-tags.py` into your
`inventory` directory, wherever that may be.

You'll need doctl authorised with a personal access token before running your
playbooks (`doctl auth login`).
