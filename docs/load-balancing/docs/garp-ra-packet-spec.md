---
url: https://docs.cloud.google.com/load-balancing/docs/garp-ra-packet-spec/
title: GARP and RA packet specifications for HA policy with fast IP move \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:47.765389+00:00
---

# GARP and RA packet specifications for HA policy with fast IP move  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/garp-ra-packet-spec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Reference ](https://docs.cloud.google.com/load-balancing/docs/apis)



Send feedback 

#  GARP and RA packet specifications for HA policy with fast IP move Stay organized with collections  Save and categorize content based on your preferences. 

The following sections specify the GARP and RA packet specifications required by Google Cloud when the `haPolicy.fastIPMove` backend service parameter is set to `GARP_RA`.

## GARP packet format for IPv4 traffic

The following fields are required when you use a GARP packet to trigger a new leader.

Sender MAC address | MAC address of the sender VM instance (the new leader).  
---|---  
Sender IPv4 address | The `/32` IPv4 address that is moving to the new leader.  
Target MAC address | Broadcast MAC address: `FF-FF-FF-FF-FF-FF`  
Target IPv4 address | Same as the sender IPv4 address.  
ARP operation | `ARPOP_REPLY`: 2  
  
## RA packet format for IPv6 traffic

RA supports advertising multiple IPv6 prefix ranges in a single RA packet by attaching multiple ICMPv6 [prefix information options](https://www.rfc-editor.org/rfc/rfc4861#section-4.6.2).

When `haPolicy.fastIPMove` is set to `GARP_RA`, every IPv6 prefix range in a single RA packet should be an exact match to a forwarding rule IP address, and all of those forwarding rules must point to the same regional backend service.

If the set of IPv6 prefix ranges are served by different regional backend services, the RA packet is treated as invalid and doesn't trigger a fast IP move.

The following fields are required when you use an RA packet to trigger a new leader.

Sender MAC address | MAC address of the sender VM instance (the new leader).  
---|---  
Sender IPv6 address | Link-local IPv6 address of the sender VM instance. This is not the IPv6 address that is moving to the new leader.  
Target MAC address | All node multicast MAC address: `33-33-00-00-00-01`  
Target IPv6 address | IPv6 all node multicast address: `FF02::1`  
IPv6 hop limit | 255  
ICMPv6 type | `ND_ROUTER_ADVERT`: 134  
ICMPv6 options type | `ND_OPT_PREFIX_INFORMATION`: 3  
Prefix information option prefix | The IPv6 prefix that is moving to the new leader. Bits after the prefix must be zero.  
Prefix information option prefix length | The length of IPv6 prefix that is moving to the new leader.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
