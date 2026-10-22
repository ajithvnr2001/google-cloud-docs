---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/network/inbound/
title: Inbound networking \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:09.979749+00:00
---

# Inbound networking  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/network/inbound/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Inbound networking Stay organized with collections  Save and categorize content based on your preferences. 

CX Agent Studio offers services using [Google APIs](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) (`ces.googleapis.com`) designed for high performance and low latency, leveraging Google's extensive global network infrastructure, including its many [Points of Presence (PoPs)](https://en.wikipedia.org/wiki/Point_of_presence). Google advertises the IP addresses for its APIs and services using [Anycast](https://en.wikipedia.org/wiki/Anycast) from numerous Edge PoP locations worldwide. With Anycast, the same IP prefix is announced simultaneously from multiple points in Google's network. When a user or application makes a request to a Google API, the internet's routing fabric directs the traffic to the topologically nearest Google PoP advertising that IP address. This "nearest" is in terms of network hops and routing metrics, which generally correlates with geographical proximity. This minimizes the distance traffic has to travel over the public internet, reducing latency by getting the request onto Google's high-performance, low-congestion global backbone network as quickly as possible.

![inbound architecture](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/network-inbound-1.png)

To optimize your connection to Google services, you can move beyond standard internet routing by using [Verified Peering Provider (VPP)](https://docs.cloud.google.com/network-connectivity/docs/verified-peering-provider) or [Direct Peering](https://docs.cloud.google.com/network-connectivity/docs/direct-peering). Both options reduce network hops by connecting your infrastructure more directly to Google's edge.

Direct private connectivity using hybrid networking (including [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview)) to CX Agent Studio is not supported. To mitigate data exfiltration risks and enhance security, it is recommended to implement [VPC Service Controls (VPC-SC).](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls)

All [CX Agent Studio deployment options](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy) are supported with inbound access.

## Connectivity options

To further optimize performance beyond standard internet routing, you can use peering options to connect infrastructure directly to Google's edge.

### Verified Peering Provider (Recommended)

[Verified Peering Provider](https://docs.cloud.google.com/network-connectivity/docs/verified-peering-provider) (VPP) identifies Internet Service Providers (ISPs) that have already established diverse, high-capacity, and redundant links to Google.

  * Ease of Use: Your ISP manages the peering complexity, BGP configurations, and maintenance.
  * Reliability: Partners are vetted by Google to ensure they meet strict performance and redundancy standards.



### Direct peering

This provides a physical, [direct interconnection](https://docs.cloud.google.com/network-connectivity/docs/direct-peering) between your on-premises network and Google's edge at a mutual Point of Presence (PoP). This service is not the same as the interconnect offerings to establish connectivity to Google Cloud VPC networks.

  * Control: You establish a direct BGP session with Google.
  * Infrastructure: Requires your own registered Autonomous System (AS) number and physical presence in a colocation facility where Google peers.



### Choosing connectivity option

Feature | Verified Peering Provider | Direct Peering  
---|---|---  
**Best For** | Simplified, managed high-availability access. | Organizations requiring direct control over BGP.  
**Management** | Fully managed by your ISP. | Self-managed by your internal network team.  
**Expertise** | Low — no deep networking expertise needed. | High — requires AS number and BGP knowledge.  
**SLA** | Vetted for reliability. | No Google-provided SLA.  
  
In essence:

  * Choose Verified Peering Provider if you want a simpler, more managed way to get reliable and high-availability access to all Google services, without needing deep networking expertise.
  * Choose Direct Peering if you have the technical capability to manage BGP peering, meet Google's requirements, and want direct control over the interconnection, understanding that it comes without a Google-provided SLA.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
