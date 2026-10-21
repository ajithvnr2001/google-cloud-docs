---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RecordErrorType/
title: RecordErrorType \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:06:16.444801+00:00
---

# RecordErrorType  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RecordErrorType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RecordErrorType Stay organized with collections  Save and categorize content based on your preferences. 

Enums  
---  
`ERROR_TYPE_UNSPECIFIED` | Default, shall not be used.  
`EMPTY_LINE` | The record is empty.  
`INVALID_JSON_SYNTAX` | Invalid json format.  
`INVALID_CSV_SYNTAX` | Invalid csv format.  
`INVALID_AVRO_SYNTAX` | Invalid avro format.  
`INVALID_EMBEDDING_ID` | The embedding id is not valid.  
`EMBEDDING_SIZE_MISMATCH` | The size of the dense embedding vectors does not match with the specified dimension.  
`NAMESPACE_MISSING` | The `namespace` field is missing.  
`PARSING_ERROR` | Generic catch-all error. Only used for validation failure where the root cause cannot be easily retrieved programmatically.  
`DUPLICATE_NAMESPACE` | There are multiple restricts with the same `namespace` value.  
`OP_IN_DATAPOINT` | Numeric restrict has operator specified in datapoint.  
`MULTIPLE_VALUES` | Numeric restrict has multiple values specified.  
`INVALID_NUMERIC_VALUE` | Numeric restrict has invalid numeric value specified.  
`INVALID_ENCODING` | File is not in UTF_8 format.  
`INVALID_SPARSE_DIMENSIONS` | Error parsing sparse dimensions field.  
`INVALID_TOKEN_VALUE` | token restrict value is invalid.  
`INVALID_SPARSE_EMBEDDING` | Invalid sparse embedding.  
`INVALID_EMBEDDING` | Invalid dense embedding.  
`INVALID_EMBEDDING_METADATA` | Invalid embedding metadata.  
`EMBEDDING_METADATA_EXCEEDS_SIZE_LIMIT` | Embedding metadata exceeds size limit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
