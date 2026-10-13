---
url: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/UserInfo/
title: UserInfo \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:29.071501+00:00
---

# UserInfo  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/UserInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/document-warehouse/docs/reference/rest)



Send feedback 

#  UserInfo Stay organized with collections  Save and categorize content based on your preferences. 

The user information.

JSON representation  
---  
      
    
    {
      "id": string,
      "groupIds": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` A unique user identification string, as determined by the client. The maximum number of allowed characters is 255. Allowed characters include numbers 0 to 9, uppercase and lowercase letters, and restricted special symbols (:, @, +, -, _, ~) The format is "user:[xxxx@example.com"](mailto:xxxx@example.com");  
`groupIds[]` |  `string` The unique group identifications which the user is belong to. The format is "group:[yyyy@example.com"](mailto:yyyy@example.com");  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
