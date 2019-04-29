#!/usr/bin/env python3

import os, sys, subprocess
import pickle, time
import xml.etree.ElementTree as ET

# sudo pip3 install ifaddr
import ifaddr

pickle_file = "./wifi-stats-memory.bin"

if __name__ == '__main__':
  
  mac_to_name_map = {}
  if os.path.exists(pickle_file):
    try:
      with open(pickle_file, "rb") as f:
        mac_to_name_map = pickle.load(f)
    except Exception as e:
      print("{}".format(e))
  
  if len(sys.argv) > 2:
    mac = sys.argv[1].lower()
    human = sys.argv[2]
    print("Adding identity map for mac {} to human '{}'".format(mac, human))
    
    mac_to_name_map[mac] = human
    
    with open(pickle_file, "wb") as f:
      pickle.dump(mac_to_name_map, f)
    
    
    sys.exit(0)
  
  # Normal execution
  
  refresh_s = 5.0
  if len(sys.argv) > 1:
    refresh_s = float(sys.argv[1])
  
  print("refresh_s={}".format(refresh_s))
  
  
  adapters = ifaddr.get_adapters()
  cidr_to_scan = None
  for adapter in adapters:
    if adapter.nice_name == "lo":
      continue # ignore localhost
    #print("IPs of network adapter " + adapter.nice_name)
    #for ip in adapter.ips:
    #  print("   %s/%s" % (ip.ip, ip.network_prefix))
    for ip in adapter.ips:
      # ipv4 only please
      if not ":" in str(ip.ip)+str(ip.network_prefix):
        cidr_to_scan = "{}/{}".format(ip.ip, ip.network_prefix)
  
  if not cidr_to_scan:
    print("ERROR: cannot determine a LAN to scan!")
    sys.exit(5)
  
  
  print("Scanning CIDR {}".format(cidr_to_scan))
  time.sleep(0.5)
  
  while True:
    #"nmap -sn 10.5.0.0/24"
    
    try:
      nmap_data = subprocess.check_output(["nmap", "-oX", "-", "-sn", cidr_to_scan])
      nmap_data = nmap_data.decode("utf-8")
      
      root = ET.fromstring(nmap_data)
      
      # Clear screen
      print("\n" * 100)
      
      # Print report
      total_known = 0
      total_people = -1 # router doesn't count
      for neighbor in root.iter('host'):
        for addr in neighbor.findall('address'):
          if addr.attrib['addrtype'].lower() == "mac":
            their_mac = addr.attrib['addr'].lower()
            if their_mac in mac_to_name_map:
              print("We see mac {} which belongs to {}".format(their_mac, mac_to_name_map[their_mac] ))
              total_known += 1
            else:
              print("Unidentified mac {} vendor = {}".format(their_mac, addr.attrib['vendor'] if 'vendor' in addr.attrib else "unknown" ))
              
            total_people += 1
      
      # Sumary
      print("We see {} people in the innovation center and we know {} of them.".format(total_people, total_known))
      
    except Exception as e:
      print("{}".format(e))
    
    
    try:
      with open(pickle_file, "wb") as f:
        pickle.dump(mac_to_name_map, f)
    except Exception as e:
      print("{}".format(e))
      
    time.sleep(refresh_s)