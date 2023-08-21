#!/usr/bin/env python
import subprocess
import json

# Run a command to get SSH key fingerprints
command = "ssh-keygen -l -E sha256 -f /etc/ssh/ssh_host_rsa_key.pub"
output = subprocess.check_output(command, shell=True).decode("utf-8")

# Extract the fingerprints
fingerprints = [line.split()[1] for line in output.splitlines()]

# Construct the dynamic inventory
inventory = {
    "_meta": {
        "hostvars": {
            "my_server": {
                "ssh_fingerprints": fingerprints
            }
        }
    },
    "all": {
        "children": ["my_group"]
    },
    "my_group": {
        "hosts": ["my_server"]
    }
}

print(json.dumps(inventory))
