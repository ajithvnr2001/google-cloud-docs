---
url: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.BatchDeleteMetastorePartitionsRequest
title: Class BatchDeleteMetastorePartitionsRequest (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:32.635930+00:00
---

# Class BatchDeleteMetastorePartitionsRequest (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.BatchDeleteMetastorePartitionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchDeleteMetastorePartitionsRequest (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.2  2.35.0  2.34.0  2.33.1  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.2  2.15.0  2.14.2  2.13.2  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.8.0  0.7.0  0.6.0 
    
    
    BatchDeleteMetastorePartitionsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for BatchDeleteMetastorePartitions. The MetastorePartition is uniquely identified by values, which is an ordered list. Hence, there is no separate name or partition id field.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Reference to the table to which these metastore partitions belong, in the format of projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.   
`partition_values` |  `MutableSequence[[google.cloud.bigquery_storage_v1beta.types.MetastorePartitionValues](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.MetastorePartitionValues)]`   
Required. The list of metastore partitions (identified by its values) to be deleted. A maximum of 900 partitions can be deleted in a batch.   
`trace_id` |  `str`   
Optional. Optional trace id to be used for debugging. It is expected that the client sets the same `trace_id` for all the batches in the same operation, so that it is possible to tie together the logs to all the batches in the same operation. This is expected, but not required, to be globally unique.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
