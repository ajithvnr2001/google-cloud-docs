---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata/
title: MultimodalDatasetMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:58:45.453356+00:00
---

# MultimodalDatasetMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  MultimodalDatasetMetadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata of Multimodal Datasets.

Fields  
  
`inputConfig` `object (`[MultimodalDatasetInputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata#MultimodalDatasetInputConfig)`)` Specifies the input source and configuration. | `geminiRequestReadConfig` `object (`[GeminiRequestReadConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig)`)` The configuration for how to read Gemini requests from the dataset. | `keyColumnName` `string` The name of the column in the BigQuery table that contains the keys of the rows. | JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([MultimodalDatasetInputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata#MultimodalDatasetInputConfig))
      },
      "geminiRequestReadConfig": {
        object ([GeminiRequestReadConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig))
      },
      "keyColumnName": string
    }  
  
## MultimodalDatasetInputConfig

Specifies the input source and configuration.

Fields  
  
`source` `Union type`  
  
The source of the input. We only support BigQuery as source for now. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bigquerySource` `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata#BigQuerySource)`)` BigQuery source table. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // source
      "bigquerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MultimodalDatasetMetadata#BigQuerySource))
      }
      // Union type
    }  
  
## BigQuerySource

Specifies the BigQuery source.

Fields  
  
`uri` `string` The URI of a BigQuery table. e.g. <bq://project.bqDataset.bqTable> | JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
