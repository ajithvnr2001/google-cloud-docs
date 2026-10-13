---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.OperationMetadataV1
title: Class OperationMetadataV1 (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:03.056490+00:00
---

# Class OperationMetadataV1 (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.OperationMetadataV1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OperationMetadataV1 (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    OperationMetadataV1(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata describing an `Operation][google.longrunning.Operation]`

## Attributes  
  
---  
**Name** | **Description**  
`target` |  `str`   
Target of the operation - for example `projects/project-1/locations/region-1/functions/function-1`  
`type_` |  `[google.cloud.functions_v1.types.OperationType](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.OperationType)`   
Type of operation.   
`request` |  `google.protobuf.any_pb2.Any`   
The original request that started the operation.   
`version_id` |  `int`   
Version id of the function created or updated by an API call. This field is only populated for Create and Update operations.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The last update timestamp of the operation.   
`build_id` |  `str`   
The Cloud Build ID of the function created or updated by an API call. This field is only populated for Create and Update operations.   
`source_token` |  `str`   
An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.   
`build_name` |  `str`   
The Cloud Build Name of the function deployment. This field is only populated for Create and Update operations. `projects/`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
