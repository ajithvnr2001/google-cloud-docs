---
url: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest
title: Class FailoverInstanceRequest (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:21.026247+00:00
---

# Class FailoverInstanceRequest (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FailoverInstanceRequest (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.5  2.14.0  2.13.1  2.12.1  2.11.1  2.10.0  2.9.3  2.8.1  2.7.1  2.6.0  2.5.1  2.4.1  2.3.0  2.2.4  2.1.1  2.0.0  1.0.2  0.4.0  0.3.0 
    
    
    FailoverInstanceRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for Failover.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.   
`data_protection_mode` |  `[google.cloud.redis_v1beta1.types.FailoverInstanceRequest.DataProtectionMode](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest.DataProtectionMode)`   
Optional. Available data protection modes that the user can choose. If it's unspecified, data protection mode will be LIMITED_DATA_LOSS by default.   
  
## Classes 

### DataProtectionMode
    
    
    DataProtectionMode(value)

Specifies different modes of operation in relation to the data retention.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
