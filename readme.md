
# Wifi Stats Utility

I was procrastinating and avoiging physics homework.

# System dependencies

Assuming a linux system which already has `python3`:

```bash
sudo pacman -Syu nmap || sudo apt-get install -y nmap || sudo yum install -y nmap
sudo pip3 install ifaddr
```

`nmap` is used to scan the network and `ifaddr` is a python library used to easily get your local network CIDR mask,
which identifies how large your network is and what numbers fall inside it.

# Usage

## Passive observing people connected to LAN

```bash
sudo ./wifi-stats.py
```

You may be interested in using a technique like the one outlined here to reduce the number of times you need to type your password to send privledged packes: https://askubuntu.com/a/159009

Output:

```
Unidentified mac 78:4f:43:76:ab:74 vendor = Apple
Unidentified mac f8:62:14:34:ee:b3 vendor = Apple
Unidentified mac 34:42:62:3f:83:91 vendor = unknown
We see mac cc:fd:17:ed:0b:92 which belongs to Jeffrey Phone
Unidentified mac 34:08:bc:0b:2b:f3 vendor = Apple
Unidentified mac f0:18:98:44:6d:df vendor = unknown
Unidentified mac b0:39:56:73:95:d1 vendor = Netgear
We see 6 people in the innovation center and we know 1 of them.
```

## Active adding someone to the known list

```bash
sudo ./wifi-stats.py cc:fd:17:ed:0b:92 "Jeffrey's phone"
```



