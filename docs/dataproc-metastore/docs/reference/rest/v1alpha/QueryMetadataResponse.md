---
url: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1alpha/QueryMetadataResponse/
title: QueryMetadataResponse \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:54.886754+00:00
---

# QueryMetadataResponse  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1alpha/QueryMetadataResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Reference ](https://docs.cloud.google.com/dataproc-metastore/docs/reference)



Send feedback 

#  QueryMetadataResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[DataprocMetastore.QueryMetadata](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1alpha/projects.locations.services/queryMetadata#google.cloud.metastore.v1alpha.DataprocMetastore.QueryMetadata)`.

JSON representation  
---  
      
    
    {
      "resultManifestUri": string
    }  
  
Fields  
---  
`resultManifestUri` |  `string` The manifest URI is link to a JSON instance in Cloud Storage. This instance manifests immediately along with QueryMetadataResponse. The content of the URI is not retriable until the long-running operation query against the metadata finishes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
