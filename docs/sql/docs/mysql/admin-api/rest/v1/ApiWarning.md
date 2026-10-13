---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ApiWarning/
title: ApiWarning \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:15.245460+00:00
---

# ApiWarning  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ApiWarning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  ApiWarning Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SqlApiWarningCode



An Admin API warning message.

JSON representation  
---  
      
    
    {
      "code": enum ([SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ApiWarning#SqlApiWarningCode)),
      "message": string,
      "region": string
    }  
  
Fields  
---  
`code` |  `enum (`[SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ApiWarning#SqlApiWarningCode)`)` Code to uniquely identify the warning type.  
`message` |  `string` The warning message.  
`region` |  `string` The region name for REGION_UNREACHABLE warning.  
  
## SqlApiWarningCode

Enums  
---  
`SQL_API_WARNING_CODE_UNSPECIFIED` | An unknown or unset warning type from Cloud SQL API.  
`REGION_UNREACHABLE` | Warning when one or more regions are not reachable. The returned result set may be incomplete.  
`MAX_RESULTS_EXCEEDS_LIMIT` | Warning when user provided maxResults parameter exceeds the limit. The returned result set may be incomplete.  
`COMPROMISED_CREDENTIALS` | Warning when user tries to create/update a user with credentials that have previously been compromised by a public data breach.  
`INTERNAL_STATE_FAILURE` | Warning when the operation succeeds but some non-critical workflow state failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-24 UTC."],[],[]] 
