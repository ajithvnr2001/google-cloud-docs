---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiObservation
title: Class DiscoveredApiObservation (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:38.513182+00:00
---

# Class DiscoveredApiObservation (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiObservation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DiscoveredApiObservation (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    DiscoveredApiObservation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Respresents an API Observation observed in one of the sources.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the discovered API Observation. Format: `projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}`  
`style` |  `[google.cloud.apihub_v1.types.DiscoveredApiObservation.Style](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiObservation.Style)`   
Optional. Style of ApiObservation   
`server_ips` |  `MutableSequence[str]`   
Optional. The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.   
`hostname` |  `str`   
Optional. The hostname of requests processed for this Observation.   
`last_event_detected_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. Last event detected time stamp   
`source_locations` |  `MutableSequence[str]`   
Optional. The location of the observation source.   
`api_operation_count` |  `int`   
Optional. The number of observed API Operations.   
`origin` |  `str`   
Optional. For an observation pushed from a gcp resource, this would be the gcp project id.   
`source_types` |  `MutableSequence[[google.cloud.apihub_v1.types.DiscoveredApiObservation.SourceType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DiscoveredApiObservation.SourceType)]`   
Optional. The type of the source from which the observation was collected.   
`known_operations_count` |  `int`   
Output only. The number of known API Operations.   
`unknown_operations_count` |  `int`   
Output only. The number of unknown API Operations.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time stamp of the observation in API Hub.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time stamp of the observation in API Hub.   
`source_metadata` |  `[google.cloud.apihub_v1.types.SourceMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SourceMetadata)`   
Output only. The metadata of the source from which the observation was collected.   
  
## Classes 

### SourceType
    
    
    SourceType(value)

The possible types of the source from which the observation was collected.

### Style
    
    
    Style(value)

DiscoveredApiObservation protocol style

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
