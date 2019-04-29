
# Wifi Stats Utility

I was procrastinating and avoiging physics homework.

# Usage

## Passive observing people connected to LAN

```bash
sudo ./wifi-stats.py
```

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



