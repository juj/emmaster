# Emscripten SDK Build Master CI

This repository contains the buildbot master scripts for the Emscripten project.

## Installation

To set up a build master on a clean Linux system, run

1. Clone emmaster repository:

```bash
cd ~
git clone https://github.com/juj/emmaster.git
```

2. Set up needed apt-get preliminaries (following apply on an Ubuntu Linux 16.04 Server):

```bash
sudo apt update
sudo apt install python-minimal python-pip
sudo -H pip install --upgrade pip
sudo -H pip install 'buildbot[bundle]'
```

2. Create buildbot master:

```bash
cd ~/emmaster/master
buildbot create-master
rm master.cfg.sample # This is a redundant template file that gets generated
```

More information about this step can be found in http://docs.buildbot.net/latest/tutorial/firstrun.html

3. Configure build master secret (and public) information (passwords and web ports):

```bash
cd ~/emmaster/master
cp secret.template.py secret.py
pico secret.py
```

4. Start master:

```bash
cd ~/emmaster/master
buildbot start
```

5. Configure Amazon EC 2 firewall to accept inbound connections to the configured ports. This is done by logging in to Amazon EC2 configuration in the browser, navigating to the instance, editing its Security Group properties on Inbound panel, and specifying the inbound access rules. Three rules need to be present:

a. Inbound TCP/HTTP traffic for Buildbot Web GUI access (by default port 8112 in secret.py, see variable buildmaster_web_gui_port)
b. Inbound TCP traffic to buildbot slave listen port (by default port 9989 in secret.py, see variable buildmaster_slave_listen_port)
c. The default rule to accept inbound SSH traffic on port 22. (this already exists by default, don't erase it with the above)

For more information about this step, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html

Finally, set up all build slaves and point them to this buildbot master server.

## Maintenance

Edits can be made live in master.cfg and/or secret.py, but in order for them to apply, execute `buildbot reconfig` in `~/emmaster/master/` if the buildbot master is live, or `buildbot stop` followed by `buildbot start` to do a full restart.
