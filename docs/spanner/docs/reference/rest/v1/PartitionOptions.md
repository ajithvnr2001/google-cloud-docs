---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionOptions/
title: PartitionOptions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:20.051691+00:00
---

# PartitionOptions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  PartitionOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Options for a `PartitionQueryRequest` and `PartitionReadRequest`.

JSON representation  
---  
      
    
    {
      "partitionSizeBytes": string,
      "maxPartitions": string
    }  
  
Fields  
---  
`partitionSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` **Note:** This hint is currently ignored by `sessions.partitionQuery` and `sessions.partitionRead` requests.The desired data size for each partition generated. The default for this option is currently 1 GiB. This is only a hint. The actual size of each partition can be smaller or larger than this size request.  
`maxPartitions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` **Note:** This hint is currently ignored by `sessions.partitionQuery` and `sessions.partitionRead` requests.The desired maximum number of partitions to return. For example, this might be set to the number of workers available. The default for this option is currently 10,000. The maximum value is currently 200,000. This is only a hint. The actual number of partitions returned can be smaller or larger than this maximum count request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
