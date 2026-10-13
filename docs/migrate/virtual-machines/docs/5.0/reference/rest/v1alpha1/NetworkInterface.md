---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface/
title: NetworkInterface \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:10.927703+00:00
---

# NetworkInterface  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  NetworkInterface Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ComputeEngineNetworkTier



NetworkInterface represents a NIC of a VM.

JSON representation  
---  
      
    
    {
      "network": string,
      "subnetwork": string,
      "internalIp": string,
      "externalIp": string,
      "networkTier": enum ([ComputeEngineNetworkTier](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface#ComputeEngineNetworkTier))
    }  
  
Fields  
---  
`network` |  `string` The network to connect the NIC to.  
`subnetwork` |  `string` Optional. The subnetwork to connect the NIC to.  
`internalIp` |  `string` Optional. The internal IP to define in the NIC. The formats accepted are: `ephemeral` \ ipv4 address \ a named address resource full path.  
`externalIp` |  `string` Optional. The external IP to define in the NIC.  
`networkTier` |  `enum (`[ComputeEngineNetworkTier](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface#ComputeEngineNetworkTier)`)` Optional. The networking tier used for optimizing connectivity between instances and systems on the internet. Applies only for external ephemeral IP addresses. If left empty, will default to PREMIUM.  
  
## ComputeEngineNetworkTier

Describes the networking tier used for configuring network access configuration.

Enums  
---  
`COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED` | An unspecified network tier. Will be used as PREMIUM.  
`NETWORK_TIER_STANDARD` | A standard network tier.  
`NETWORK_TIER_PREMIUM` | A premium network tier.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
