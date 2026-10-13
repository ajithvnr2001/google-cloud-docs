---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubInstance
title: Class ApiHubInstance (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:27.755895+00:00
---

# Class ApiHubInstance (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubInstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ApiHubInstance (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ApiHubInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An ApiHubInstance represents the instance resources of the API Hub. Currently, only one ApiHub instance is allowed for each project.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Creation timestamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Last update timestamp.   
`state` |  `[google.cloud.apihub_v1.types.ApiHubInstance.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubInstance.State)`   
Output only. The current state of the ApiHub instance.   
`state_message` |  `str`   
Output only. Extra information about ApiHub instance state. Currently the message would be populated when state is `FAILED`.   
`config` |  `[google.cloud.apihub_v1.types.ApiHubInstance.Config](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubInstance.Config)`   
Required. Config of the ApiHub instance.   
`labels` |  `MutableMapping[str, str]`   
Optional. Instance labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources   
`description` |  `str`   
Optional. Description of the ApiHub instance.   
  
## Classes 

### Config
    
    
    Config(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Available configurations to provision an ApiHub Instance.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### State
    
    
    State(value)

State of the ApiHub Instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
