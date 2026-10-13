---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/CloudSqlSource/
title: CloudSqlSource \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:17.793799+00:00
---

# CloudSqlSource  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/CloudSqlSource/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  CloudSqlSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Cloud SQL source import data from.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "instanceId": string,
      "databaseId": string,
      "tableId": string,
      "gcsStagingDir": string,
      "offload": boolean
    }  
  
Fields  
---  
`projectId` |  `string` The project ID that contains the Cloud SQL source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request.  
`instanceId` |  `string` Required. The Cloud SQL instance to copy the data from with a length limit of 256 characters.  
`databaseId` |  `string` Required. The Cloud SQL database to copy the data from with a length limit of 256 characters.  
`tableId` |  `string` Required. The Cloud SQL table to copy the data from with a length limit of 256 characters.  
`gcsStagingDir` |  `string` Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the Cloud SQL export to a specific Cloud Storage directory.Ensure that the Cloud SQL service account has the necessary Cloud Storage Admin permissions to access the specified Cloud Storage directory.  
`offload` |  `boolean` Option for serverless export. Enabling this option will incur additional cost. More info can be found [here](https://cloud.google.com/sql/pricing#serverless).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
