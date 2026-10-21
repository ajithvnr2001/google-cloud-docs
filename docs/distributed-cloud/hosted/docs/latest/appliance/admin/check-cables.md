---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/check-cables/
title: Verify the cable connections \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:38.908574+00:00
---

# Verify the cable connections  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/check-cables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Verify the cable connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to verify the network cabling for Google Distributed Cloud (GDC) air-gapped appliance, and connect the bootstrapper device.

Refer to the following images while following the instructions.

**Figure 1.** The TOR switch, with labelled ports.

![TOR switch with numbers identifying certain ports](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/tor-switch-connections.png)

**Figure 2.** The chassis and bare metal nodes, with labelled ports.

![Chassis and nodes with numbers indicating certain ports](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/chassis-connections.png)

## Verify the cabling

  1. Verify that port labeled "1" on the TOR switch (Figure 1) is connected to the port labeled "1" in the Chassis and Nodes (Figure 2).
  2. Continue the process for the ports 2, 4, 5, 7, 8, 13, and 14 on the TOR switch (Figure 1), verifying that each is connected to the corresponding numbered port on the chassis or nodes (Figure 2).
  3. Connect port 16 and 17 of the TOR switch to your network.

ToR Switch Port (xx-aa-tesw01) | Connected Device | Device Port | Notes  
---|---|---|---  
`eth1/1` | Server 1 (bm01) | `s1p1` | Data  
`eth1/2` | Server 1 (bm01) | `s1p2` | Data  
`eth1/4` | Server 2 (bm02) | `s1p1` | Data  
`eth1/5` | Server 2 (bm02) | `s1p2` | Data  
`eth1/7` | Server 3 (bm03) | `s1p1` | Data  
`eth1/8` | Server 3 (bm03) | `s1p2` | Data  
`eth1/10` | Management device (laptop or edge router) | N/A | Management (must use source IP `198.18.0.30`)  
`eth1/13` | Chassis (chs01) | `iLO` | Management (HPE iLO)  
`eth1/14` | Chassis (chs01) | `LOM1` | Management (LAN on Motherboard)  
  
Explanation of terms:

     * tesw01: Top of Rack switch.
     * ethx/xx: Port number on the switch.
     * bm0x: Bare metal server (e.g., bm01 is Server 1).
     * s1p1, s1p2: Network ports on the servers.
     * chs01: Chassis.
     * iLO: HPE Integrated Lights-Out port for out-of-band management.
     * LOM1: LAN on motherboard port on the chassis.

**Figure 3.** The connections between the ports.

![Connections between the switch and the chassis and nodes](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/connect-ports.png)

  4. Verify that link lights show green for all of the ports you have verified in the previous steps.

If the link lights remain yellow or red, try again with different cables or hardware before opening a support case.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
