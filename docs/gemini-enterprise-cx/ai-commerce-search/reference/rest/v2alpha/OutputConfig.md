---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig/
title: OutputConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:46:53.805274+00:00
---

# OutputConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  OutputConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GcsDestination
    * JSON representation
  * BigQueryDestination
    * JSON representation



The output configuration setting.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig#GcsDestination))
      },
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig#BigQueryDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. The configuration of destination for holding output data. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig#GcsDestination)`)` The Google Cloud Storage location where the output is to be written to.  
`bigqueryDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/OutputConfig#BigQueryDestination)`)` The BigQuery location where the output is to be written to.  
  
## GcsDestination

The Google Cloud Storage output destination configuration.

JSON representation  
---  
      
    
    {
      "outputUriPrefix": string
    }  
  
Fields  
---  
`outputUriPrefix` |  `string` Required. The output uri prefix for saving output data to json files. Some mapping examples are as follows: outputUriPrefix sample output(assuming the object is foo.json) ======================== ============================================= gs://bucket/ gs://bucket/foo.json gs://bucket/folder/ gs://bucket/folder/foo.json gs://bucket/folder/item_ gs://bucket/folder/item_foo.json  
  
## BigQueryDestination

The BigQuery output destination configuration.

JSON representation  
---  
      
    
    {
      "datasetId": string,
      "tableIdPrefix": string,
      "tableType": string
    }  
  
Fields  
---  
`datasetId` |  `string` Required. The ID of a BigQuery Dataset.  
`tableIdPrefix` |  `string` Required. The prefix of exported BigQuery tables.  
`tableType` |  `string` Required. Describes the table type. The following values are supported:

  * `table`: A BigQuery native table.
  * `view`: A virtual table defined by a SQL query.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
