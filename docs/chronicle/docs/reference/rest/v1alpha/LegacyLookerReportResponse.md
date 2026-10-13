---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyLookerReportResponse/
title: LegacyLookerReportResponse \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:12.072505+00:00
---

# LegacyLookerReportResponse  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyLookerReportResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  LegacyLookerReportResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LegacyAdvancedReportCategory



Locker Advanced Report.

JSON representation  
---  
      
    
    {
      "title": string,
      "firstViewName": string,
      "category": enum ([LegacyAdvancedReportCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyLookerReportResponse#LegacyAdvancedReportCategory)),
      "creatorGuid": string,
      "modifier": string,
      "externalId": string,
      "includeViewOnlyUsers": boolean,
      "environments": [
        string
      ],
      "environmentsJson": string,
      "id": string,
      "tenantId": string,
      "creatorFullName": string,
      "modifierFullName": string,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string
    }  
  
Fields  
---  
`title` |  `string` Optional. The title of the Looker report.  
`firstViewName` |  `string` Optional. The name of the first view in the Looker report.  
`category` |  `enum (`[LegacyAdvancedReportCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyLookerReportResponse#LegacyAdvancedReportCategory)`)` Optional. The category of the Looker report.  
`creatorGuid` |  `string` Optional. The creator guid of the Looker report.  
`modifier` |  `string` Optional. The modifier of the Looker report.  
`externalId` |  `string` Optional. The external id of the Looker report.  
`includeViewOnlyUsers` |  `boolean` Optional. Indicates if view only users should be included.  
`environments[]` |  `string` Optional. List of environments associated with the copied advanced report.  
`environmentsJson` |  `string` Optional. The JSON representation of the environments field.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The ID of the advanced report.  
`tenantId` |  `string` Optional. The tenant id of the advanced report.  
`creatorFullName` |  `string` Optional. The full name of the creator of the advanced report.  
`modifierFullName` |  `string` Optional. The full name of the modifier of the advanced report.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The creation time of the advanced report in Unix time in milliseconds.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The modification time of the advanced report in Unix time in milliseconds.  
  
## LegacyAdvancedReportCategory

The category of the advanced report.

Enums  
---  
`DEFAULT` | Default.  
`PERSONAL` | Personal.  
`SHARED` | Shared.  
`OTHER` | Other.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
