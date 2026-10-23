---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke/
title: Add VLAN attachments to NCC Gateway spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:05.168424+00:00
---

# Add VLAN attachments to NCC Gateway spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Add VLAN attachments to NCC Gateway spokes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to route VLAN attachment traffic through an NCC Gateway spoke if you have a hub configured to the [preset mesh topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#mesh-topology).

To do so, follow these steps:

  1. [Create an NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke).

  2. [Create Secure Access Connect attachments](https://docs.cloud.google.com/secure-access-connect/docs/create-attachments).

  3. [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments#create-cloud-router) associated with the gateway.

  4. [Create a new Cloud Interconnect VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

  5. Modify route advertisements on Cloud Routers to attract traffic through the new VLAN attachment connected to NCC Gateway. Cloud Routers in gateway spokes need to use the custom advertisement mode. For more information, see [Update the base route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority).

  6. Add NCC Gateway advertised routes (GAR) to attract traffic from VPC spokes to the gateway. For instructions, see [Create and manage NCC Gateway advertised routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes).




## What's next

  * [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview)
  * [NCC Gateway setup overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview)
  * [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
