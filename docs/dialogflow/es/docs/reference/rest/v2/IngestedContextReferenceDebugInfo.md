---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo/
title: IngestedContextReferenceDebugInfo \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:30.684495+00:00
---

# IngestedContextReferenceDebugInfo  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  IngestedContextReferenceDebugInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * IngestedParameterDebugInfo
    * JSON representation
  * IngestionStatus



Debug information related to ingested context reference.

JSON representation  
---  
      
    
    {
      "projectNotAllowlisted": boolean,
      "contextReferenceRetrieved": boolean,
      "ingestedParametersDebugInfo": [
        {
          object ([IngestedParameterDebugInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo#IngestedParameterDebugInfo))
        }
      ]
    }  
  
Fields  
---  
`projectNotAllowlisted` |  `boolean` Indicates if the project is allowlisted to use ingested context reference.  
`contextReferenceRetrieved` |  `boolean` The status of context_reference retrieval from database.  
`ingestedParametersDebugInfo[]` |  `object (`[IngestedParameterDebugInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo#IngestedParameterDebugInfo)`)` Parameters ingested from the context reference.  
  
## IngestedParameterDebugInfo

Debug information related to ingested parameters from context reference.

JSON representation  
---  
      
    
    {
      "parameter": string,
      "ingestionStatus": enum ([IngestionStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo#IngestionStatus))
    }  
  
Fields  
---  
`parameter` |  `string` The name of the parameter in the context reference.  
`ingestionStatus` |  `enum (`[IngestionStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IngestedContextReferenceDebugInfo#IngestionStatus)`)` The ingestion status for this specific parameter.  
  
## IngestionStatus

Enum representing the various states of parameter ingestion.

Enums  
---  
`INGESTION_STATUS_UNSPECIFIED` | Default value, indicates that the ingestion status is not specified.  
`INGESTION_STATUS_SUCCEEDED` | Indicates that the parameter was successfully ingested.  
`INGESTION_STATUS_CONTEXT_NOT_AVAILABLE` | Indicates that the parameter was not available for ingestion.  
`INGESTION_STATUS_PARSE_FAILED` | Indicates that there was a failure parsing the parameter content.  
`INGESTION_STATUS_INVALID_ENTRY` | Indicates that the context reference had an unexpected number of content entries as Context reference should only have one entry.  
`INGESTION_STATUS_INVALID_FORMAT` | Indicates that the context reference content was not in the expected format (e.g., JSON).  
`INGESTION_STATUS_LANGUAGE_MISMATCH` | Indicates that the context reference language does not match the conversation language.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-29 UTC."],[],[]] 
