---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OptimizeRestoredDatabaseMetadata/
title: OptimizeRestoredDatabaseMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:19.835060+00:00
---

# OptimizeRestoredDatabaseMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OptimizeRestoredDatabaseMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  OptimizeRestoredDatabaseMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata type for the long-running operation used to track the progress of optimizations performed on a newly restored database. This long-running operation is automatically created by the system after the successful completion of a database restore, and cannot be cancelled.

JSON representation  
---  
      
    
    {
      "name": string,
      "progress": {
        object ([OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress))
      }
    }  
  
Fields  
---  
`name` |  `string` Name of the restored database being optimized.  
`progress` |  `object (`[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/OperationProgress)`)` The progress of the post-restore optimizations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
