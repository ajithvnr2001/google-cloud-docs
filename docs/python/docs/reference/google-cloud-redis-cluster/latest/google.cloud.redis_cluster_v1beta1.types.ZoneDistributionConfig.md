---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig
title: Class ZoneDistributionConfig (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:28.346718+00:00
---

# Class ZoneDistributionConfig (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ZoneDistributionConfig (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.14 
    
    
    ZoneDistributionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Zone distribution config for allocation of cluster resources.

## Attributes  
  
---  
**Name** | **Description**  
`mode` |  `[google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig.ZoneDistributionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig.ZoneDistributionMode)`   
Optional. The mode of zone distribution. Defaults to MULTI_ZONE, when not specified.   
`zone` |  `str`   
Optional. When SINGLE ZONE distribution is selected, zone field would be used to allocate all resources in that zone. This is not applicable to MULTI_ZONE, and would be ignored for MULTI_ZONE clusters.   
  
## Classes 

### ZoneDistributionMode
    
    
    ZoneDistributionMode(value)

Defines various modes of zone distribution.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
