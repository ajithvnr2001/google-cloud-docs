---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Dependency
title: Class Dependency (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:36.170704+00:00
---

# Class Dependency (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Dependency

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Dependency (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    Dependency(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A dependency resource defined in the API hub describes a dependency directed from a consumer to a supplier entity. A dependency can be defined between two Operations or between an Operation and [External API][google.cloud.apihub.v1.ExternalApi].

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the dependency in the API Hub. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`  
`consumer` |  `[google.cloud.apihub_v1.types.DependencyEntityReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DependencyEntityReference)`   
Required. Immutable. The entity acting as the consumer in the dependency.   
`supplier` |  `[google.cloud.apihub_v1.types.DependencyEntityReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DependencyEntityReference)`   
Required. Immutable. The entity acting as the supplier in the dependency.   
`state` |  `[google.cloud.apihub_v1.types.Dependency.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Dependency.State)`   
Output only. State of the dependency.   
`description` |  `str`   
Optional. Human readable description corresponding of the dependency.   
`discovery_mode` |  `[google.cloud.apihub_v1.types.Dependency.DiscoveryMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Dependency.DiscoveryMode)`   
Output only. Discovery mode of the dependency.   
`error_detail` |  `[google.cloud.apihub_v1.types.DependencyErrorDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DependencyErrorDetail)`   
Output only. Error details of a dependency if the system has detected it internally.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the dependency was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the dependency was last updated.   
`attributes` |  `MutableMapping[str, [google.cloud.apihub_v1.types.AttributeValues](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.AttributeValues)]`   
Optional. The list of user defined attributes associated with the dependency resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.   
  
## Classes 

### AttributesEntry
    
    
    AttributesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### DiscoveryMode
    
    
    DiscoveryMode(value)

Possible modes of discovering the dependency.

### State
    
    
    State(value)

Possible states for a dependency.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
