---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization/
title: RangeUtilization \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:13.693457+00:00
---

# RangeUtilization  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  RangeUtilization Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Utilization metrics for an IP Range, including consumed and produced address counts.

JSON representation  
---  
      
    
    {
      "totalConsumed": string,
      "totalProduced": string,
      "usage": number
    }  
  
Fields  
---  
`totalConsumed` |  `string` Output only. The total number of IP addresses consumed in the Range.  
`totalProduced` |  `string` Output only. The total number of IP addresses produced in the Range.  
`usage` |  `number` Output only. The usage of the Range as a percentage. This is marked as optional so that we have presence tracking and API responses show 0.0 instead of NULL.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
