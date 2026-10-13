---
url: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.StreamMetastorePartitionsResponse
title: Class StreamMetastorePartitionsResponse (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:16.365869+00:00
---

# Class StreamMetastorePartitionsResponse (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1beta.types.StreamMetastorePartitionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamMetastorePartitionsResponse (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.2  2.35.0  2.34.0  2.33.1  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.2  2.15.0  2.14.2  2.13.2  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.8.0  0.7.0  0.6.0 
    
    
    StreamMetastorePartitionsResponse(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

This is the response message sent by the server to the client for the [Partitions.StreamMetastorePartitions][] method when the commit is successful. Server will close the stream after sending this message.

## Attributes  
  
---  
**Name** | **Description**  
`total_partitions_streamed_count` |  `int`   
Total count of partitions streamed by the client during the lifetime of the stream. This is only set in the final response message before closing the stream.   
`total_partitions_inserted_count` |  `int`   
Total count of partitions inserted by the server during the lifetime of the stream. This is only set in the final response message before closing the stream.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
