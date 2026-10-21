---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/CompletionDataInputConfig/
title: CompletionDataInputConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:43:47.795781+00:00
---

# CompletionDataInputConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/CompletionDataInputConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  CompletionDataInputConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The input config source for completion data.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "bigQuerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BigQuerySource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. The source of the input.Supported `[BigQuerySource.data_schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BigQuerySource#FIELDS.data_schema)` values for suggestions imports:

  * `suggestions` (default): One JSON completion suggestion per line.
  * `denylist`: One JSON deny suggestion per line.
  * `allowlist`: One JSON allow suggestion per line. `source` can be only one of the following:

  
`bigQuerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BigQuerySource)`)` Required. BigQuery input source.Add the IAM permission "BigQuery Data Viewer" for [cloud-retail-customer-data-access@system.gserviceaccount.com](mailto:cloud-retail-customer-data-access@system.gserviceaccount.com) before using this feature otherwise an error is thrown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
