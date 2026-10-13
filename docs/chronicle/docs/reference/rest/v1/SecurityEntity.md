---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/SecurityEntity/
title: SecurityEntity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:37.260317+00:00
---

# SecurityEntity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/SecurityEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  SecurityEntity Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Security entity.

JSON representation  
---  
      
    
    {
      "entityType": string,
      "identifier": string,
      "caseId": integer,
      "isArtifact": boolean,
      "isEnriched": boolean,
      "isVulnerable": boolean,
      "isPivot": boolean,
      "environment": string,
      "sourceUrl": string,
      "fields": [
        {
          object ([WidgetContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetContextGroup))
        }
      ],
      "isSuspicious": boolean,
      "isInternal": boolean,
      "isManuallyCreated": boolean
    }  
  
Fields  
---  
`entityType` |  `string` Output only. The entity type.  
`identifier` |  `string` Output only. The entity identifier.  
`caseId` |  `integer` Output only. The case id of the entity.  
`isArtifact` |  `boolean` Output only. Flag that indicates whether the entity is an artifact or not.  
`isEnriched` |  `boolean` Output only. Flag that indicates whether the entity is enriched or not.  
`isVulnerable` |  `boolean` Output only. Flag that indicates whether the entity is vulnerable or not.  
`isPivot` |  `boolean` Output only. Flag that indicates whether the entity is a pivot or not.  
`environment` |  `string` Output only. The environment the entity belongs to.  
`sourceUrl` |  `string` Output only. The source URL of the entity.  
`fields[]` |  `object (`[WidgetContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WidgetContextGroup)`)` Output only. The context groups.  
`isSuspicious` |  `boolean` Output only. Flag that indicates whether the entity is suspicious or not.  
`isInternal` |  `boolean` Output only. Flag that indicates whether the entity is internal or not.  
`isManuallyCreated` |  `boolean` Output only. Flag that indicates whether the entity is manually created or not.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
