---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OperationMetadata
title: Class OperationMetadata (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:44.510677+00:00
---

# Class OperationMetadata (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OperationMetadata (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    OperationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the metadata of the long-running operation.

## Attributes  
  
---  
**Name** | **Description**  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time the operation was created.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time the operation finished running.   
`target` |  `str`   
Server-defined resource path for the target of the operation.   
`verb` |  `str`   
Name of the verb executed by the operation.   
`status_detail` |  `str`   
Human-readable status of the operation, if any.   
`cancel_requested` |  `bool`   
Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have `google.longrunning.Operation.error][google.longrunning.Operation.error]` value with a `google.rpc.Status.code][google.rpc.Status.code]` of 1, corresponding to `Code.CANCELLED`.   
`api_version` |  `str`   
API version used to start the operation.   
`request_resource` |  `google.protobuf.any_pb2.Any`   
The original request that started the operation.   
`stages` |  `MutableSequence[[google.cloud.functions_v2.types.Stage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Stage)]`   
Mechanism for reporting in-progress stages   
`source_token` |  `str`   
An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.   
`build_name` |  `str`   
The build name of the function for create and update operations.   
`operation_type` |  `[google.cloud.functions_v2.types.OperationType](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.OperationType)`   
The operation type.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
