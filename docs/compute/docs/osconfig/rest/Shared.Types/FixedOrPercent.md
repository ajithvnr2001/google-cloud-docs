---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/FixedOrPercent/
title: FixedOrPercent \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:07.709120+00:00
---

# FixedOrPercent  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/FixedOrPercent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  FixedOrPercent Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message encapsulating a value that can be either absolute ("fixed") or relative ("percent") to a value.

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "fixed": integer,
      "percent": integer
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`. Type of the value. `mode` can be only one of the following:  
`fixed` |  `integer` Specifies a fixed value.  
`percent` |  `integer` Specifies the relative value defined as a percentage, which will be multiplied by a reference value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
