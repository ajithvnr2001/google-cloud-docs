---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange/
title: Route exchange with site-to-site data transfer \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:34.049436+00:00
---

# Route exchange with site-to-site data transfer  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Route exchange with site-to-site data transfer Stay organized with collections  Save and categorize content based on your preferences. 

Network Connectivity Center (NCC) lets you manage network connectivity in a hub-and-spoke model. Its data transfer feature lets you establish full mesh connectivity between your network spokes to provide communication across all your connected sites. If all spokes have the feature enabled, NCC propagates all routes that one spoke learns to all other spokes.

[ ![NCC topology.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/ncc-topology.svg) NCC topology (click to enlarge)

In the preceding topology, Spokes A, B, and C are attached to the same hub and use Cloud Router to advertise prefixes into the hub.

To enable _cross-region_ site-to-site traffic through hubs and spokes, you must [enable global routing](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes) in the VPC network associated with the hub and spokes. If all spokes are located in the same region, then global routing isn't necessary because site-to-site traffic works without enabling global routing.

The following table shows how the hub propagates prefix advertisements to other spokes.

| Routes from Spoke A | Routes from Spoke B | Routes from Spoke C  
---|---|---|---  
Routes exported to Spoke A |  | 10.3.0.0/16 is reachable through Spoke B. | 10.4.0.0/16 is reachable through Spoke C.  
Routes exported to Spoke B | 10.2.0.0/16 is reachable through Spoke A. |  | 10.4.0.0/16 is reachable through Spoke C.  
Routes exported to Spoke C | 10.2.0.0/16 is reachable through Spoke A. | 10.3.0.0/16 is reachable through Spoke B. |   
  
## What's next

  * To view a sample topology, see [Sample topology for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology).
  * To learn about high availability requirements, see [High availability requirements for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).
  * To work through a tutorial, see [Connecting two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
