# ansible-inventory-doctl-tags

Ansible dynamic inventory script which groups DigitalOcean droplets by tag.

- Uses [doctl](https://github.com/digitalocean/doctl) v1.1.0+ (clue's in the name).
- Works well with [dobro](https://github.com/snoopdouglas/dobro), my
  'tag-centric' droplet manager. (let's be honest - dobro is why I wrote this)
- Requires Python 2.7+.


## Usage

As with any other dynamic inventory script, just copy `doctl-tags.py` into your
`inventory` directory, wherever that may be.

You'll need doctl authorised with a personal access token before running your
playbooks (`doctl auth login`) or [see below](#specify-an-api-token).


## Groups

Each droplet will be placed into groups named exactly as its tags.

For example, if your droplet has tags `db` and `postgres`, it'll be placed into
two groups named `db` and `postgres`. That's it.


## Specify an API token

If you don't want to use the token specified with `doctl auth login`, set the
`DOCTL_INVENTORY_API_TOKEN` environment variable.


## Blacklist or whitelist droplets by tag

You can specify a space-delimited list of tags to the
`DOCTL_INVENTORY_IGNORE_TAGS` and/or `DOCTL_INVENTORY_ONLY_TAGS` environment
variables respectively.


## Note on usage with dobro

If your DigitalOcean account has droplets that weren't created under the dobro
umbrella but are still tagged, you can set an environment variable
`DOCTL_INVENTORY_NAMESPACE` to eg. `bro` (or whatever your dobro namespace is)
in order to target only those droplets. This will only produce an inventory of
droplets whose name starts with `bro-`.
