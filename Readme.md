DUAL-ISP FAILOVER WITH ZBF

This lab demostrates dual ISP failover facilitated by IPSLA with object tracking.
This aids in dynamically adding a backup floating static route when the primary path to the internet fails.

Zone based filewall facilitates stateful inspection of traffic leaving the LAN towards the internet, by using 
the concept of Security zones.

Traffic leaving and entering the network is captured (via Inspect device), which may act as an IDS; this is by
sending all traffic to the device (SPAN) to be scanned and/or analyzed.

The server acts a DHCP server for clients in 10.1.68.0/24 prefix

Automation is used for information gathering and inventory purposes.

Devices used:

  -  Routers/Firewall : i86bi-linux-l3-adventerprisek9-ms.155-2.T.bin
  -  Inspect : Osinato/Wireshark docker
  -  Server : Win2k16_14393.0.161119-1705.RS1_REFRESH_SERVER_EVAL_X64FRE_EN-US.ISO
  -  PC : Webterm docker


