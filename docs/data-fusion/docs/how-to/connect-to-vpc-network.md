---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-vpc-network/
title: Connect to an external network \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:15.102476+00:00
---

# Connect to an external network  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-vpc-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Connect to an external network Stay organized with collections  Save and categorize content based on your preferences. 

To connect to a resource in an external network (an on-premises network or another Virtual Private Cloud (VPC) network), the external network and Cloud Data Fusion instance must be connected through the same VPC network.

To connect an external network to the Cloud Data Fusion VPC network using Cloud VPN tunnels with border gateway protocol (BGP) routing or VLAN attachments, do the following:

  * Ensure your VPC network is connected to the external network using a [Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or a VLAN attachment for [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).
  * Ensure the BGP sessions on the Cloud Router managing your Cloud VPN tunnels or VLAN attachments have received specific prefixes (destinations) from your external network. Default routes (destination 0.0.0.0/0) cannot be imported into the Cloud Data Fusion VPC network because that network has its own local default route. Local routes for a destination are always used, even though the Cloud Data Fusion peering is configured to import custom routes from your VPC network.
  * [Identify the peering connections](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing-connections) produced by the private services connection. Depending on the service, the private services connection might create one or more of the following peering connections, but not necessarily all of them: 
    * `datafusion-googleapis-com`
    * `servicenetworking-googleapis-com`
  * [Update all of the peering connections](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection) to enable Export custom routes.
  * [Identify the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing_allocated_ip_address_ranges) used by the private services connection.
  * [Create a Cloud Router custom advertised route](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for the allocated range on the Cloud Routers managing BGP sessions for your Cloud VPN tunnels or VLAN attachments.



## What's next

  * Learn how to [create a private instance in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
