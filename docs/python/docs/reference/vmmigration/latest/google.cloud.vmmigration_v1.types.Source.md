---
url: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.Source
title: Class Source (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:22.048213+00:00
---

# Class Source (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.Source

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Source (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.3  1.10.0  1.9.1  1.8.5  1.7.0  1.6.2  1.5.1  1.4.0  1.3.3  1.2.0  1.1.2  1.0.0  0.1.0 
    
    
    Source(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Source message describes a specific vm migration Source resource. It contains the source environment information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`vmware` |  `[google.cloud.vmmigration_v1.types.VmwareSourceDetails](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.VmwareSourceDetails)`   
Vmware type source details. This field is a member of `oneof`_ `source_details`.   
`aws` |  `[google.cloud.vmmigration_v1.types.AwsSourceDetails](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.AwsSourceDetails)`   
AWS type source details. This field is a member of `oneof`_ `source_details`.   
`azure` |  `[google.cloud.vmmigration_v1.types.AzureSourceDetails](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.AzureSourceDetails)`   
Azure type source details. This field is a member of `oneof`_ `source_details`.   
`name` |  `str`   
Output only. The Source name.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The create time timestamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The update time timestamp.   
`labels` |  `MutableMapping[str, str]`   
The labels of the source.   
`description` |  `str`   
User-provided description of the source.   
`encryption` |  `[google.cloud.vmmigration_v1.types.Encryption](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.Encryption)`   
Optional. Immutable. The encryption details of the source data stored by the service.   
  
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
