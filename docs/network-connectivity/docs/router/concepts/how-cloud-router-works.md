---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works/
title: How Cloud Router works \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:17.821014+00:00
---

# How Cloud Router works  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# How Cloud Router works

Cloud Router is an API abstraction implemented by multiple and redundant BGP tasks, a dynamic route control plane, and Virtual Private Cloud (VPC) network control and data planes. Understanding how these three software components work together helps you understand Cloud Router operations and how learned-route-best-path-selection options work.

## Software components of Cloud Router

There are several software components within Cloud Router and VPC:

Cloud Router BGP task
    Cloud Router BGP tasks are grouped together within a region. Each BGP task communicates with a dynamic route control plane for its region and group. BGP tasks don't handle packet data processing. Instead, BGP tasks manage BGP sessions to send and receive BGP prefixes.
Dynamic route control plane
    Each region contains a dynamic route control plane that communicates with BGP tasks for its region and group. In global dynamic routing mode, dynamic route control planes in one region also communicate with dynamic route control planes in other regions. Each dynamic route control plane sends messages to the VPC network control plane.
VPC network control and data planes
    

Google Cloud uses the [Andromeda network virtualization stack (PDF download)](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf) as the distributed control and data plane for VPC networking, and includes the following components:

VPC network control plane
    Each region contains a VPC network control plane that receives information from the groups of dynamic route control planes in their own region. Each VPC network control plane programs dynamic routes in receiving VPC networks. VPC network control planes also enforce dynamic route quotas.
VPC network data plane
    Each region contains a VPC network data plane that evaluates and implements dynamic routes using information from the VPC network control plane. The VPC network data plane performs packet forwarding.

## Cloud Router BGP tasks

The following table shows how many BGP tasks a Cloud Router uses for common scenarios:

Example scenario | Number of BGP tasks used to implement the Cloud Router  
---|---  
One or more interfaces, each connected to a Classic VPN tunnel.  | One BGP task  
One or more interfaces, each connected to a VLAN attachment, where the VLAN attachments are in the same edge availability domain. | One BGP task  
Any number of interfaces, each connected to an HA VPN tunnel, where the tunnels are all connected to the same interface number on one or more HA VPN gateways—for example, two tunnels, each connected to `interface 0` on different HA VPN gateways. | One BGP task  
At least two interfaces, one connected to a VLAN attachment in a single edge availability domain, and another connected to a single HA VPN tunnel, where the edge availability domain and VPN gateway interface numbers are the same—for example, the first edge availability domain in a pair of edge availability domains and the first VPN gateway interface. | One BGP task  
At least two interfaces, each connected to a Router appliance instance, where one of the interfaces is configured as a redundant interface. To create a redundant interface, use the `redundant-interface` flag (Google Cloud CLI) or the `redundantInterface` field (Compute Engine API). Router appliance is part of Network Connectivity Center. | Two BGP tasks  
At least two interfaces, each connected to a VLAN attachment, where the VLAN attachments are in different edge availability domains. | Two BGP tasks  
At least two interfaces, each connected to an HA VPN tunnel, where each tunnel is connected to different HA VPN gateway interface numbers—for example, one tunnel connected to `interface 0` of an HA VPN gateway and another tunnel connected to `interface 1` of the same gateway or a different gateway.  | Two BGP tasks  
A Cloud Router with at least the following:  


  * One interface connected to a VLAN attachment in `edge availability domain 0` and/or one interface connected to an HA VPN tunnel that is connected to `interface 0` of an HA VPN gateway.
  * One interface connected to a VLAN attachment in `edge availability domain 1` and/or one interface connected to an HA VPN tunnel that is connected to `interface 1` of an HA VPN gateway.
  * One interface connected to a Classic VPN tunnel.

| Three BGP tasks  
  
## Software maintenance

Cloud Router maintenance events release new features and improve reliability. During maintenance, new BGP tasks take over as BGP speakers and responders. Before maintenance, the last BGP task notifies its peer router in one of the following ways:

  * If the peer router supports graceful restart, Cloud Router sends a graceful restart notification (a TCP `FIN` packet).

  * If the peer router _doesn't_ support graceful restart, Cloud Router sends a BGP `CEASE` notification to the peer router to terminate the BGP session.




Cloud Router maintenance events aren't announced in advance because maintenance events are automatic and not disruptive, as long as the peer router supports graceful restart. Maintenance events are designed to complete in less than 120 seconds—thus, Cloud Router uses a [120 second graceful restart timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#graceful-restart-timer). For information about how to find completed maintenance events, see [Identify router maintenance events](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/identifying-router-events).

If the peer router supports graceful restart, the peer router logs a graceful restart event during Cloud Router maintenance. In accordance with [Section 4.2 of RFC 4724](https://datatracker.ietf.org/doc/html/rfc4724#section-4.2), the peer router must honor the 120 second Cloud Router graceful restart timer, preserving learned routes and continuing to advertise routes, in the event that:

  * Cloud Router stops sending BGP keepalive packets.

  * _Applicable only when BFD is configured_ : Cloud Router stops sending BFD packets. Consequently, the peer router _must_ honor the BFD control plane independent bit value of `0` because Cloud Router uses a control plane _dependent_ BFD implementation. For more information, see [graceful restart and BFD](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#graceful-restart-and-bfd).




If the peer router _doesn't_ support graceful restart or if a peer router has graceful restart disabled, Cloud Router sends a BGP `CEASE` notification following [Section 4.5 of RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271#section-4.5). After the `CEASE` notification, the BGP session remains down until Cloud Router replaces the BGP task. Making adjustments to the Cloud Router hold timer or the peer router hold timer doesn't prevent the BGP session from terminating.

## Planned Cloud Interconnect maintenance

When the data path becomes unavailable during [planned Cloud Interconnect maintenance](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events#planned-maintenance), the BGP session is held open for the duration of the negotiated hold timer. After the hold timer expires, Cloud Router terminates the BGP session.

## Unexpected BGP task failures

Cloud Router uses multiple BGP tasks so that HA VPN tunnel pairs, Router appliances, and VLAN attachments that meet a Cloud Interconnect SLA don't depend on a single BGP task. For more information, see the Cloud Router BGP tasks section of this document. If a Cloud Router BGP task fails unexpectedly, Cloud Router isn't able to send one of the notifications that it normally sends during software maintenance. However, both learned and advertised routes remain for the duration of the negotiated [hold timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#hold_timer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
