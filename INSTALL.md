Mini-NDN Installing Instructions
================================

### What equipment will I need ?

Basically, you'll need a laptop/desktop with a recent Linux distro (Ubuntu, Fedora).
We recommend Ubuntu. For this guide, the _Ubuntu 14.04 LTS_ was used.
Also, note that you'll need administrative privileges in order to download and install
extra packages and also to execute **Mini-NDN**.

### Installing NDN

Each node in **Mini-NDN** will run the official implementation of NDN. The following dependencies are needed:

Mini-NDN uses NFD, NLSR, and ndn-tlv-ping.

To install NFD:
http://named-data.net/doc/NFD/current/INSTALL.html

To install NLSR:
http://named-data.net/doc/NLSR/current/INSTALL.html

To install ndn-tools:
https://github.com/named-data/ndn-tools

### Installing Mininet-Wifi

**Mini-NDN-Wifi** is based on Mininet-Wifi. To install Mininet-Wifi:
https://github.com/intrig-unicamp/mininet-wifi

### Installing **Mini-NDN**

If you have all the dependencies installed simply clone this repository and run:

    sudo ./install.sh -i

else if you don't have the dependencies:

    sudo ./install.sh -mrfti

### Verification

You can use these steps to verify your installation:

1. Issue the command: `sudo minindn --experiment=pingall --nPings=50`
2. When the `mininet>` CLI prompt appears, the experiment has finished. On the Mini-NDN CLI, issue the command `exit` to exit the experiment.
3. Issue the command: `grep -c content /tmp/*/ping-data/*.txt`. Each file should report a count of 50.
4. Issue the command: `grep -c timeout /tmp/*/ping-data/*.txt`. Each file should report a count of 0.
