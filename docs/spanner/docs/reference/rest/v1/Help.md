---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Help/
title: Help \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:18.118722+00:00
---

# Help  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Help/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Help Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Link
    * JSON representation



Provides links to documentation or for performing an out of band action.

For example, if a quota check failed with an error indicating the calling project hasn't enabled the accessed service, this can contain a URL pointing directly to the right place in the developer console to flip the bit.

JSON representation  
---  
      
    
    {
      "links": [
        {
          object ([Link](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Help#Link))
        }
      ]
    }  
  
Fields  
---  
`links[]` |  `object (`[Link](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Help#Link)`)` URL(s) pointing to additional information on handling the current error.  
  
## Link

Describes a URL link.

JSON representation  
---  
      
    
    {
      "description": string,
      "url": string
    }  
  
Fields  
---  
`description` |  `string` Describes what the link offers.  
`url` |  `string` The URL of the link.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
