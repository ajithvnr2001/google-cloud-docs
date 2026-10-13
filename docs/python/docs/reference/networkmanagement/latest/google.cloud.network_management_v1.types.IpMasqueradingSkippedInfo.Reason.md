---
url: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.IpMasqueradingSkippedInfo.Reason
title: Class Reason (1.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:03.660230+00:00
---

# Class Reason (1.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.IpMasqueradingSkippedInfo.Reason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Reason (1.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.38.0 (latest)  1.37.0  1.36.0  1.35.0  1.34.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.1  1.25.3  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.17.3  1.16.0  1.15.1  1.14.0  1.13.3  1.12.0  1.11.0  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.4  1.4.0  1.3.3  1.2.1  1.1.0  1.0.2  0.2.0  0.1.1 
    
    
    Reason(value)

Reason why IP masquerading was skipped.

## Enums  
  
---  
**Name** | **Description**  
`REASON_UNSPECIFIED` | Unused default value.  
`DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE` | Masquerading not applied because destination IP is in one of configured non-masquerade ranges.  
`DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE` | Masquerading not applied because destination IP is in one of default non-masquerade ranges.  
`DESTINATION_ON_SAME_NODE` | Masquerading not applied because destination is on the same Node.  
`DEFAULT_SNAT_DISABLED` | Masquerading not applied because ip-masq-agent doesn't exist and default SNAT is disabled.  
`NO_MASQUERADING_FOR_IPV6` | Masquerading not applied because the packet's IP version is IPv6.  
`POD_USES_NODE_NETWORK_NAMESPACE` | Masquerading not applied because the source Pod uses the host Node's network namespace, including the Node's IP address.  
`NO_MASQUERADING_FOR_RETURN_PACKET` | Masquerading not applied because the packet is a return packet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
