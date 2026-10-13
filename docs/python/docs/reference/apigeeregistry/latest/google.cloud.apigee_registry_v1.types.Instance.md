---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Instance
title: Class Instance (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:10.874161+00:00
---

# Class Instance (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Instance (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 
    
    
    Instance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An Instance represents the instance resources of the Registry. Currently, only one instance is allowed for each project.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Format: `projects/*/locations/*/instance`. Currently only `locations/global` is supported.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Creation timestamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Last update timestamp.   
`state` |  `[google.cloud.apigee_registry_v1.types.Instance.State](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Instance.State)`   
Output only. The current state of the Instance.   
`state_message` |  `str`   
Output only. Extra information of Instance.State if the state is `FAILED`.   
`config` |  `[google.cloud.apigee_registry_v1.types.Instance.Config](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Instance.Config)`   
Required. Config of the Instance.   
  
## Classes 

### Config
    
    
    Config(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Available configurations to provision an Instance.

### State
    
    
    State(value)

State of the Instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
