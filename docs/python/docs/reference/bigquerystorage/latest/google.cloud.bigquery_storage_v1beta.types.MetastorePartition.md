---
url: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.MetastorePartition
title: Class MetastorePartition (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:14.314781+00:00
---

# Class MetastorePartition (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.MetastorePartition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MetastorePartition (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.2  2.35.0  2.34.0  2.33.1  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.2  2.15.0  2.14.2  2.13.2  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.8.0  0.7.0  0.6.0 
    
    
    MetastorePartition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about a Hive partition.

## Attributes  
  
---  
**Name** | **Description**  
`values` |  `MutableSequence[str]`   
Required. Represents the values of the partition keys, where each value corresponds to a specific partition key in the order in which the keys are defined. Each value is limited to 1024 characters.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The creation time of the partition.   
`storage_descriptor` |  `[google.cloud.bigquery_storage_v1beta.types.StorageDescriptor](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.StorageDescriptor)`   
Optional. Contains information about the physical storage of the data in the partition.   
`parameters` |  `MutableMapping[str, str]`   
Optional. Additional parameters or metadata associated with the partition. Maximum size 10 KiB.   
`fields` |  `MutableSequence[[google.cloud.bigquery_storage_v1beta.types.FieldSchema](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.FieldSchema)]`   
Optional. List of columns.   
  
## Classes 

### ParametersEntry
    
    
    ParametersEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
