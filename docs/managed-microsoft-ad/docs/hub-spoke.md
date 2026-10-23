---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/hub-spoke/
title: Deploy hub and spoke model \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:32.595630+00:00
---

# Deploy hub and spoke model  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/hub-spoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Deploy hub and spoke model Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to implement and manage the hub and spoke model when using Managed Microsoft AD.

## Hub and spoke on Google Cloud

The hub and spoke model is a network design where the central device, or _hub_ , is connected to multiple other devices, or _spokes_. To implement this design on Google Cloud, you create a Virtual Private Cloud (VPC) which is connected to your on-premises network via either Cloud Interconnect or VPN. The VPC serves as the hub. Using VPC peering, you can create connections to other projects and your on-premises resources, or spokes.

Though this model works for immediate peers of the hub, it doesn't scale to peers of peers. VPC peering is non-transitive and custom route exchange only supports propagating routes to an immediate peer, not to peers of peers.

## Impact on Managed Microsoft AD

To provide connectivity with authorized networks hosted in user projects, Managed Microsoft AD uses VPC peering with route exchange enabled by default. This allows connectivity between the authorized networks and the tenant projects hosted by the VPC. You can also set up Cloud Interconnect or VPN directly with an authorized network.

However, if the authorized network is a spoke or if it is peered to a network that is connected to the on-premises network, Managed Microsoft AD resources will not be able to reach on-premises resources, and vice versa. There are two possible workarounds to allow connectivity.

### Using Shared VPC

If possible, use a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). It does not rely on peering, so it is not impacted by same route exchange limitations.

### Using VPN

You can also use VPN between the hub and spokes instead of VPC peering to overcome the route exchange limitation.

![VPN workaround](https://docs.cloud.google.com/static/managed-microsoft-ad/docs/images/hub-spoke.png)

**Figure 1.** Using VPN to avoid the route exchange limitation.

This workaround is less ideal because it requires more network planning and incurs the extra cost of VPN tunnels. When you create a VPN between hub and spoke, Managed Microsoft AD is considered a direct peer of the authorized network and the routes to the hub network will be exported. When using this approach, we recommend using DNS peering between the authorized network and the hub and spokes so that DNS requests can be forwarded to Managed Microsoft AD network via the authorized network configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
