---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate/
title: TableCandidate \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:57.745254+00:00
---

# TableCandidate  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  TableCandidate Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FieldSuggestion
    * JSON representation



A retrieved BigQuery table candidate.

JSON representation  
---  
      
    
    {
      "linkedResource": string,
      "iclString": string,
      "fieldSuggestions": [
        {
          object ([FieldSuggestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate#FieldSuggestion))
        }
      ]
    }  
  
Fields  
---  
`linkedResource` |  `string` The fully qualified resource name of the candidate in its source system, if applicable. E.g. for BigQuery tables, the format is: `bigquery.googleapis.com/projects/{projectId}/datasets/{datasetId}/tables/{tableId}`.  
`iclString` |  `string` In-context-learning string. For example, could be in DDL format.  
`fieldSuggestions[]` |  `object (`[FieldSuggestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate#FieldSuggestion)`)` Suggested field descriptions for this candidate, if requested.  
  
## FieldSuggestion

A suggested description for a field.

JSON representation  
---  
      
    
    {
      "field": string,
      "suggestedDescription": string,
      "nested": [
        {
          object ([FieldSuggestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate#FieldSuggestion))
        }
      ]
    }  
  
Fields  
---  
`field` |  `string` The field name.  
`suggestedDescription` |  `string` The suggested description, if descriptions were requested.  
`nested[]` |  `object (`[FieldSuggestion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/TableCandidate#FieldSuggestion)`)` Suggestions for nested fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
