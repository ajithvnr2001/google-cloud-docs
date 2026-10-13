---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig/
title: DocumentOutputConfig \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:00.987467+00:00
---

# DocumentOutputConfig  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  DocumentOutputConfig Stay organized with collections  Save and categorize content based on your preferences. 

Config that controls the output of documents. All documents will be written as a JSON file.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsOutputConfig": {
        object ([GcsOutputConfig](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig#GcsOutputConfig))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. The destination of the results. `destination` can be only one of the following:  
`gcsOutputConfig` |  `object (`[GcsOutputConfig](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig#GcsOutputConfig)`)` Output config to write the results to Cloud Storage.  
  
## GcsOutputConfig

The configuration used when outputting documents.

JSON representation  
---  
      
    
    {
      "gcsUri": string,
      "fieldMask": string,
      "shardingConfig": {
        object ([ShardingConfig](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig#ShardingConfig))
      }
    }  
  
Fields  
---  
`gcsUri` |  `string` The Cloud Storage uri (a directory) of the output.  
`fieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Specifies which fields to include in the output documents. Only supports top level document and pages field so it must be in the form of `{document_field_name}` or `pages.{page_field_name}`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`shardingConfig` |  `object (`[ShardingConfig](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/DocumentOutputConfig#ShardingConfig)`)` Specifies the sharding config for the output document.  
  
## ShardingConfig

The sharding config for the output document.

JSON representation  
---  
      
    
    {
      "pagesPerShard": integer,
      "pagesOverlap": integer
    }  
  
Fields  
---  
`pagesPerShard` |  `integer` The number of pages per shard.  
`pagesOverlap` |  `integer` The number of overlapping pages between consecutive shards.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
