---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowance
title: Class ResourceAllowance (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:45.621247+00:00
---

# Class ResourceAllowance (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceAllowance (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    ResourceAllowance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The Resource Allowance description for Cloud Batch. Only one Resource Allowance is supported now under a specific location and project.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`usage_resource_allowance` |  `[google.cloud.batch_v1alpha.types.UsageResourceAllowance](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowance)`   
The detail of usage resource allowance. This field is a member of `oneof`_ `resource_allowance`.   
`name` |  `str`   
Identifier. ResourceAllowance name. For example: "projects/123456/locations/us-central1/resourceAllowances/resource-allowance-1".   
`uid` |  `str`   
Output only. A system generated unique ID (in UUID4 format) for the ResourceAllowance.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the ResourceAllowance was created.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels are attributes that can be set and used by both the user and by Batch. Labels must meet the following constraints: \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. \- All characters must use UTF-8 encoding, and international characters are allowed. \- Keys must start with a lowercase letter or international character. \- Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128="" bytes.="">  
`notifications` |  `MutableSequence[[google.cloud.batch_v1alpha.types.Notification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Notification)]`   
Optional. Notification configurations.   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
