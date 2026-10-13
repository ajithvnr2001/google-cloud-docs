---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchOperationMetadata
title: Class BatchOperationMetadata (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:13.371417+00:00
---

# Class BatchOperationMetadata (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchOperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchOperationMetadata (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 
    
    
    BatchOperationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata used for long running operations returned by CTS batch APIs. It's used to replace `google.longrunning.Operation.metadata][google.longrunning.Operation.metadata]`.

## Attributes  
  
---  
**Name** | **Description**  
`state` |  `[google.cloud.talent_v4.types.BatchOperationMetadata.State](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchOperationMetadata.State)`   
The state of a long running operation.   
`state_description` |  `str`   
More detailed information about operation state.   
`success_count` |  `int`   
Count of successful item(s) inside an operation.   
`failure_count` |  `int`   
Count of failed item(s) inside an operation.   
`total_count` |  `int`   
Count of total item(s) inside an operation.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time when the batch operation is created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time when the batch operation status is updated. The metadata and the update_time is refreshed every minute otherwise cached data is returned.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time when the batch operation is finished and `google.longrunning.Operation.done][google.longrunning.Operation.done]` is set to `true`.   
  
## Classes 

### State
    
    
    State(value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
