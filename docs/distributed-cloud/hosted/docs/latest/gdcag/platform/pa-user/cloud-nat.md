---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat/
title: Cloud NAT \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:27.212364+00:00
---

# Cloud NAT  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Cloud NAT Stay organized with collections  Save and categorize content based on your preferences. 

## Overview of Cloud NAT

Cloud NAT is the evolution of the project default egress configuration. Cloud NAT is a project-scoped, zonal service limited to IPv4 traffic, and provides the following features:

  * Multiple gateways per project that can egress traffic from different sets of endpoints.
  * Multiple configurable egress IPs per gateway.
  * Multiple configurable endpoint label selectors per gateway.
  * Configurable connection timeouts per gateway.
  * Higher reliability and lower blast-radius in case of egress node failure.



The following diagram illustrates an example overview for Cloud NAT. Each gateway egresses all traffic directed to non-internal IPs from endpoints from pods or VMs (in the same project as the gateway) that have all the labels in the gateway label selector (AND matching). Endpoints in different projects or that don't fully match the label selector can't egress traffic through the gateway. Gateways will statically assign one of their egress IPs to each endpoint that egresses traffic through them. IPs from leaf subnets are used to specify the set of egress IPs that each Cloud NAT gateway can use.

![Example deployment showing multiple endpoints connecting through two gateways](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/cloudnat-overview.png)

For Example, if a pod in `project-1`, with the label `app:aa`, and with IP `192.168.0.1` issues a packet with destination IP `22.22.22.22`, it will be directed to the Cloud NAT gateway. The gateway will swap the source IP for the egress IP assigned to the pod's endpoint (`34.1.22.1`), and forward it to the **data VRF**. If a reply comes back from that VRF, it will do the reverse operation and forward the resulting packet to the pod's endpoint. The same mechanism will apply to VMs in that project and label.

![Detail of example deployment showing distinct IP addresses exposed to outside](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/cloudnat-overview-example.png)

By default the egress connections created through a Cloud NAT gateway will have the following timeouts. They can be manually configured if needed.

**Timeout** | **Default value (seconds)**  
---|---  
Non-TCP connections | 60  
Idle TCP connections | 8000  
TCP connections teardown | 10  
TCP connection establishment | 60  
  
## Limitations

  * Each endpoint can only egress through a single Cloud NAT gateway using a single egress IP address. This IP address is automatically assigned by the gateway to each endpoint. This assignment won't change unless the configuration of the endpoint or the gateway change.
  * To ensure that routing between endpoints and gateways is deterministic, Cloud NAT gateways must not have overlapping label selectors, and endpoints must not have labels matching multiple gateways.
  * If the endpoint also has routes from VPN gateways, those will have preference over the routes from Cloud NAT gateways.



## Scale limits

  * The maximum number of egress IP addresses per project is **100**. If the subnets assigned to the Cloud NAT Gateway exceeds 100, only the first 100 IPs will be used by the gateway.
  * The maximum number of parallel connections per egress IP per protocol to a specific destination IP & port is limited to **32k**. Going beyond this limit will cause connections to fail.
  * The maximum number of NAT mappings is **1k** per VPC per zone. One mapping is created for each endpoint assigned to each Cloud NAT gateway. Since one endpoint can only be assigned to a single NAT gateway, the maximum number of endpoints that can use Cloud NAT in a zone is 1k. NAT mappings DO NOT scale with the number of connections.



## Failover behaviour

In case an egress node becomes unavailable, the Cloud NAT gateways using that egress node will automatically migrate their external IPs from the unavailable node to other available egress nodes. Then the gateways will reconfigure the system to egress traffic using the other available nodes. Once the reconfiguration is complete, the endpoints that were using the unavailable node will be able to reestablish the egress connections.

**Note:** Cloud NAT gateways don't preserve connections in case of failover.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
