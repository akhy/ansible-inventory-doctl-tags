# ansible-inventory-doctl-tags

Ansible dynamic inventory script which groups DigitalOcean droplets by tag.

- Uses [doctl](https://github.com/digitalocean/doctl) (clue's in the name).
- Works well with [dobro](https://github.com/snoopdouglas/dobro), my
  'tag-centric' droplet manager. (let's be honest - dobro is why I wrote this)
- Requires Python 2.7+.


## Usage

As with any other dynamic inventory script, just copy `doctl-tags.py` into your
`inventory` directory, wherever that may be.

You'll need doctl authorised with a personal access token before running your
playbooks (`doctl auth login`).


## Groups

Each droplet will be placed into groups named exactly as its tags.

For example, if your droplet has tags `db` and `postgres`, it'll be placed into
two groups named `db` and `postgres`. That's it.


## Using with dobro

If your DigitalOcean account has droplets that weren't created under the dobro
umbrella but are still tagged, you can set an environment variable
`DOCTL_INVENTORY_NAMESPACE` to eg. `bro` (or whatever your dobro namespace is).
This will only produce an inventory of droplets whose name starts with `bro-`.
