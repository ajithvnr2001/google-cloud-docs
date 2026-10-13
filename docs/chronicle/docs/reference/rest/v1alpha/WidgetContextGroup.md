---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetContextGroup/
title: WidgetContextGroup \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:10.570806+00:00
---

# WidgetContextGroup  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetContextGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  WidgetContextGroup Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ContextStringItem
    * JSON representation



Widget context group.

JSON representation  
---  
      
    
    {
      "isHighlight": boolean,
      "groupName": string,
      "hideOptions": boolean,
      "items": [
        {
          object ([ContextStringItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetContextGroup#ContextStringItem))
        }
      ]
    }  
  
Fields  
---  
`isHighlight` |  `boolean` Output only. Flag that indicates whether the context group is a highlight.  
`groupName` |  `string` Output only. The group name.  
`hideOptions` |  `boolean` Output only. Flag that indicates whether the context group is hidden.  
`items[]` |  `object (`[ContextStringItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetContextGroup#ContextStringItem)`)` Output only. The context string items.  
  
## ContextStringItem

Context string item.

JSON representation  
---  
      
    
    {
      "originalName": string,
      "name": string,
      "value": string
    }  
  
Fields  
---  
`originalName` |  `string` Output only. The original name of the property.  
`name` |  `string` Output only. The name of the context string item.  
`value` |  `string` Output only. The value of the context string item.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-25 UTC."],[],[]] 
