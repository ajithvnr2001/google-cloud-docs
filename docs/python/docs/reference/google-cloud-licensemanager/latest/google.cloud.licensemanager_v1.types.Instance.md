---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-licensemanager/latest/google.cloud.licensemanager_v1.types.Instance
title: Class Instance (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:10.752286+00:00
---

# Class Instance (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-licensemanager/latest/google.cloud.licensemanager_v1.types.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Instance (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.0 
    
    
    Instance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing Instance object

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. name of resource   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update time stamp   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels as key value pairs   
`state` |  `[google.cloud.licensemanager_v1.types.Instance.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-licensemanager/latest/google.cloud.licensemanager_v1.types.Instance.State)`   
Output only. The state of the VM.   
`region` |  `str`   
Output only. The location of the VM.   
`product_activation` |  `MutableMapping[str, [google.cloud.licensemanager_v1.types.ActivationState](https://docs.cloud.google.com/python/docs/reference/google-cloud-licensemanager/latest/google.cloud.licensemanager_v1.types.ActivationState)]`   
Output only. Map with Product_Name and Activation State of the VM.   
`license_version_id` |  `str`   
Output only. license version id.   
`compute_instance` |  `str`   
Required. Compute Instance resource name, i.e. projects/{project}/zones/{zone}/instances/{instance}   
  
## Classes 

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
  
### ProductActivationEntry
    
    
    ProductActivationEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

VM status enum.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
