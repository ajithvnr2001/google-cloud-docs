---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata/
title: NearestNeighborSearchOperationMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:12:12.072215+00:00
---

# NearestNeighborSearchOperationMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  NearestNeighborSearchOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Runtime operation metadata with regard to Matching Engine Index.

Fields  
  
`contentValidationStats[]` `object (`[ContentValidationStats](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata#ContentValidationStats)`)` The validation stats of the content (per file) to be inserted or updated on the Matching Engine Index resource. Populated if contentsDeltaUri is provided as part of `[Index.metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.indexes#Index.FIELDS.metadata)`. Please note that, currently for those files that are broken or has unsupported file format, we will not have the stats for those files. | `dataBytesCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The ingested data size in bytes. | JSON representation  
---  
      
    
    {
      "contentValidationStats": [
        {
          object ([ContentValidationStats](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata#ContentValidationStats))
        }
      ],
      "dataBytesCount": string
    }  
  
## ContentValidationStats

Fields  
  
`sourceGcsUri` `string` Cloud Storage URI pointing to the original file in user's bucket. | `validRecordCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of records in this file that were successfully processed. | `invalidRecordCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of records in this file we skipped due to validate errors. | `partialErrors[]` `object (`[RecordError](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata#RecordError)`)` The detail information of the partial failures encountered for those invalid records that couldn't be parsed. Up to 50 partial errors will be reported. | `validSparseRecordCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of sparse records in this file that were successfully processed. | `invalidSparseRecordCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of sparse records in this file we skipped due to validate errors. | JSON representation  
---  
      
    
    {
      "sourceGcsUri": string,
      "validRecordCount": string,
      "invalidRecordCount": string,
      "partialErrors": [
        {
          object ([RecordError](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NearestNeighborSearchOperationMetadata#RecordError))
        }
      ],
      "validSparseRecordCount": string,
      "invalidSparseRecordCount": string
    }  
  
## RecordError

Fields  
  
`errorType` `enum (`[RecordErrorType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RecordErrorType)`)` The error type of this record. | `errorMessage` `string` A human-readable message that is shown to the user to help them fix the error. Note that this message may change from time to time, your code should check against errorType as the source of truth. | `sourceGcsUri` `string` Cloud Storage URI pointing to the original file in user's bucket. | `embeddingId` `string` Empty if the embedding id is failed to parse. | `rawRecord` `string` The original content of this record. | JSON representation  
---  
      
    
    {
      "errorType": enum ([RecordErrorType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RecordErrorType)),
      "errorMessage": string,
      "sourceGcsUri": string,
      "embeddingId": string,
      "rawRecord": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
