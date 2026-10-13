---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Software/
title: Software \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:50.140913+00:00
---

# Software  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Software/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Software Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Information about a software package or application.

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Permission))
        }
      ],
      "description": string,
      "vendorName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the software.  
`version` |  `string` The version of the software.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Permission)`)` System permissions granted to the software. For example, "android.permission.WRITE_EXTERNAL_STORAGE"  
`description` |  `string` The description of the software.  
`vendorName` |  `string` The name of the software vendor.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
