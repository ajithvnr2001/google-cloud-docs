---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatusProto/
title: StatusProto \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:22.821907+00:00
---

# StatusProto  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/StatusProto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  StatusProto Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Wire-format for a Status object

JSON representation  
---  
      
    
    {
      "code": integer,
      "space": string,
      "message": string,
      "canonicalCode": integer,
      "messageSet": {
        object ([MessageSet](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MessageSet))
      }
    }  
  
Fields  
---  
`code` |  `integer` Numeric code drawn from the space specified below.  
`space` |  `string` Space to which this status belongs  
`message` |  `string` Detail message  
`canonicalCode` |  `integer` The canonical error code that most closely corresponds to this status.  
`messageSet` |  `object (`[MessageSet](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MessageSet)`)` Associates an arbitrary proto message with the status.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
