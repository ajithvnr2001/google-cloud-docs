---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse/
title: PartitionResponse \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:20.217025+00:00
---

# PartitionResponse  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  PartitionResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Partition
    * JSON representation



The response for `[sessions.partitionQuery](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionQuery#google.spanner.v1.Spanner.PartitionQuery)` or `[sessions.partitionRead](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#google.spanner.v1.Spanner.PartitionRead)`

JSON representation  
---  
      
    
    {
      "partitions": [
        {
          object ([Partition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse#Partition))
        }
      ],
      "transaction": {
        object ([Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction))
      }
    }  
  
Fields  
---  
`partitions[]` |  `object (`[Partition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse#Partition)`)` Partitions created by this request.  
`transaction` |  `object (`[Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction)`)` Transaction created by this request.  
  
## Partition

Information returned for each partition returned in a PartitionResponse.

JSON representation  
---  
      
    
    {
      "partitionToken": string
    }  
  
Fields  
---  
`partitionToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` This token can be passed to `sessions.read`, `sessions.streamingRead`, `ExecuteSql`, or `sessions.executeStreamingSql` requests to restrict the results to those identified by this partition token.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
