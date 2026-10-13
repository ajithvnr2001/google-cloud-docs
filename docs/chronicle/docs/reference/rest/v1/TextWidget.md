---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TextWidget/
title: TextWidget \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:06.925515+00:00
---

# TextWidget  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TextWidget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  TextWidget Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Text widget.

JSON representation  
---  
      
    
    {
      "text": string,
      "title": string,
      "order": integer,
      "type": enum ([WidgetTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetTemplateType)),
      "gridColumns": enum ([WidgetTemplateGridColumns](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetTemplateGridColumns)),
      "description": string,
      "identifier": string,
      "jsonData": string,
      "errorJsonData": string,
      "resultStatus": enum ([WidgetResultStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetResultStatus))
    }  
  
Fields  
---  
`text` |  `string` Output only. The text of the widget.  
`title` |  `string` Output only. The widget title.  
`order` |  `integer` Output only. The widget order.  
`type` |  `enum (`[WidgetTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetTemplateType)`)` Output only. The widget template type.  
`gridColumns` |  `enum (`[WidgetTemplateGridColumns](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetTemplateGridColumns)`)` Output only. The widget template grid columns.  
`description` |  `string` Output only. The widget description.  
`identifier` |  `string` Output only. The widget identifier.  
`jsonData` |  `string` Output only. The widget json data.  
`errorJsonData` |  `string` Output only. The widget error json data.  
`resultStatus` |  `enum (`[WidgetResultStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetResultStatus)`)` Output only. The widget result status.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
