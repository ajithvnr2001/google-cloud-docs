---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiOperation
title: Class DiscoveredApiOperation (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:39.001944+00:00
---

# Class DiscoveredApiOperation (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiOperation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DiscoveredApiOperation (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    DiscoveredApiOperation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DiscoveredApiOperation represents an API Operation observed in one of the sources.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`http_operation` |  `[google.cloud.apihub_v1.types.HttpOperationDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.HttpOperationDetails)`   
Optional. An HTTP Operation. This field is a member of `oneof`_ `operation`.   
`name` |  `str`   
Identifier. The name of the discovered API Operation. Format: `projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}/discoveredApiOperations/{discovered_api_operation}`  
`first_seen_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. First seen time stamp   
`last_seen_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. Last seen time stamp   
`count` |  `int`   
Optional. The number of occurrences of this API Operation.   
`classification` |  `[google.cloud.apihub_v1.types.DiscoveredApiOperation.Classification](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiOperation.Classification)`   
Output only. The classification of the discovered API operation.   
`match_results` |  `MutableSequence[[google.cloud.apihub_v1.types.DiscoveredApiOperation.MatchResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiOperation.MatchResult)]`   
Output only. The list of matched results for the discovered API operation. This will be populated only if the classification is known. The current usecase is for a single match. Keeping it repeated to support multiple matches in future.   
`source_metadata` |  `[google.cloud.apihub_v1.types.SourceMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SourceMetadata)`   
Output only. The metadata of the source from which the api operation was collected.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time stamp of the discovered API operation in API Hub.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time stamp of the discovered API operation in API Hub.   
  
## Classes 

### Classification
    
    
    Classification(value)

The classification of the discovered API operation.

### MatchResult
    
    
    MatchResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

MatchResult represents the result of matching a discovered API operation with a catalog API operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
