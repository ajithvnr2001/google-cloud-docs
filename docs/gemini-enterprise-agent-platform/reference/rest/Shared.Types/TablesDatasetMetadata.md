---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata/
title: TablesDatasetMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:51:53.709447+00:00
---

# TablesDatasetMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TablesDatasetMetadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata of Datasets that contain tables data.

Fields  
  
`inputConfig` `object (`[InputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#InputConfig)`)` | JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#InputConfig))
      }
    }  
  
## InputConfig

The tables Dataset's data source. The Dataset doesn't store the data directly, but only pointer(s) to its data.

Fields  
  
`source` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsSource` `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#GcsSource)`)` | `bigquerySource` `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#BigQuerySource)`)` End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // source
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#GcsSource))
      },
      "bigquerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TablesDatasetMetadata#BigQuerySource))
      }
      // Union type
    }  
  
## GcsSource

Fields  
  
`uri[]` `string` Cloud Storage URI of one or more files. Only CSV files are supported. The first line of the CSV file is used as the header. If there are multiple files, the header is the first line of the lexicographically first file, the other files must either contain the exact same header or omit the header. | JSON representation  
---  
      
    
    {
      "uri": [
        string
      ]
    }  
  
## BigQuerySource

Fields  
  
`uri` `string` The URI of a BigQuery table. e.g. <bq://projectId.bqDatasetId.bqTableId> | JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
