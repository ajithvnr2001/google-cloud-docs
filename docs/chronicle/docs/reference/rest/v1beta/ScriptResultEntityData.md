---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/ScriptResultEntityData/
title: ScriptResultEntityData \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:22.136833+00:00
---

# ScriptResultEntityData  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/ScriptResultEntityData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  ScriptResultEntityData Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The result entity data of the API action.

JSON representation  
---  
      
    
    {
      "title": string,
      "type": string,
      "csvLines": [
        string
      ],
      "attachments": {
        string: string,
        ...
      },
      "htmls": {
        string: string,
        ...
      },
      "links": [
        string
      ],
      "content": string,
      "rawJson": string,
      "entity": string,
      "markdowns": {
        string: string,
        ...
      },
      "isForEntity": boolean
    }  
  
Fields  
---  
`title` |  `string` Output only. The title of the result entity data.  
`type` |  `string` Output only. The type of the result entity data.  
`csvLines[]` |  `string` Output only. The csv lines of the result entity data.  
`attachments` |  `map (key: string, value: string)` Output only. The attachments of the result entity data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`htmls` |  `map (key: string, value: string)` Output only. The htmls of the result entity data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`links[]` |  `string` Output only. The links of the result entity data.  
`content` |  `string` Output only. The content of the result entity data.  
`rawJson` |  `string` Output only. The raw json of the result entity data.  
`entity` |  `string` Output only. The entity of the result entity data.  
`markdowns` |  `map (key: string, value: string)` Output only. The markdowns of the result entity data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`isForEntity` |  `boolean` Output only. The flag that indicates whether the result entity data is for entity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-02 UTC."],[],[]] 
