---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationResultStatusType/
title: TransformationResultStatusType \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:51.933634+00:00
---

# TransformationResultStatusType  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationResultStatusType/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  TransformationResultStatusType Stay organized with collections  Save and categorize content based on your preferences. 

Enum of possible outcomes of transformations. SUCCESS if transformation and storing of transformation was successful, otherwise, reason for not transforming.

Enums  
---  
`STATE_TYPE_UNSPECIFIED` | Unused.  
`INVALID_TRANSFORM` | This is set when a finding cannot be transformed (i.e. outside user set bucket range).  
`BIGQUERY_MAX_ROW_SIZE_EXCEEDED` | This is set when a transformation is successful but cannot be stored in BigQuery because the transformed row exceeds BigQuery's max row size.  
`METADATA_UNRETRIEVABLE` | This is set when there is a finding in the custom metadata of a file, but at the write time of the transformed file, this key / value pair is unretrievable.  
`SUCCESS` | This is set when the transformation and its storage are successful.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-15 UTC."],[],[]] 
