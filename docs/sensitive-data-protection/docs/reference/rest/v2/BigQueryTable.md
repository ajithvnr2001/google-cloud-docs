---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable/
title: BigQueryTable \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:42.471597+00:00
---

# BigQueryTable  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  BigQueryTable Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message defining the location of a BigQuery table. A table is uniquely identified by its projectId, datasetId, and table_name. Within a query a table is often referenced with a string in the format of: `<projectId>:<datasetId>.<tableId>` or `<projectId>.<datasetId>.<tableId>`.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "tableId": string
    }  
  
Fields  
---  
`projectId` |  `string` The Google Cloud project ID of the project containing the table. If omitted, project ID is inferred from the API call.  
`datasetId` |  `string` Dataset ID of the table.  
`tableId` |  `string` Name of the table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
