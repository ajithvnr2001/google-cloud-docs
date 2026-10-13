---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline
title: Class DeliveryPipeline (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:48.673235+00:00
---

# Class DeliveryPipeline (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeliveryPipeline (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    DeliveryPipeline(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A `DeliveryPipeline` resource in the Cloud Deploy API.

A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of the `DeliveryPipeline`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}`. The `deliveryPipeline` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`uid` |  `str`   
Output only. Unique identifier of the `DeliveryPipeline`.   
`description` |  `str`   
Optional. Description of the `DeliveryPipeline`. Max length is 255 characters.   
`annotations` |  `MutableMapping[str, str]`   
Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy.   
`labels` |  `MutableMapping[str, str]`   
Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. \- All characters must use UTF-8 encoding, and international characters are allowed. \- Keys must start with a lowercase letter or international character. \- Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128="" bytes.="">  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the pipeline was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Most recent time at which the pipeline was updated.   
`serial_pipeline` |  `[google.cloud.deploy_v1.types.SerialPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SerialPipeline)`   
Optional. SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`. This field is a member of `oneof`_ `pipeline`.   
`condition` |  `[google.cloud.deploy_v1.types.PipelineCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PipelineCondition)`   
Output only. Information around the state of the Delivery Pipeline.   
`etag` |  `str`   
This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
`suspended` |  `bool`   
Optional. When suspended, no new releases or rollouts can be created, but in-progress ones will complete.   
  
## Classes 

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
