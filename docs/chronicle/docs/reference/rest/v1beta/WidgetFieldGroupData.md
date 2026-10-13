---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/WidgetFieldGroupData/
title: WidgetFieldGroupData \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:08.330744+00:00
---

# WidgetFieldGroupData  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/WidgetFieldGroupData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  WidgetFieldGroupData Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * WidgetFieldData
    * JSON representation



Widget field group data.

JSON representation  
---  
      
    
    {
      "order": integer,
      "groupName": string,
      "items": [
        {
          object ([WidgetFieldData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/WidgetFieldGroupData#WidgetFieldData))
        }
      ],
      "sourceUrl": string,
      "isIntegration": boolean,
      "isHighlight": boolean,
      "isManuallyCreated": boolean
    }  
  
Fields  
---  
`order` |  `integer` Output only. Field group order.  
`groupName` |  `string` Output only. Field group name.  
`items[]` |  `object (`[WidgetFieldData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/WidgetFieldGroupData#WidgetFieldData)`)` Output only. The list of fields in the field group.  
`sourceUrl` |  `string` Output only. The entity source URL.  
`isIntegration` |  `boolean` Output only. Flag that indicates whether the field group is related to a specific integration or not.  
`isHighlight` |  `boolean` Output only. Flag that indicates whether the field group is highlighted.  
`isManuallyCreated` |  `boolean` Output only. Flag that indicates whether the entity is manually created or not.  
  
## WidgetFieldData

Widget field data.

JSON representation  
---  
      
    
    {
      "originalName": string,
      "name": string,
      "value": string
    }  
  
Fields  
---  
`originalName` |  `string` Output only. Field name.  
`name` |  `string` Output only. Field display name.  
`value` |  `string` Output only. Field value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-02 UTC."],[],[]] 
