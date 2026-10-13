---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UsableSubnetwork.Purpose
title: Class Purpose (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:47.806000+00:00
---

# Class Purpose (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UsableSubnetwork.Purpose

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Purpose (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    Purpose(value)

## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_PURPOSE` | A value indicating that the enum field is not set.  
`CUSTOM_HARDWARE_LINK` | Subnetwork used for Custom Hardware Link.  
`GLOBAL_MANAGED_PROXY` | Subnet reserved for Global Envoy-based Load Balancing.  
`INTERNAL_HTTPS_LOAD_BALANCER` | Subnet reserved for Internal HTTP(S) Load Balancing. This is a legacy purpose, please use REGIONAL_MANAGED_PROXY instead.  
`PEER_MIGRATION` | Subnetwork will be used for Migration from one peered VPC to another. (a transient state of subnetwork while migrating resources from one project to another).  
`PRIVATE` | Regular user created or automatically created subnet.  
`PRIVATE_NAT` | Subnetwork used as source range for Private NAT Gateways.  
`PRIVATE_RFC_1918` | Regular user created or automatically created subnet.  
`PRIVATE_SERVICE_CONNECT` | Subnetworks created for Private Service Connect in the producer network.  
`REGIONAL_MANAGED_PROXY` | Subnetwork used for Regional Envoy-based Load Balancing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
